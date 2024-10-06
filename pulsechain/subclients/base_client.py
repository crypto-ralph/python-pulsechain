"""
Base class for subclients.
All subclients must inherit SubpathClient.
"""
from abc import ABC, abstractmethod

import httpx

from pulsechain.exceptions import (
    PulseChainBadParamException,
    PulseChainBadRequestException,
    PulseChainServerError,
    PulseChainTimeoutException,
    PulseChainUnknownException,
    PulseChainUnprocessableEntityException,
)


class BaseClient(ABC):
    def __init__(self):
        """
        Initialize the BaseClient with the PulseChain API base URL.
        """
        self.base_url = "https://api.scan.pulsechain.com/api/v2"

    @abstractmethod
    def _explorer_get_request(self, path: str, params: dict | None = None) -> dict:
        """
        Perform a GET request to the PulseChain API explorer.

        This method sends a GET request to the specified path on the PulseChain API
        explorer and handles any errors that might occur during the request, such as
        timeouts or bad requests.

        :param path: The API path to send the request to.
        :param params: Optional parameters to include in the request.
        :return: The response from the API if the request is successful.
        """
        try:
            response = httpx.get(f"{self.base_url}/{path}", params=params, timeout=60)
        except httpx.ReadTimeout as exc:
            raise PulseChainTimeoutException(exc.args[0]) from exc
        return self._check_result(response)

    @staticmethod
    def _check_result(response: httpx.Response) -> dict:
        """
        Check the result of the API response and handle errors.

        This method checks the HTTP status code of the response and raises the appropriate
        exception if the request was not successful.

        :param response: The response object from the PulseChain API.
        :return: The parsed JSON response if the status code is 200.
        :raises PulseChainServerError: If the response status code is 500.
        :raises PulseChainUnprocessableEntityException: If the response status code is 422.
        :raises PulseChainBadRequestException: If the response status code is 400.
        :raises PulseChainUnknownException: If the response status code is not recognized.
        """

        if response.status_code == 200:
            return response.json()
        if response.status_code == 500:
            raise PulseChainServerError(response)
        if response.status_code == 422:
            raise PulseChainUnprocessableEntityException(response)
        if response.status_code == 400:
            raise PulseChainBadRequestException(response)
        raise PulseChainUnknownException(f"{response.status_code}: {response.text}")

    @staticmethod
    def _validate_token_type(token_type: list[str]) -> str:
        """
        Validate the token type filter.

        :param list[str] token_type: A list of token types to validate.
                                     Valid options are 'ERC-20', 'ERC-721', or 'ERC-1155'.
        :returns: String with comma separated token types if valid
        :rtype: str
        :raises PulseChainBadParamException: If any `token_type` is not a valid type.
        """
        valid_token_types = {"ERC-20", "ERC-721", "ERC-1155"}
        for t_type in token_type:
            if t_type not in valid_token_types:
                raise PulseChainBadParamException(
                    "token_type must be either 'ERC-20', 'ERC-721', or 'ERC-1155'"
                )
        return ",".join(token_type)


class SubpathClient(BaseClient):
    def __init__(self, subpath: str):
        super().__init__()
        self.subpath = subpath

    def _explorer_get_request(
        self, path: str | None = None, params: dict | None = None
    ):
        path = f"{self.subpath}/{path}" if path else self.subpath
        return super()._explorer_get_request(f"{path}", params)

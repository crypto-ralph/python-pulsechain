from abc import ABC, abstractmethod

import httpx

from pulsechain.exceptions import (
    PulseChainTimeoutException,
    PulseChainServerError,
    PulseChainUnprocessableEntityException,
    PulseChainUnknownException,
    PulseChainBadRequestException,
    PulseChainBadParamException,
)


class BaseClient(ABC):
    def __init__(self):
        self.base_url = "https://api.scan.pulsechain.com/api/v2"

    @abstractmethod
    def _explorer_get_request(self, path: str, params: dict | None = None) -> dict:
        """
        Get request to the explorer API.
        :param path: API path
        :param params: Additional parameters for the request.
        :return: Response from the API if the call was successful.
        """
        try:
            response = httpx.get(f"{self.base_url}/{path}", params=params, timeout=60)
        except httpx.ReadTimeout as exc:
            raise PulseChainTimeoutException(exc.args[0]) from exc
        return self._check_result(response)

    @staticmethod
    def _check_result(response: httpx.Response) -> dict:
        """
        :param response: Response from the API to be checked.
        :return: Unwrapped result if the call was successful.
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

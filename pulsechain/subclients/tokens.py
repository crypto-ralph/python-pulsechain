from pulsechain.models import BaseResponse
from pulsechain.subclients.base_client import SubpathClient
from pulsechain.utils import paginated


class TokensClient(SubpathClient):
    def __init__(self):
        """
        Initialize the TokensClient with the subpath 'tokens'.
        """
        super().__init__(subpath="tokens")

    @paginated
    def get_tokens(
        self,
        name_query: str,
        token_type: list[str] | None = None,
        params: dict | None = None,
    ) -> tuple[BaseResponse, dict]:
        """
        Get tokens matching the query.

        :param name_query: The query to search for.
        :param list[str] token_type: A list of token types to filter the balances. Valid options are ``'ERC-20'``,
            ``'ERC-721'``, or ``'ERC-1155'``. Defaults to None.
        :param dict params: Additional parameters for the request.
        :return: A list of tokens matching the query.
        """
        if params:
            params["q"] = name_query
            if token_type:
                params["type"] = self._validate_token_type(token_type)

        response = self._explorer_get_request(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_info(self, address: str) -> BaseResponse:
        """
        Get information about token specific to an address.
        :param address: The address for which to fetch information.
        :return: A dictionary containing information about the token.
        """
        response = self._explorer_get_request(address)
        return BaseResponse(items=[response])

    @paginated
    def get_transfers(self, address: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Get token transfers for a token.
        :param address: The token address for which to fetch transfers.
        :param params: Additional parameters for the request.
        :return: Response object containing token transfers.
        """
        repsonse = self._explorer_get_request(f"{address}/transfers", params=params)
        return BaseResponse(items=repsonse["items"]), repsonse["next_page_params"]

    @paginated
    def get_holders(self, address: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Get token holders for a token.
        :param address: The address for which to fetch holders.
        :param params: Additional parameters for the request.
        :return: Response object containing token holders.
        """
        repsonse = self._explorer_get_request(f"{address}/holders", params=params)
        return BaseResponse(items=repsonse["items"]), repsonse["next_page_params"]

    def get_counters(self, address: str) -> BaseResponse:
        """
        Get counters for a token
        :param address: Token address
        :return: Response object containing token counters
        """
        repsonse = self._explorer_get_request(f"{address}/counters")
        return BaseResponse(items=[repsonse])

    @paginated
    def get_nft_instances(
        self, address: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Get NFT instances for a token
        :param address: Token address
        :param params: Additional parameters for the request.
        :return: Response object containing NFT instances
        """
        repsonse = self._explorer_get_request(f"{address}/instances", params=params)
        return BaseResponse(items=repsonse["items"]), repsonse["next_page_params"]

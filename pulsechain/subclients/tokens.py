"""
Tokens subclient for the PulseChain API.

This module defines the TokensClient class, which handles API endpoints related to tokens.
It includes methods for fetching token information, transfers, holders, counters, and
NFT instances. The client provides search capabilities and supports paginated responses.
"""

from pulsechain.models import BaseResponse
from pulsechain.subclients.base_client import SubpathClient
from pulsechain.utils import paginated


class TokensClient(SubpathClient):
    """
    A client for accessing token-related endpoints in the PulseChain API.

    The TokensClient allows users to query for tokens, retrieve token-specific
    information, and fetch data related to token transfers, holders, and counters.
    Additionally, it provides functionality for retrieving NFT instances and supports
    paginated responses for large data sets.
    """

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
        Retrieve tokens matching the provided query.

        This method allows users to search for tokens by name and optionally filter
        by token type (ERC-20, ERC-721, or ERC-1155). Results are paginated.

        :param name_query: The query to search for token names.
        :param token_type: A list of token types to filter the results. Valid options are
                           'ERC-20', 'ERC-721', or 'ERC-1155'. Defaults to None.
        :param params: Additional parameters for the request. Defaults to None.
        :return: A tuple containing a BaseResponse object with the list of tokens and
                 a dictionary with pagination parameters for the next page.
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
        response = self._explorer_get_request(f"{address}/transfers", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_holders(self, address: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Retrieve the list of holders for a specific token.

        This method returns a list of addresses that hold the token at the specified address.
        Results are paginated.

        :param address: The token address for which to fetch holders.
        :param params: Additional parameters for the request.
        :return: A tuple containing a BaseResponse object with holder data and
                 a dictionary with pagination parameters for the next page.
        """
        response = self._explorer_get_request(f"{address}/holders", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_counters(self, address: str) -> BaseResponse:
        """
        Retrieve counter data for a specific token.

        This method fetches the counter metrics for the token at the specified address,
        which might include information like the number of transfers, holders, etc.

        :param address: The token address for which to fetch counters.
        :return: A BaseResponse object containing the token counters.
        """
        response = self._explorer_get_request(f"{address}/counters")
        return BaseResponse(items=[response])

    @paginated
    def get_nft_instances(
        self, address: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Retrieve NFT instances for a specific token.

        This method fetches the instances of NFTs (Non-Fungible Tokens) for the token
        at the specified address. Results are paginated.

        :param address: The token address for which to fetch NFT instances.
        :param params: Additional parameters for the request.
        :return: A tuple containing a BaseResponse object with NFT instance data and
                 a dictionary with pagination parameters for the next page.
        """
        response = self._explorer_get_request(f"{address}/instances", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

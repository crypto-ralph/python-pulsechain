"""
Search subclient for the PulseChain API.

This module provides the SearchClient for the PulseChain API.
It allows users to search for items and check for query redirects
within the PulseChain ecosystem.
"""

from pulsechain.models import BaseResponse
from pulsechain.subclients.base_client import SubpathClient
from pulsechain.utils import paginated


class SearchClient(SubpathClient):
    """
    A client that provides search functionality for the PulseChain API.

    This client offers methods to perform searches with specific queries
    and to check if a search query triggers a redirect. It is initialized
    with the 'search' subpath.
    """

    def __init__(self):
        """
        Initialize the SearchClient with the subpath 'search'.
        """
        super().__init__(subpath="search")

    @paginated
    def search(self, query: str, params: dict) -> tuple[BaseResponse, dict]:
        """
        Search for items.
        :param query: The query to search for.
        :param params: Additional parameters for the request.
        :return: A tuple containing a response object with the search results and the next page parameters.
        """
        params["q"] = query
        response = self._explorer_get_request(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def check_redirect(self, query: str) -> BaseResponse:
        """
        Check if a query is a redirect.
        :param query: The query to search for.
        :return: A response object with the search results.
        """
        response = self._explorer_get_request("check-redirect", params={"q": query})
        return BaseResponse(items=[response])

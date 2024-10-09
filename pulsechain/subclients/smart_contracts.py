"""
This module provides the `SmartContractsClient` class, which interacts with the 'smart-contracts'
subpath of the PulseChain API.

The `SmartContractsClient` class provides methods to retrieve information about smart contracts,
including contract details, counters, and available read and write methods. It uses the
`APIRequestHandler` for making HTTP requests.
"""
from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient


class SmartContractsClient(SubpathClient):
    """
    Client for interacting with the 'smart-contracts' subpath of the PulseChain API.

    The `SmartContractsClient` provides methods to interact with smart contract data,
    including retrieving contract counters, information, and the available read and write methods
    for verified smart contracts.

    Attributes:
        request_handler (APIRequestHandler): The handler for making HTTP requests.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the SmartContractsClient with the subpath 'smart-contracts'.

        :param request_handler: The handler for making HTTP requests.
        """
        super().__init__(subpath="smart-contracts", request_handler=request_handler)

    def get_counters(self) -> BaseResponse:
        """
        Get counters for a verified smart contracts.
        :return: Response object containing smart contracts counters
        """
        response = self.get("counters")
        return BaseResponse(items=[response])

    def get_info(self, address: str) -> BaseResponse:
        """
        Get information about a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract information
        """
        response = self.get(address)
        return BaseResponse(items=[response])

    def get_read_methods(self, address: str) -> BaseResponse:
        """
        Get read methods for a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract read methods
        """
        response = self.get(f"{address}/methods-read")
        print(response)
        return BaseResponse(items=[response])

    def get_write_methods(self, address: str) -> BaseResponse:
        """
        Get write methods for a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract write methods
        """
        response = self.get(f"{address}/methods-write")
        return BaseResponse(items=[response])

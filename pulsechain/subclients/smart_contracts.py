from pulsechain.models import BaseResponse
from pulsechain.subclients.base_client import SubpathClient


class SmartContractsClient(SubpathClient):
    def __init__(self):
        """
        Initialize the SmartContractsClient with the subpath 'smart-contracts'.
        """
        super().__init__(subpath="smart-contracts")

    def get_counters(self) -> BaseResponse:
        """
        Get counters for a verified smart contracts.
        :return: Response object containing smart contracts counters
        """
        response = self._explorer_get_request("counters")
        return BaseResponse(items=[response])

    def get_info(self, address: str) -> BaseResponse:
        """
        Get information about a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract information
        """
        response = self._explorer_get_request(address)
        return BaseResponse(items=[response])

    def get_read_methods(self, address: str) -> BaseResponse:
        """
        Get read methods for a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract read methods
        """
        response = self._explorer_get_request(f"{address}/methods-read")
        return BaseResponse(items=response)

    def get_write_methods(self, address: str) -> BaseResponse:
        """
        Get write methods for a smart contract.
        :param address: The address of the smart contract
        :return: Response object containing smart contract write methods
        """
        response = self._explorer_get_request(f"{address}/methods-write")
        return BaseResponse(items=response)

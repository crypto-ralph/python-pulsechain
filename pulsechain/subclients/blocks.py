from pulsechain.exceptions import PulseChainBadParamException
from pulsechain.models import BaseResponse
from pulsechain.subclients.base_client import SubpathClient
from pulsechain.utils import paginated


class BlocksClient(SubpathClient):
    def __init__(self):
        """
        Initialize the AddressesClient with the subpath 'transactions'.
        """
        super().__init__(subpath="blocks")

    @staticmethod
    def _validate_block_type(block_type: list[str]) -> str:
        """
        Validate the block type filter.

        :param block_type: A list of block types to validate. Valid options are 'block', 'uncle' or 'reorg'.
        :returns: String with comma separated block types if valid
        :raises PulseChainBadParamException: If any `block_type` is not a valid type.
        """
        valid_block_types = {"block", "uncle", "reorg"}
        for b_type in block_type:
            if b_type not in valid_block_types:
                raise PulseChainBadParamException(
                    "block_type must be either 'header' or 'body'"
                )
        return "|".join(block_type)

    @paginated
    def get_blocks(
        self, block_type: list[str] | None = None, params: dict | None = None
    ) -> tuple[BaseResponse, dict]:
        """
        Get information about blocks.
        :return: BaseResponse containing information about the blocks.
        """
        if params:
            if block_type:
                params["type"] = self._validate_block_type(block_type)
        response = self._explorer_get_request(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_block_info(self, block: str) -> BaseResponse:
        """
        Get information about a specific block.
        :param block: the hash or the number of the block
        :return: BaseResponse with information about the block
        """
        response = self._explorer_get_request(block)
        return BaseResponse(items=[response])

    def get_block_txns(self, block: str) -> BaseResponse:
        """
        Get transactions in a specific block.
        :param block: the hash or the number of the block
        :return: BaseResponse with information about the block transactions
        """
        response = self._explorer_get_request(f"{block}/transactions")
        return BaseResponse(items=[response])

    def get_block_withdrawals(self, block: str) -> BaseResponse:
        """
        Get withdrawals in a specific block.
        :param block: the hash or the number of the block
        :return: BaseResponse with information about the block withdrawals
        """
        response = self._explorer_get_request(f"{block}/withdrawals")
        return BaseResponse(items=[response])

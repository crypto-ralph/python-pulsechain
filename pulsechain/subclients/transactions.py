from pulsechain.subclients.base_client import SubpathClient
from pulsechain.exceptions import PulseChainBadParamException
from pulsechain.models import BaseResponse
from pulsechain.utils import paginated


class TransactionsClient(SubpathClient):
    def __init__(self):
        """
        Initialize the AddressesClient with the subpath 'transactions'.
        """
        super().__init__(subpath="transactions")

    @staticmethod
    def _validate_txn_type(txn_type: list[str]) -> str:
        """
        Validate the tx type filter.

        :param txn_type: A list of tx types to validate.
                        Valid options are 'token_transfer', 'contract_creation',
                        'contract_call', 'coin_transfer', or 'token_creation'.
        :returns: String with comma separated tx types if valid
        :raises PulseChainBadParamException: If any `tx_type` is not a valid type.
        """
        valid_txn_types = {
            "token_transfer",
            "contract_creation",
            "contract_call",
            "coin_transfer",
            "token_creation",
        }
        for t_type in txn_type:
            if t_type not in valid_txn_types:
                raise PulseChainBadParamException(
                    "tx_type must be either 'token_transfer', 'contract_creation', 'contract_call', 'coin_transfer', "
                    "or 'token_creation'"
                )
        return ",".join(txn_type)

    @staticmethod
    def _validate_txn_filter(txn_filter: list[str]) -> str:
        """
        Validate the transaction filter.

        :param str txn_filter: The transaction filter to validate. Should be either 'pending' or 'validated'.
        :returns: The validated transaction filter.
        :raises PulseChainBadParamException: If `txn_filter` is not 'pending' or 'validated'.
        """
        valid_txn_filters = {"pending", "validated"}
        for t_filter in txn_filter:
            if t_filter not in valid_txn_filters:
                raise PulseChainBadParamException(
                    "txn_filter must be either 'pending or 'validated'"
                )
        return " | ".join(txn_filter)

    @staticmethod
    def _validate_method(method: list[str]) -> str:
        """
        Validate the method filter.

        :param method: The method filter to validate.
                           Should be either 'approve', 'transfer', 'multicall', 'mint', or 'commit'.
        :returns: The validated method filter.
        :raises PulseChainBadParamException: If `method` is not 'approve', 'transfer', 'multicall', 'mint', or 'commit'.
        """
        valid_methods = {"approve", "transfer", "multicall", "mint", "commit"}
        if method not in valid_methods:
            raise PulseChainBadParamException(
                "method must be either 'approve', 'transfer', 'multicall', 'mint', or 'commit'"
            )
        return ",".join(method)

    @paginated
    def get_transactions(
        self,
        txn_filter: list[str] | None = None,
        txn_type: list[str] | None = None,
        method: list[str] | None = None,
        params: dict | None = None,
    ) -> tuple[BaseResponse, dict]:
        if params:
            if txn_filter:
                params["filter"] = self._validate_txn_filter(txn_filter)
            if txn_type:
                params["tx_type"] = self._validate_txn_type(txn_type)
            if method:
                params["method"] = self._validate_method(method)

        response = self._explorer_get_request(params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_transaction_info(self, transaction_hash: str) -> BaseResponse:
        """
        Get information about a specific transaction.
        :param transaction_hash: the hash of the transaction
        :return: A response object containing information about the transaction.
        """
        return BaseResponse(items=[self._explorer_get_request(transaction_hash)])

    @paginated
    def get_token_transfers(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Get information about a token transfers in a specific transaction.
        :param transaction_hash: the hash of the transaction
        :param dict params: Additional parameters for the request.
        :return: A response object containing information about the transaction.
        """
        response = self._explorer_get_request(
            f"{transaction_hash}/token-transfers", params=params
        )
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_internal_transactions(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """
        Get information about the internal transactions in a specific transaction.
        :param transaction_hash: the hash of the transaction
        :param dict params: Additional parameters for the request.
        :return: A response object containing information about the internal transactions.
        """
        response = self._explorer_get_request(
            f"{transaction_hash}/internal-transactions", params=params
        )
        return BaseResponse(items=response["items"]), response["next_page_params"]

    @paginated
    def get_logs(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """

        :param transaction_hash: the hash of the transaction
        :param dict params: Additional parameters for the request.
        :return:
        """
        response = self._explorer_get_request(f"{transaction_hash}/logs", params=params)
        return BaseResponse(items=response["items"]), response["next_page_params"]

    def get_raw_trace(self, transaction_hash: str) -> BaseResponse:
        """
        Get information about a specific transaction.
        :param transaction_hash: the hash of the transaction
        :return: A response object containing information about the transaction.
        """
        return BaseResponse(
            items=self._explorer_get_request(f"{transaction_hash}/raw-trace")
        )

    @paginated
    def get_state_changes(
        self, transaction_hash: str, params: dict
    ) -> tuple[BaseResponse, dict]:
        """

        :param transaction_hash: the hash of the transaction
        :param dict params: Additional parameters for the request.
        :return:
        """
        response = self._explorer_get_request(
            f"{transaction_hash}/state-changes", params=params
        )
        return BaseResponse(items=response["items"]), response["next_page_params"]

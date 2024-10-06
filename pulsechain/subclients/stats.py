from pulsechain.subclients.base_client import BaseClient


class StatsClient(BaseClient):
    def __init__(self):
        super().__init__()
        self.subpath = "stats"

    def _explorer_get_request(
        self, path: str | None = None, params: dict | None = None
    ):
        path = f"{self.subpath}/{path}" if path else self.subpath
        return super()._explorer_get_request(f"{path}", params)

    def get_stats(self) -> dict:
        """
        Get statistical counters

        :return: A dictionary representing the JSON response from the API,
                 which includes the transaction receipt status.
        :rtype: dict
        """
        response = self._explorer_get_request()
        return response

    def get_transactions_chart(self) -> dict:
        """
        Get tx_count value from last 31 days.

        :return: A dictionary representing the JSON response from the API,
                 which includes the transaction receipt status.
        :rtype: dict
        """
        response = self._explorer_get_request("charts/transactions")
        return response["chart_data"]

    def get_market_chart(self) -> dict:
        """
        No idea what this endpoint supposed to do.
        :return: Data about available supply. Currently empty
        """
        return self._explorer_get_request("charts/market")

from pulsechain.subclients.adresses import AddressesClient
from pulsechain.subclients.blocks import BlocksClient
from pulsechain.subclients.search import SearchClient
from pulsechain.subclients.smart_contracts import SmartContractsClient
from pulsechain.subclients.stats import StatsClient
from pulsechain.subclients.tokens import TokensClient
from pulsechain.subclients.transactions import TransactionsClient


class Client:
    def __init__(self):
        self.stats = StatsClient()
        self.addresses = AddressesClient()
        self.transactions = TransactionsClient()
        self.tokens = TokensClient()
        self.blocks = BlocksClient()
        self.search = SearchClient()
        self.smart_contracts = SmartContractsClient()

PulseChain API Documentation
============================

The PulseChain API provides a set of subclients that allow interaction with various blockchain resources.
This documentation covers the available subclients, response models, and usage examples.


Response Models
===============

This section documents the `BaseResponse` and `PaginatedResponse` models, which are used
to structure responses from the PulseChain API.

.. automodule:: pulsechain.models
   :members:
   :undoc-members:
   :show-inheritance:


Subclients Overview
===================

The PulseChain API consists of several subclients, each responsible for interacting with different parts of the PulseChain network.

- **Addresses Subclient**: Handles operations related to addresses.
- **Blocks Subclient**: Retrieves information about blocks.
- **Search Subclient**: Allows searching within the blockchain.
- **Smart Contracts Subclient**: Interacts with smart contracts.
- **Stats Subclient**: Provides network statistics.
- **Tokens Subclient**: Deals with tokens on the blockchain.
- **Transactions Subclient**: Retrieves information about transactions.

Subclients:
-----------

.. toctree::
   :maxdepth: 2
   :caption: Subclients:


Addresses Subclient
===================

This subclient allows interactions with blockchain addresses, such as retrieving balances, transactions, etc.

.. automodule:: pulsechain.subclients.addresses
   :members:
   :undoc-members:
   :show-inheritance:

Blocks Subclient
================

This subclient retrieves information related to blocks in the blockchain.

.. automodule:: pulsechain.subclients.blocks
   :members:
   :undoc-members:
   :show-inheritance:

Search Subclient
================

The Search Subclient allows users to perform searches within the PulseChain blockchain.

.. automodule:: pulsechain.subclients.search
   :members:
   :undoc-members:
   :show-inheritance:

Smart Contracts Subclient
=========================

The Smart Contracts Subclient allows for interactions with smart contracts, including retrieving details, counters, and methods available.

Example:
--------

.. code-block:: python

    from pulsechain.subclients.smart_contracts import SmartContractsClient
    from pulsechain.req_handler import APIRequestHandler

    request_handler = APIRequestHandler(api_key="your_api_key")
    client = SmartContractsClient(request_handler)

    # Retrieve information about a specific contract
    contract_info = client.get_info("0x1234...abcd")

.. automodule:: pulsechain.subclients.smart_contracts
   :members:
   :undoc-members:
   :show-inheritance:

Stats Subclient
===============

The Stats Subclient provides various statistics about the PulseChain network.

.. automodule:: pulsechain.subclients.stats
   :members:
   :undoc-members:
   :show-inheritance:

Tokens Subclient
================

This subclient allows interactions related to tokens on the PulseChain network.

.. automodule:: pulsechain.subclients.tokens
   :members:
   :undoc-members:
   :show-inheritance:

Transactions Subclient
======================

The Transactions Subclient allows users to retrieve information about transactions.

.. automodule:: pulsechain.subclients.transactions
   :members:
   :undoc-members:
   :show-inheritance:

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

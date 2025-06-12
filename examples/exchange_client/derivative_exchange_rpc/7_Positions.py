import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    market_ids = [
        "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6",
        "0xd97d0da6f6c11710ef06315971250e4e9aed4b7d4cd02059c9477ec8cf243782",
    ]
    subaccount_id = "0xc6fe5d33615a1c52c08018c47e8bc53646a0e101000000000000000000000000"
    direction = "short"
    subaccount_total_positions = False
    skip = 4
    limit = 4
    pagination = PaginationOption(skip=skip, limit=limit)
    positions = await client.fetch_derivative_positions_v2(
        market_ids=market_ids,
        subaccount_id=subaccount_id,
        direction=direction,
        subaccount_total_positions=subaccount_total_positions,
        pagination=pagination,
    )
    print(json.dumps(positions, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

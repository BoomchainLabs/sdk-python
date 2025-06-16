import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    order_direction = "buy"
    market_id = "0x17ef48032cb24375ba7c2e39f384e56433bcab20cbee9a7357e4cba2eb00abe6"
    subacc_order_summary = await client.fetch_subaccount_order_summary(
        subaccount_id=subaccount, order_direction=order_direction, market_id=market_id
    )
    print(json.dumps(subacc_order_summary, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

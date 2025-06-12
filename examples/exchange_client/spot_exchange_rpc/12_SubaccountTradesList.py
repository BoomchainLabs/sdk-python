import asyncio
import json

from pyinjective.client.model.pagination import PaginationOption
from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    # select network: local, testnet, mainnet
    network = Network.testnet()
    client = IndexerClient(network)
    subaccount_id = "0xaf79152ac5df276d9a8e1e2e22822f9713474902000000000000000000000000"
    market_id = "0x0611780ba69656949525013d947713300f56c37b6175e02f26bffa495c3208fe"
    execution_type = "market"
    direction = "buy"
    skip = 2
    limit = 3
    pagination = PaginationOption(skip=skip, limit=limit)
    trades = await client.fetch_spot_subaccount_trades_list(
        subaccount_id=subaccount_id,
        market_id=market_id,
        execution_type=execution_type,
        direction=direction,
        pagination=pagination,
    )
    print(json.dumps(trades, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

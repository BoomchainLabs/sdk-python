import asyncio
import json

from pyinjective.core.network import Network
from pyinjective.indexer_client import IndexerClient


async def main() -> None:
    network = Network.testnet()
    client = IndexerClient(network)
    spot_order_hashes = [
        "0xce0d9b701f77cd6ddfda5dd3a4fe7b2d53ba83e5d6c054fb2e9e886200b7b7bb",
        "0x2e2245b5431638d76c6e0cc6268970418a1b1b7df60a8e94b8cf37eae6105542",
    ]
    derivative_order_hashes = [
        "0x82113f3998999bdc3892feaab2c4e53ba06c5fe887a2d5f9763397240f24da50",
        "0xbb1f036001378cecb5fff1cc69303919985b5bf058c32f37d5aaf9b804c07a06",
    ]
    orders = await client.fetch_order_states(
        spot_order_hashes=spot_order_hashes, derivative_order_hashes=derivative_order_hashes
    )
    print(json.dumps(orders, indent=2))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

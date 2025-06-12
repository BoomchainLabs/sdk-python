import asyncio
import os

import dotenv

from pyinjective import PrivateKey
from pyinjective.async_client_v2 import AsyncClient
from pyinjective.core.network import Network


async def main() -> None:
    dotenv.load_dotenv()
    configured_private_key = os.getenv("INJECTIVE_PRIVATE_KEY")

    # select network: local, testnet, mainnet
    network = Network.testnet()

    # initialize grpc client
    client = AsyncClient(network)

    # load account
    priv_key = PrivateKey.from_hex(configured_private_key)
    pub_key = priv_key.to_public_key()
    address = pub_key.to_address()
    await client.fetch_account(address.to_acc_bech32())

    is_opted_out = await client.fetch_is_opted_out_of_rewards(
        account=address.to_acc_bech32(),
    )
    print(is_opted_out)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())

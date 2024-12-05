import grpc
import pytest

from pyinjective.client.chain.grpc.chain_grpc_token_factory_api import ChainGrpcTokenFactoryApi
from pyinjective.core.network import DisabledCookieAssistant, Network
from pyinjective.proto.cosmos.base.v1beta1 import coin_pb2 as coin_pb
from pyinjective.proto.injective.tokenfactory.v1beta1 import (
    authorityMetadata_pb2 as token_factory_authority_metadata_pb,
    genesis_pb2 as token_factory_genesis_pb,
    params_pb2 as token_factory_params_pb,
    query_pb2 as token_factory_query_pb,
)
from tests.client.chain.grpc.configurable_token_factory_query_servicer import ConfigurableTokenFactoryQueryServicer


@pytest.fixture
def token_factory_query_servicer():
    return ConfigurableTokenFactoryQueryServicer()


class TestChainGrpcTokenFactoryApi:
    @pytest.mark.asyncio
    async def test_fetch_module_params(
        self,
        token_factory_query_servicer,
    ):
        coin = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        params = token_factory_params_pb.Params(
            denom_creation_fee=[coin],
        )
        token_factory_query_servicer.params_responses.append(token_factory_query_pb.QueryParamsResponse(params=params))

        api = self._api_instance(servicer=token_factory_query_servicer)

        module_params = await api.fetch_module_params()
        expected_params = {
            "params": {
                "denomCreationFee": [
                    {"denom": coin.denom, "amount": coin.amount},
                ],
            }
        }

        assert module_params == expected_params

    @pytest.mark.asyncio
    async def test_fetch_denom_authority_metadata(
        self,
        token_factory_query_servicer,
    ):
        authority_metadata = token_factory_authority_metadata_pb.DenomAuthorityMetadata(
            admin="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7",
            admin_burn_allowed=True,
        )
        token_factory_query_servicer.denom_authority_metadata_responses.append(
            token_factory_query_pb.QueryDenomAuthorityMetadataResponse(
                authority_metadata=authority_metadata,
            )
        )

        api = self._api_instance(servicer=token_factory_query_servicer)

        metadata = await api.fetch_denom_authority_metadata(
            creator=authority_metadata.admin,
            sub_denom="inj",
        )
        expected_metadata = {
            "authorityMetadata": {
                "admin": authority_metadata.admin,
                "adminBurnAllowed": authority_metadata.admin_burn_allowed,
            },
        }

        assert metadata == expected_metadata

    @pytest.mark.asyncio
    async def test_fetch_denoms_from_creator(
        self,
        token_factory_query_servicer,
    ):
        denom = "factory/inj17vytdwqczqz72j65saukplrktd4gyfme5agf6c/weth"
        token_factory_query_servicer.denoms_from_creator_responses.append(
            token_factory_query_pb.QueryDenomsFromCreatorResponse(denoms=[denom])
        )

        api = self._api_instance(servicer=token_factory_query_servicer)

        denoms = await api.fetch_denoms_from_creator(creator="inj1ady3s7whq30l4fx8sj3x6muv5mx4dfdlcpv8n7")
        expected_denoms = {"denoms": [denom]}

        assert denoms == expected_denoms

    @pytest.mark.asyncio
    async def test_fetch_tokenfactory_module_state(
        self,
        token_factory_query_servicer,
    ):
        coin = coin_pb.Coin(denom="inj", amount="988987297011197594664")
        params = token_factory_params_pb.Params(
            denom_creation_fee=[coin],
        )
        authority_metadata = token_factory_authority_metadata_pb.DenomAuthorityMetadata(
            admin="inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0",
            admin_burn_allowed=True,
        )
        genesis_denom = token_factory_genesis_pb.GenesisDenom(
            denom="factory/inj1apmvarl2xyv6kecx2ukkeymddw3we4zkygjyc0/ninja",
            authority_metadata=authority_metadata,
            name="Dog Wif Nunchucks",
            symbol="NINJA",
            decimals=6,
        )
        state = token_factory_genesis_pb.GenesisState(
            params=params,
            factory_denoms=[genesis_denom],
        )
        token_factory_query_servicer.tokenfactory_module_state_responses.append(
            token_factory_query_pb.QueryModuleStateResponse(state=state)
        )

        api = self._api_instance(servicer=token_factory_query_servicer)

        state = await api.fetch_tokenfactory_module_state()
        expected_state = {
            "state": {
                "params": {
                    "denomCreationFee": [
                        {"denom": coin.denom, "amount": coin.amount},
                    ],
                },
                "factoryDenoms": [
                    {
                        "denom": genesis_denom.denom,
                        "authorityMetadata": {
                            "admin": authority_metadata.admin,
                            "adminBurnAllowed": authority_metadata.admin_burn_allowed,
                        },
                        "name": genesis_denom.name,
                        "symbol": genesis_denom.symbol,
                        "decimals": genesis_denom.decimals,
                    }
                ],
            }
        }

        assert state == expected_state

    def _api_instance(self, servicer):
        network = Network.devnet()
        channel = grpc.aio.insecure_channel(network.grpc_endpoint)
        cookie_assistant = DisabledCookieAssistant()

        api = ChainGrpcTokenFactoryApi(channel=channel, cookie_assistant=cookie_assistant)
        api._query_stub = servicer

        return api

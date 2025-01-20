from warnings import catch_warnings

import grpc
import pytest

from pyinjective.async_client import AsyncClient
from pyinjective.core.network import Network
from pyinjective.proto.cosmos.authz.v1beta1 import query_pb2 as authz_query
from pyinjective.proto.cosmos.bank.v1beta1 import query_pb2 as bank_query_pb
from pyinjective.proto.cosmos.base.tendermint.v1beta1 import query_pb2 as tendermint_query
from pyinjective.proto.cosmos.tx.v1beta1 import service_pb2 as tx_service
from pyinjective.proto.exchange import (
    injective_accounts_rpc_pb2 as exchange_accounts_pb,
    injective_auction_rpc_pb2 as exchange_auction_pb,
    injective_derivative_exchange_rpc_pb2 as exchange_derivative_pb,
    injective_explorer_rpc_pb2 as exchange_explorer_pb,
    injective_insurance_rpc_pb2 as exchange_insurance_pb,
    injective_meta_rpc_pb2 as exchange_meta_pb,
    injective_oracle_rpc_pb2 as exchange_oracle_pb,
    injective_portfolio_rpc_pb2 as exchange_portfolio_pb,
    injective_spot_exchange_rpc_pb2 as exchange_spot_pb,
)
from pyinjective.proto.injective.stream.v1beta1 import query_pb2 as chain_stream_pb
from pyinjective.proto.injective.types.v1beta1 import account_pb2 as account_pb
from tests.client.chain.grpc.configurable_auth_query_servicer import ConfigurableAuthQueryServicer
from tests.client.chain.grpc.configurable_authz_query_servicer import ConfigurableAuthZQueryServicer
from tests.client.chain.grpc.configurable_bank_query_servicer import ConfigurableBankQueryServicer
from tests.client.chain.stream_grpc.configurable_chain_stream_query_servicer import ConfigurableChainStreamQueryServicer
from tests.client.indexer.configurable_account_query_servicer import ConfigurableAccountQueryServicer
from tests.client.indexer.configurable_auction_query_servicer import ConfigurableAuctionQueryServicer
from tests.client.indexer.configurable_derivative_query_servicer import ConfigurableDerivativeQueryServicer
from tests.client.indexer.configurable_explorer_query_servicer import ConfigurableExplorerQueryServicer
from tests.client.indexer.configurable_insurance_query_servicer import ConfigurableInsuranceQueryServicer
from tests.client.indexer.configurable_meta_query_servicer import ConfigurableMetaQueryServicer
from tests.client.indexer.configurable_oracle_query_servicer import ConfigurableOracleQueryServicer
from tests.client.indexer.configurable_portfolio_query_servicer import ConfigurablePortfolioQueryServicer
from tests.client.indexer.configurable_spot_query_servicer import ConfigurableSpotQueryServicer
from tests.core.tendermint.grpc.configurable_tendermint_query_servicer import ConfigurableTendermintQueryServicer
from tests.core.tx.grpc.configurable_tx_query_servicer import ConfigurableTxQueryServicer


@pytest.fixture
def account_servicer():
    return ConfigurableAccountQueryServicer()


@pytest.fixture
def auction_servicer():
    return ConfigurableAuctionQueryServicer()


@pytest.fixture
def auth_servicer():
    return ConfigurableAuthQueryServicer()


@pytest.fixture
def authz_servicer():
    return ConfigurableAuthZQueryServicer()


@pytest.fixture
def bank_servicer():
    return ConfigurableBankQueryServicer()


@pytest.fixture
def chain_stream_servicer():
    return ConfigurableChainStreamQueryServicer()


@pytest.fixture
def derivative_servicer():
    return ConfigurableDerivativeQueryServicer()


@pytest.fixture
def explorer_servicer():
    return ConfigurableExplorerQueryServicer()


@pytest.fixture
def insurance_servicer():
    return ConfigurableInsuranceQueryServicer()


@pytest.fixture
def meta_servicer():
    return ConfigurableMetaQueryServicer()


@pytest.fixture
def oracle_servicer():
    return ConfigurableOracleQueryServicer()


@pytest.fixture
def portfolio_servicer():
    return ConfigurablePortfolioQueryServicer()


@pytest.fixture
def spot_servicer():
    return ConfigurableSpotQueryServicer()


@pytest.fixture
def tx_servicer():
    return ConfigurableTxQueryServicer()


@pytest.fixture
def tendermint_servicer():
    return ConfigurableTendermintQueryServicer()


class TestAsyncClientDeprecationWarnings:
    def test_insecure_parameter_deprecation_warning(
        self,
        auth_servicer,
    ):
        with catch_warnings(record=True) as all_warnings:
            AsyncClient(
                network=Network.local(),
                insecure=False,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "insecure parameter in AsyncClient is no longer used and will be deprecated"
        )

    @pytest.mark.asyncio
    async def test_get_account_deprecation_warning(
        self,
        auth_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuth = auth_servicer
        auth_servicer.account_responses.append(account_pb.EthAccount())

        with catch_warnings(record=True) as all_warnings:
            await client.get_account(address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_account instead"

    @pytest.mark.asyncio
    async def test_get_bank_balance_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubBank = bank_servicer
        bank_servicer.balance_responses.append(bank_query_pb.QueryBalanceResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balance(address="", denom="inj")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_bank_balance instead"

    @pytest.mark.asyncio
    async def test_get_bank_balances_deprecation_warning(
        self,
        bank_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubBank = bank_servicer
        bank_servicer.balances_responses.append(bank_query_pb.QueryAllBalancesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_bank_balances(address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_bank_balances instead"

    @pytest.mark.asyncio
    async def test_get_order_states_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.order_states_responses.append(exchange_accounts_pb.OrderStatesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_order_states(spot_order_hashes=["hash1"], derivative_order_hashes=["hash2"])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_order_states instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccounts_list_responses.append(exchange_accounts_pb.SubaccountsListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_list(account_address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_subaccounts_list instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_balances_list_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balances_list_responses.append(
            exchange_accounts_pb.SubaccountBalancesListResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balances_list(subaccount_id="", denoms=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_subaccount_balances_list instead"
        )

    @pytest.mark.asyncio
    async def test_get_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_balance_responses.append(exchange_accounts_pb.SubaccountBalanceEndpointResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_balance(subaccount_id="", denom="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_balance instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_history_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_history_responses.append(exchange_accounts_pb.SubaccountHistoryResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_history(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_subaccount_history instead"

    @pytest.mark.asyncio
    async def test_get_subaccount_order_summary_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.subaccount_order_summary_responses.append(
            exchange_accounts_pb.SubaccountOrderSummaryResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_subaccount_order_summary(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_subaccount_order_summary instead"
        )

    @pytest.mark.asyncio
    async def test_get_portfolio_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.portfolio_responses.append(exchange_accounts_pb.PortfolioResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_portfolio(account_address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_portfolio instead"

    @pytest.mark.asyncio
    async def test_get_rewards_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.rewards_responses.append(exchange_accounts_pb.RewardsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_rewards(account_address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_rewards instead"

    @pytest.mark.asyncio
    async def test_stream_subaccount_balance_deprecation_warning(
        self,
        account_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        account_servicer.stream_subaccount_balance_responses.append(
            exchange_accounts_pb.StreamSubaccountBalanceResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.stream_subaccount_balance(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_subaccount_balance_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_grants_deprecation_warning(
        self,
        authz_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuthz = authz_servicer
        authz_servicer.grants_responses.append(authz_query.QueryGrantsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_grants(granter="granter", grantee="grantee")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_grants instead"

    @pytest.mark.asyncio
    async def test_simulate_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.simulate_responses.append(tx_service.SimulateResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.simulate_tx(tx_byte="".encode())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use simulate instead"

    @pytest.mark.asyncio
    async def test_get_tx_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.get_tx_responses.append(tx_service.GetTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_tx(tx_hash="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_tx instead"

    @pytest.mark.asyncio
    async def test_send_tx_sync_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_sync_mode(tx_byte="".encode())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use broadcast_tx_sync_mode instead"

    @pytest.mark.asyncio
    async def test_send_tx_async_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_async_mode(tx_byte="".encode())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use broadcast_tx_async_mode instead"

    @pytest.mark.asyncio
    async def test_send_tx_block_mode_deprecation_warning(
        self,
        tx_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubTx = tx_servicer
        tx_servicer.broadcast_responses.append(tx_service.BroadcastTxResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.send_tx_block_mode(tx_byte="".encode())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. BLOCK broadcast mode should not be used"
        )

    @pytest.mark.asyncio
    async def test_ping_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.ping_responses.append(exchange_meta_pb.PingResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.ping()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_ping instead"

    @pytest.mark.asyncio
    async def test_version_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.version_responses.append(exchange_meta_pb.VersionResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.version()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_version instead"

    @pytest.mark.asyncio
    async def test_info_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubMeta = meta_servicer
        meta_servicer.info_responses.append(exchange_meta_pb.InfoResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.info()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_info instead"

    @pytest.mark.asyncio
    async def test_stream_keepalive_deprecation_warning(
        self,
        meta_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExchangeAccount = account_servicer
        meta_servicer.stream_keepalive_responses.append(exchange_meta_pb.StreamKeepaliveResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_keepalive()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_keepalive instead"

    @pytest.mark.asyncio
    async def test_get_oracle_list_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.oracle_list_responses.append(exchange_oracle_pb.OracleListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_oracle_list()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_oracle_list instead"

    @pytest.mark.asyncio
    async def test_get_oracle_prices_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.price_responses.append(exchange_oracle_pb.PriceResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_oracle_prices(
                base_symbol="Gold",
                quote_symbol="USDT",
                oracle_type="pricefeed",
                oracle_scale_factor=6,
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_oracle_price instead"

    @pytest.mark.asyncio
    async def test_stream_oracle_prices_deprecation_warning(
        self,
        oracle_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubOracle = oracle_servicer
        oracle_servicer.stream_prices_responses.append(exchange_oracle_pb.StreamPricesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_oracle_prices(
                base_symbol="Gold",
                quote_symbol="USDT",
                oracle_type="pricefeed",
            )

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_oracle_prices_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_insurance_funds_deprecation_warning(
        self,
        insurance_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubInsurance = insurance_servicer
        insurance_servicer.funds_responses.append(exchange_insurance_pb.FundsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_insurance_funds()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_insurance_funds instead"

    @pytest.mark.asyncio
    async def test_get_redemptions_deprecation_warning(
        self,
        insurance_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubInsurance = insurance_servicer
        insurance_servicer.redemptions_responses.append(exchange_insurance_pb.RedemptionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_redemptions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_redemptions instead"

    @pytest.mark.asyncio
    async def test_get_auction_deprecation_warning(
        self,
        auction_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuction = auction_servicer
        auction_servicer.auction_endpoint_responses.append(exchange_auction_pb.AuctionEndpointResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_auction(bid_round=1)

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_auction instead"

    @pytest.mark.asyncio
    async def test_get_auctions_deprecation_warning(
        self,
        auction_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuction = auction_servicer
        auction_servicer.auctions_responses.append(exchange_auction_pb.AuctionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_auctions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_auctions instead"

    @pytest.mark.asyncio
    async def test_stream_bids_deprecation_warning(
        self,
        auction_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubAuction = auction_servicer
        auction_servicer.stream_bids_responses.append(exchange_auction_pb.StreamBidsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_bids()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_bids_updates instead"

    @pytest.mark.asyncio
    async def test_get_spot_markets_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.markets_responses.append(exchange_spot_pb.MarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_markets instead"

    @pytest.mark.asyncio
    async def test_get_spot_market_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.market_responses.append(exchange_spot_pb.MarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_market(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_market instead"

    @pytest.mark.asyncio
    async def test_get_spot_orderbookV2_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.orderbook_v2_responses.append(exchange_spot_pb.OrderbookV2Response())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_orderbookV2(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_orderbook_v2 instead"

    @pytest.mark.asyncio
    async def test_get_spot_orderbooksV2_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.orderbooks_v2_responses.append(exchange_spot_pb.OrderbooksV2Response())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_orderbooksV2(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_orderbooks_v2 instead"

    @pytest.mark.asyncio
    async def test_get_spot_orders_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.orders_responses.append(exchange_spot_pb.OrdersResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_orders instead"

    @pytest.mark.asyncio
    async def test_get_spot_trades_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.trades_responses.append(exchange_spot_pb.TradesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_trades()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_trades instead"

    @pytest.mark.asyncio
    async def test_get_spot_subaccount_orders_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.subaccount_orders_list_responses.append(exchange_spot_pb.SubaccountOrdersListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_subaccount_orders(subaccount_id="", market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_spot_subaccount_orders_list instead"
        )

    @pytest.mark.asyncio
    async def test_get_spot_subaccount_trades_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.subaccount_trades_list_responses.append(exchange_spot_pb.SubaccountTradesListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_spot_subaccount_trades(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_spot_subaccount_trades_list instead"
        )

    @pytest.mark.asyncio
    async def test_get_historical_spot_orders_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.orders_history_responses.append(exchange_spot_pb.SubaccountTradesListResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_historical_spot_orders()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_spot_orders_history instead"
        )

    @pytest.mark.asyncio
    async def test_stream_spot_markets_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_markets_responses.append(exchange_spot_pb.StreamMarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_spot_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_spot_markets_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_spot_orderbook_snapshot_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_orderbook_v2_responses.append(exchange_spot_pb.StreamOrderbookV2Response())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_spot_orderbook_snapshot(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_spot_orderbook_snapshots instead"
        )

    @pytest.mark.asyncio
    async def test_stream_spot_orderbook_update_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_orderbook_update_responses.append(exchange_spot_pb.StreamOrderbookUpdateRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_spot_orderbook_update(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_spot_orderbook_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_spot_orders_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_orders_responses.append(exchange_spot_pb.StreamOrdersRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_spot_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_spot_orders_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_spot_trades_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_orders_responses.append(exchange_spot_pb.StreamTradesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_spot_trades()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_spot_trades_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_historical_spot_orders_deprecation_warning(
        self,
        spot_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        spot_servicer.stream_orders_history_responses.append(exchange_spot_pb.StreamOrdersHistoryRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_historical_spot_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_spot_orders_history_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_markets_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.markets_responses.append(exchange_derivative_pb.MarketsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_derivative_markets instead"

    @pytest.mark.asyncio
    async def test_get_derivative_market_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.market_responses.append(exchange_derivative_pb.MarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_market(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_derivative_market instead"

    @pytest.mark.asyncio
    async def test_get_binary_options_markets_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.binary_options_markets_responses.append(
            exchange_derivative_pb.BinaryOptionsMarketsResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_binary_options_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_binary_options_markets instead"
        )

    @pytest.mark.asyncio
    async def test_get_binary_options_market_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.binary_options_market_responses.append(exchange_derivative_pb.BinaryOptionsMarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_binary_options_market(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_binary_options_market instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_orderbook_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.orderbook_v2_responses.append(exchange_derivative_pb.OrderbookV2Request())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_orderbook(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_orderbook_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_orderbooksV2_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.orderbooks_v2_responses.append(exchange_derivative_pb.OrderbooksV2Request())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_orderbooksV2(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_orderbooks_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_orders_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.orders_responses.append(exchange_derivative_pb.OrdersResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_derivative_orders instead"

    @pytest.mark.asyncio
    async def test_get_derivative_positions_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.positions_responses.append(exchange_derivative_pb.PositionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_positions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_positions_v2 instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_liquidable_positions_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.liquidable_positions_responses.append(exchange_derivative_pb.LiquidablePositionsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_liquidable_positions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_liquidable_positions instead"
        )

    @pytest.mark.asyncio
    async def test_get_funding_payments_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.funding_payments_responses.append(exchange_derivative_pb.FundingPaymentsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_funding_payments(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_funding_payments instead"

    @pytest.mark.asyncio
    async def test_get_funding_rates_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.funding_rates_responses.append(exchange_derivative_pb.FundingRatesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_funding_rates(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_funding_rates instead"

    @pytest.mark.asyncio
    async def test_get_derivative_trades_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.trades_responses.append(exchange_derivative_pb.TradesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_trades()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_derivative_trades instead"

    @pytest.mark.asyncio
    async def test_get_derivative_subaccount_orders_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.subaccount_orders_list_responses.append(
            exchange_derivative_pb.SubaccountOrdersListResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_subaccount_orders(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_subaccount_orders instead"
        )

    @pytest.mark.asyncio
    async def test_get_derivative_subaccount_trades_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.subaccount_trades_list_responses.append(
            exchange_derivative_pb.SubaccountTradesListResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.get_derivative_subaccount_trades(subaccount_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_subaccount_trades instead"
        )

    @pytest.mark.asyncio
    async def test_get_historical_derivative_orders_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.orders_history_responses.append(exchange_derivative_pb.OrdersHistoryResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_historical_derivative_orders()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_derivative_orders_history instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_markets_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.stream_market_responses.append(exchange_derivative_pb.StreamMarketResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_markets()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_market_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_orderbook_snapshot_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = spot_servicer
        derivative_servicer.stream_orderbook_v2_responses.append(exchange_derivative_pb.StreamOrderbookV2Response())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_orderbook_snapshot(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_orderbook_snapshots instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_orderbook_update_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.stream_orderbook_update_responses.append(
            exchange_derivative_pb.StreamOrderbookUpdateRequest()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_orderbook_update(market_ids=[])

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_orderbook_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_positions_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubDerivativeExchange = derivative_servicer
        derivative_servicer.stream_positions_responses.append(exchange_derivative_pb.StreamPositionsRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_positions()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_positions_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_orders_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = derivative_servicer
        derivative_servicer.stream_orders_responses.append(exchange_derivative_pb.StreamOrdersRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_orders_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_derivative_trades_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = derivative_servicer
        derivative_servicer.stream_orders_responses.append(exchange_derivative_pb.StreamTradesResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_derivative_trades()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_trades_updates instead"
        )

    @pytest.mark.asyncio
    async def test_stream_historical_derivative_orders_deprecation_warning(
        self,
        derivative_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubSpotExchange = derivative_servicer
        derivative_servicer.stream_orders_history_responses.append(exchange_spot_pb.StreamOrdersHistoryRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_historical_derivative_orders(market_id="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_derivative_orders_history_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_account_portfolio_deprecation_warning(
        self,
        portfolio_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubPortfolio = portfolio_servicer
        portfolio_servicer.account_portfolio_responses.append(exchange_portfolio_pb.AccountPortfolioResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_account_portfolio(account_address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use fetch_account_portfolio_balances instead"
        )

    @pytest.mark.asyncio
    async def test_stream_account_portfolio_deprecation_warning(
        self,
        portfolio_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubPortfolio = portfolio_servicer
        portfolio_servicer.stream_account_portfolio_responses.append(
            exchange_portfolio_pb.StreamAccountPortfolioResponse()
        )

        with catch_warnings(record=True) as all_warnings:
            await client.stream_account_portfolio(account_address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "This method is deprecated. Use listen_account_portfolio_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_account_txs_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.account_txs_responses.append(exchange_explorer_pb.GetAccountTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_account_txs(address="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_account_txs instead"

    @pytest.mark.asyncio
    async def test_get_blocks_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.blocks_responses.append(exchange_explorer_pb.GetBlocksResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_blocks()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_blocks instead"

    @pytest.mark.asyncio
    async def test_get_block_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.block_responses.append(exchange_explorer_pb.GetBlockResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_block(block_height="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_block instead"

    @pytest.mark.asyncio
    async def test_get_txs_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.txs_responses.append(exchange_explorer_pb.GetTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_txs()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_txs instead"

    @pytest.mark.asyncio
    async def test_get_tx_by_hash_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.tx_by_tx_hash_responses.append(exchange_explorer_pb.GetTxByTxHashResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_tx_by_hash(tx_hash="")

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_tx_by_tx_hash instead"

    @pytest.mark.asyncio
    async def test_get_peggy_deposits_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.peggy_deposit_txs_responses.append(exchange_explorer_pb.GetPeggyDepositTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_peggy_deposits()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_peggy_deposit_txs instead"

    @pytest.mark.asyncio
    async def test_get_peggy_withdrawals_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.peggy_withdrawal_txs_responses.append(exchange_explorer_pb.GetPeggyWithdrawalTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_peggy_withdrawals()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_peggy_withdrawal_txs instead"
        )

    @pytest.mark.asyncio
    async def test_get_ibc_transfers_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubExplorer = explorer_servicer
        explorer_servicer.ibc_transfer_txs_responses.append(exchange_explorer_pb.GetIBCTransferTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_ibc_transfers()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_ibc_transfer_txs instead"

    @pytest.mark.asyncio
    async def test_stream_txs_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubPortfolio = explorer_servicer
        explorer_servicer.stream_txs_responses.append(exchange_explorer_pb.StreamTxsResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_txs()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_txs_updates instead"

    @pytest.mark.asyncio
    async def test_stream_blocks_deprecation_warning(
        self,
        explorer_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubPortfolio = explorer_servicer
        explorer_servicer.stream_blocks_responses.append(exchange_explorer_pb.StreamBlocksResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.stream_blocks()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_blocks_updates instead"

    @pytest.mark.asyncio
    async def test_chain_stream_deprecation_warning(
        self,
        chain_stream_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.chain_stream_stub = chain_stream_servicer
        chain_stream_servicer.stream_responses.append(chain_stream_pb.StreamRequest())

        with catch_warnings(record=True) as all_warnings:
            await client.chain_stream()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message) == "This method is deprecated. Use listen_chain_stream_updates instead"
        )

    @pytest.mark.asyncio
    async def test_get_latest_block_deprecation_warning(
        self,
        tendermint_servicer,
    ):
        client = AsyncClient(
            network=Network.local(),
        )
        client.stubCosmosTendermint = tendermint_servicer
        tendermint_servicer.get_latest_block_responses.append(tendermint_query.GetLatestBlockResponse())

        with catch_warnings(record=True) as all_warnings:
            await client.get_latest_block()

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert str(deprecation_warnings[0].message) == "This method is deprecated. Use fetch_latest_block instead"

    def test_credentials_parameter_deprecation_warning(
        self,
        auth_servicer,
    ):
        with catch_warnings(record=True) as all_warnings:
            AsyncClient(network=Network.local(), credentials=grpc.ssl_channel_credentials())

        deprecation_warnings = [warning for warning in all_warnings if issubclass(warning.category, DeprecationWarning)]
        assert len(deprecation_warnings) == 1
        assert (
            str(deprecation_warnings[0].message)
            == "credentials parameter in AsyncClient is no longer used and will be deprecated"
        )

    @pytest.mark.asyncio
    async def test_listen_derivative_positions_updates_deprecation(self):
        # Create a mock AsyncClient (you might need to adjust this based on your actual implementation)
        client = AsyncClient(network=Network.local())

        # Expect a DeprecationWarning to be raised
        with catch_warnings(record=True) as captured_warnings:
            # Mock callback and other required parameters
            async def mock_callback(update):
                pass

            # Call the deprecated method
            await client.listen_derivative_positions_updates(
                callback=mock_callback, market_ids=["test_market"], subaccount_ids=["test_subaccount"]
            )

            # Assert that a DeprecationWarning was raised
            assert len(captured_warnings) > 0
            assert issubclass(captured_warnings[-1].category, DeprecationWarning)
            assert "deprecated. Use listen_derivative_positions_v2_updates" in str(captured_warnings[-1].message)

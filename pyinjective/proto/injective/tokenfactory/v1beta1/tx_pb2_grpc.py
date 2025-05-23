# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from pyinjective.proto.injective.tokenfactory.v1beta1 import tx_pb2 as injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the tokenfactory module's gRPC message service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDenom = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/CreateDenom',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenom.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenomResponse.FromString,
                _registered_method=True)
        self.Mint = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/Mint',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMint.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMintResponse.FromString,
                _registered_method=True)
        self.Burn = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/Burn',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurn.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurnResponse.FromString,
                _registered_method=True)
        self.ChangeAdmin = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/ChangeAdmin',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdmin.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdminResponse.FromString,
                _registered_method=True)
        self.SetDenomMetadata = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/SetDenomMetadata',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadata.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadataResponse.FromString,
                _registered_method=True)
        self.UpdateParams = channel.unary_unary(
                '/injective.tokenfactory.v1beta1.Msg/UpdateParams',
                request_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
                response_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
                _registered_method=True)


class MsgServicer(object):
    """Msg defines the tokenfactory module's gRPC message service.
    """

    def CreateDenom(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Mint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Burn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeAdmin(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetDenomMetadata(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateDenom': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDenom,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenom.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenomResponse.SerializeToString,
            ),
            'Mint': grpc.unary_unary_rpc_method_handler(
                    servicer.Mint,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMint.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMintResponse.SerializeToString,
            ),
            'Burn': grpc.unary_unary_rpc_method_handler(
                    servicer.Burn,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurn.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurnResponse.SerializeToString,
            ),
            'ChangeAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeAdmin,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdmin.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdminResponse.SerializeToString,
            ),
            'SetDenomMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.SetDenomMetadata,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadata.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadataResponse.SerializeToString,
            ),
            'UpdateParams': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateParams,
                    request_deserializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.FromString,
                    response_serializer=injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'injective.tokenfactory.v1beta1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('injective.tokenfactory.v1beta1.Msg', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the tokenfactory module's gRPC message service.
    """

    @staticmethod
    def CreateDenom(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/CreateDenom',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenom.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgCreateDenomResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Mint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/Mint',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMint.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgMintResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Burn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/Burn',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurn.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgBurnResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChangeAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/ChangeAdmin',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdmin.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgChangeAdminResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetDenomMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/SetDenomMetadata',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadata.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgSetDenomMetadataResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateParams(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/injective.tokenfactory.v1beta1.Msg/UpdateParams',
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParams.SerializeToString,
            injective_dot_tokenfactory_dot_v1beta1_dot_tx__pb2.MsgUpdateParamsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

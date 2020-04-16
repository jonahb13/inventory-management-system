# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import InventorySystem_pb2 as InventorySystem__pb2


class InventorySystemStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.addNewProduct = channel.unary_unary(
        '/ecommerce.InventorySystem/addNewProduct',
        request_serializer=InventorySystem__pb2.Product.SerializeToString,
        response_deserializer=InventorySystem__pb2.ProductID.FromString,
        )
    self.getProduct = channel.unary_unary(
        '/ecommerce.InventorySystem/getProduct',
        request_serializer=InventorySystem__pb2.ProductQuery.SerializeToString,
        response_deserializer=InventorySystem__pb2.Product.FromString,
        )
    self.updateProduct = channel.unary_unary(
        '/ecommerce.InventorySystem/updateProduct',
        request_serializer=InventorySystem__pb2.Product.SerializeToString,
        response_deserializer=InventorySystem__pb2.UpdateResult.FromString,
        )
    self.getManufacturerProducts = channel.unary_stream(
        '/ecommerce.InventorySystem/getManufacturerProducts',
        request_serializer=InventorySystem__pb2.Manufacturer.SerializeToString,
        response_deserializer=InventorySystem__pb2.Product.FromString,
        )
    self.getAllProducts = channel.unary_stream(
        '/ecommerce.InventorySystem/getAllProducts',
        request_serializer=InventorySystem__pb2.Empty.SerializeToString,
        response_deserializer=InventorySystem__pb2.Product.FromString,
        )
    self.getInStockProducts = channel.unary_stream(
        '/ecommerce.InventorySystem/getInStockProducts',
        request_serializer=InventorySystem__pb2.Empty.SerializeToString,
        response_deserializer=InventorySystem__pb2.ProductCount.FromString,
        )
    self.createOrder = channel.unary_unary(
        '/ecommerce.InventorySystem/createOrder',
        request_serializer=InventorySystem__pb2.Order.SerializeToString,
        response_deserializer=InventorySystem__pb2.OrderID.FromString,
        )
    self.getOrder = channel.unary_unary(
        '/ecommerce.InventorySystem/getOrder',
        request_serializer=InventorySystem__pb2.OrderID.SerializeToString,
        response_deserializer=InventorySystem__pb2.Order.FromString,
        )
    self.amendOrder = channel.unary_unary(
        '/ecommerce.InventorySystem/amendOrder',
        request_serializer=InventorySystem__pb2.UpdateOrder.SerializeToString,
        response_deserializer=InventorySystem__pb2.UpdateResult.FromString,
        )
    self.getUnshippedAndOrUnpaidOrders = channel.unary_stream(
        '/ecommerce.InventorySystem/getUnshippedAndOrUnpaidOrders',
        request_serializer=InventorySystem__pb2.UnshippedAndOrUnpaidQuery.SerializeToString,
        response_deserializer=InventorySystem__pb2.Order.FromString,
        )


class InventorySystemServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def addNewProduct(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getProduct(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def updateProduct(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getManufacturerProducts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getAllProducts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInStockProducts(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def amendOrder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getUnshippedAndOrUnpaidOrders(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InventorySystemServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'addNewProduct': grpc.unary_unary_rpc_method_handler(
          servicer.addNewProduct,
          request_deserializer=InventorySystem__pb2.Product.FromString,
          response_serializer=InventorySystem__pb2.ProductID.SerializeToString,
      ),
      'getProduct': grpc.unary_unary_rpc_method_handler(
          servicer.getProduct,
          request_deserializer=InventorySystem__pb2.ProductQuery.FromString,
          response_serializer=InventorySystem__pb2.Product.SerializeToString,
      ),
      'updateProduct': grpc.unary_unary_rpc_method_handler(
          servicer.updateProduct,
          request_deserializer=InventorySystem__pb2.Product.FromString,
          response_serializer=InventorySystem__pb2.UpdateResult.SerializeToString,
      ),
      'getManufacturerProducts': grpc.unary_stream_rpc_method_handler(
          servicer.getManufacturerProducts,
          request_deserializer=InventorySystem__pb2.Manufacturer.FromString,
          response_serializer=InventorySystem__pb2.Product.SerializeToString,
      ),
      'getAllProducts': grpc.unary_stream_rpc_method_handler(
          servicer.getAllProducts,
          request_deserializer=InventorySystem__pb2.Empty.FromString,
          response_serializer=InventorySystem__pb2.Product.SerializeToString,
      ),
      'getInStockProducts': grpc.unary_stream_rpc_method_handler(
          servicer.getInStockProducts,
          request_deserializer=InventorySystem__pb2.Empty.FromString,
          response_serializer=InventorySystem__pb2.ProductCount.SerializeToString,
      ),
      'createOrder': grpc.unary_unary_rpc_method_handler(
          servicer.createOrder,
          request_deserializer=InventorySystem__pb2.Order.FromString,
          response_serializer=InventorySystem__pb2.OrderID.SerializeToString,
      ),
      'getOrder': grpc.unary_unary_rpc_method_handler(
          servicer.getOrder,
          request_deserializer=InventorySystem__pb2.OrderID.FromString,
          response_serializer=InventorySystem__pb2.Order.SerializeToString,
      ),
      'amendOrder': grpc.unary_unary_rpc_method_handler(
          servicer.amendOrder,
          request_deserializer=InventorySystem__pb2.UpdateOrder.FromString,
          response_serializer=InventorySystem__pb2.UpdateResult.SerializeToString,
      ),
      'getUnshippedAndOrUnpaidOrders': grpc.unary_stream_rpc_method_handler(
          servicer.getUnshippedAndOrUnpaidOrders,
          request_deserializer=InventorySystem__pb2.UnshippedAndOrUnpaidQuery.FromString,
          response_serializer=InventorySystem__pb2.Order.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ecommerce.InventorySystem', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
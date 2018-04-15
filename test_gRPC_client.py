import grpc
import test_gRPC_pb2
import test_gRPC_pb2_grpc



def run():
	channel = grpc.insecure_channel('localhost:50051')
	stub = test_gRPC_pb2_grpc.test_gRPCStub(channel)
	# the_request = test_gRPC_pb2.An_unexciting_request(request_name_1 = "first request")
	# reponse = stub.GetFeature(the_request)
	response = stub.GetFeature(test_gRPC_pb2.An_unexciting_request(request_name_1 = "this is the request parameter 1 "))
	print("test_gRPC client received: " + response.exciting_response_1)

if __name__ == '__main__':
    run()

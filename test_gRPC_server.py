import grpc
import test_gRPC_pb2
import test_gRPC_pb2_grpc
from concurrent import futures
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
class test_gRPC_server(test_gRPC_pb2_grpc.test_gRPCServicer):
	def GetFeature(self, request, context):
		print("%s" %request.request_name_1)
		return test_gRPC_pb2.An_exciting_response(exciting_response_1 = "this is a response")

def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
	test_gRPC_pb2_grpc.add_test_gRPCServicer_to_server(test_gRPC_server(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	try:
		while True:
			time.sleep(_ONE_DAY_IN_SECONDS)
	except KeyboardInterrupt:
		server.stop(0)

def stop(a_server):
	a_server.stop(0)

    # try:
    # 	while True:
    # 		time.sleep(_ONE_DAY_IN_SECONDS)
    # except KeyboardInterrupt:
    # 	server.stop(0)

if __name__ == '__main__':
	serve()
	# try:
	# 	while True:
	# 		a_server = serve()
	# except KeyboardInterrupt:
	# 	stop(a_server)

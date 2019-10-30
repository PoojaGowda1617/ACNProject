import time, socket,threading,sys


print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

server_port=[6000,6001] #server port

def fog_node_connect(server_port):
	ip = "0.0.0.0"
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	start = time.time()
	client_port = 1234 #own port
	conn_establ = False
	s.bind((ip,client_port))
	while True:
		try:
			s.settimeout(2)
			s.listen(1)
			conn, addr = s.accept()
			if conn:
				print("Connection established with client with port : {}".format(client_port))
				conn_establ = True
				break
		except:
			print("Connection not established")
			s.shutdown(1)
			s.close()
			break
	if not conn_establ:	
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('127.0.0.1', server_port))
	
		print( "(", ip, ")\n")
		name = input(str("\nEnter your name: "))
	
		print("\nTrying to connect to ", "(", server_port, ")\n")
		time.sleep(1)
	
		print("Connected...\n")
	
		while 1:
			message = input(str("Please enter your message: "))
			message = message.encode()
			s.send(message)
			print("Sent")
			print("")
			message = s.recv(1024)
			message = message.decode()
			print(name, ":" ,message)
			print("")



thread1 = threading.Thread(target=fog_node_connect,args=(server_port[0],))
thread1.start()
thread2 = threading.Thread(target=fog_node_connect,args=(server_port[1],))
thread2.start()


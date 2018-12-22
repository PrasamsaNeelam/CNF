import socket

def main():
	host = '127.0.0.1'
	port = 5000
	s = socket.socket()
	s.connect((host,port))

	message = input("Enter roll number: ")
	while message != 'q':
		s.send(str.encode(message))
		data = s.recv(1024)
		data = data.decode()
		if data == "ATTENDANCE SUCCESS":
			print("Response from server: " + data.decode())
			break
		print("Response from server: " + data.decode())
		message = input("-> ")
	s.close()

if __name__ == '__main__':
	main() 
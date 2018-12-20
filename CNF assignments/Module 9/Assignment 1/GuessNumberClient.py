import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.connect((host, port))

	message = input("Guess the number")

	while message != 'q':
		s.send(str.encode(message))
		data = s.recv(1024)
		data = data.decode()
		print("Received from server: " + str(data))
		tokens = str(data).split(" ")
		if tokens[0] == "Correct":
			print("Congratulations. Game done.")
			s.close()
			return
		message = input("-> ")
	s.close()

if __name__ == "__main__":
	main()
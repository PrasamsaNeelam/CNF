import socket

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print ("connection from: " + str(addr))
	while True:
		currency = dict({("Dollar", "INR"):67, ("INR", "Dollar"):1/67, ("Dollar", "Pounds"):0.75, ("Pounds", "Dollar"):1/0.75, ("Dollar", "Yen"):113.41, ("Yen", "Dollar"):1/113.41})
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		print ("from connected user: " + str(data))
		tokens = str(data).split(" ")
		key = (tokens[0], tokens[3])
		value = float(tokens[1]) * currency[key]
		print("Sending: " + str(value))
		c.send(str(value).encode())
	c.close()

if __name__ == '__main__':
	main()
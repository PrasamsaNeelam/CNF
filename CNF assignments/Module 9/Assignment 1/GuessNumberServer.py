import socket
import random
import threading

def guess(s):
	c, addr = s.accept()
	print("Connection from: " + str(addr))
	num = random.randint(0,50)
	print("Random number is: " + str(num))
	guesses = 0

	while True:
		message = ""
		data = c.recv(1024)
		data = data.decode()
		if not data:
			break
		print("From connected user: " + str(c) + str(data))
		data = int(data)
		guesses += 1
		if num == data:
			message = "Correct guess. Number of guesses is: " + str(guesses)
			c.send(message.encode())
			c.close()
			return
		elif num > data:
			message = "Number is lesser than guess."
		else:
			message = "Number is greater than guess."

		c.send(str(message).encode())

def main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket()
	s.bind((host, port))
	s.listen(1)

	t1 = threading.Thread(target = guess, args = (s,))
	t2 = threading.Thread(target = guess, args = (s,))
	t3 = threading.Thread(target = guess, args = (s,))

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()
	
if __name__ == '__main__':
	main()

import socket
import threading
import csv

clientList = list()
rollnumbers = list()
questions = {}
answers = {}

def roll(s):
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:
        message = ""
        data = c.recv(1024)
        data = data.decode()
        if not data:
            break
        print("From connected user: " + str(data))
        tokens = data.split(" ")
        if tokens[0] == "MARK-ATTENDANCE":
            # fd = fopen(<data.csv>)
            if tokens[1] in rollnumbers:
                message = "SECRETQUESTION-" + questions{}
                c.send(message.encode())
            else:
                message = ""
                c.send()


def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    t1 = threading.Thread(target = roll, args = (s,))
    t2 = threading.Thread(target = roll, args = (s,))
    t3 = threading.Thread(target = roll, args = (s,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == '__main__':
    main()

#!/usr/bin/python3

import socket
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python whois.py <domain>")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send((sys.argv[1] + "\r\n").encode())
    response = s.recv(1024).split()
    s.close()

    whois = response[19]

    print(whois)

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect((whois, 43))
    s1.send((sys.argv[1] + "\r\n").encode())
    resp = s1.recv(1024)
    print(resp)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import socket

def list_open_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    host = '127.0.0.1'
    start_port = 1
    end_port = 1024
    print(f"Scanning {host} for open ports in range {start_port}-{end_port}...")
    open_ports = list_open_ports(host, start_port, end_port)
    if open_ports:
        print(f"Open ports found: {open_ports}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()

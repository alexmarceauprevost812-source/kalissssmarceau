#!/usr/bin/env python3

import ipaddress
import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed


def normalize_target(raw: str) -> str:
    raw = raw.strip()
    if not raw:
        raise ValueError("Cible vide.")

    try:
        ip = ipaddress.ip_address(raw)
    except ValueError as exc:
        raise ValueError("Entre une adresse IP valide, ex. 192.168.2.40") from exc

    if not (ip.is_private or ip.is_loopback):
        raise ValueError("Par sécurité, seules les adresses privées/locales sont permises.")

    return str(ip)


def _port_open(host: str, port: int) -> int | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.08)
            if sock.connect_ex((host, port)) == 0:
                return port
    except OSError:
        pass
    return None


def list_open_ports(host: str, start_port: int = 1, end_port: int = 1024):
    ports = range(start_port, end_port + 1)
    open_ports = []

    # Nombre limité de workers pour rester léger sur un réseau local.
    with ThreadPoolExecutor(max_workers=48) as executor:
        futures = [executor.submit(_port_open, host, port) for port in ports]
        for future in as_completed(futures):
            port = future.result()
            if port is not None:
                open_ports.append(port)

    return sorted(open_ports)


def main():
    if len(sys.argv) < 2:
        print("Utilisation : python list_ports.py 192.168.2.40")
        raise SystemExit(2)

    try:
        host = normalize_target(sys.argv[1])
    except ValueError as exc:
        print(f"Erreur : {exc}")
        raise SystemExit(2)

    print(f"Scan local de {host} sur les ports 1-1024...")
    open_ports = list_open_ports(host)

    if open_ports:
        print("Ports ouverts :", ", ".join(map(str, open_ports)))
    else:
        print("Aucun port ouvert détecté dans la plage 1-1024.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

import os

def write_targets(targets, file_path):
    with open(file_path, 'w') as file:
        for target in targets:
            file.write(target + '\n')
    print(f"Targets written to {file_path}")

def main():
    targets = ['127.0.0.1', '192.168.1.1', '10.0.0.1', 'johnny', 'harcart']
    file_path = 'kalissmarceau/cible'
    write_targets(targets, file_path)

if __name__ == "__main__":
    main()

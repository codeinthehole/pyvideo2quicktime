#!/usr/bin/env python
import sys

from download import download


if __name__ == '__main__':
    file = sys.argv[1]
    with open(file, 'r') as f:
        for line in f:
            fields = line.strip().split()
            if len(fields) != 2:
                continue
            url, name = fields
            download(url, name)

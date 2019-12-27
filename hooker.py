#!/usr/bin/env python3
import argparse
import sys
import time
import re
import requests
from config import token,chat

url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--re", type=str, required=True)
    parser.add_argument("--token", type=str, required=False)
    parser.add_argument("--chat", type=int, required=False)
    args = parser.parse_args()
    if args.token:
        token = args.token
    if args.chat:
        chat = args.chat
    if not chat or not token:
        print("[*] Token or chat not found")
        sys.exit(-1)
    for line in sys.stdin:
        line = line[:-1]
        if re.match(args.re, line):
            requests.get(url.format(token, chat, line))


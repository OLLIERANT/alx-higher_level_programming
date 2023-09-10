#!/usr/bin/python3
"""
A script that takes in a URL and sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib import request, error


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

        url = sys.argv[1]

        try:
            with request.urlopen(url) as response:
                body = response.read().decode('utf-8')
                print(body)

        except error.HTTPError as e:
            print("Error code:", e.code)

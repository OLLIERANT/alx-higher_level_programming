#!/usr/bin/python3
"""
Takes in a URL and sends a request to the URl
and displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))

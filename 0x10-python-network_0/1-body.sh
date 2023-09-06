#!/bin/bash
# Takes in a URL, sends a GET request to it and displays the response body
curl -Lsf "$1"

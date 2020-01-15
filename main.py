#!/usr/bin/env python3

# We try to stay as close to standard library as possible.
import sys
import json
import os

# Do we have the things we need?

try:
    import argparse
except ImportError:
    print("elastictl requires argparse")
    print("Please run 'pip3 install argparse' before proceeding")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("elastictl requires requests")
    print("Please run 'pip3 install requests' before proceeding")
    sys.exit(1)

# Script specific utilities
# valp has the validate functions
from val_ip import validate_ipv4


def main():
    # Start the argument parser
    parser = argparse.ArgumentParser()
    # Set the cluster endpoint i.e. localhost
    parser.add_argument("--addr", type=str, default="127.0.0.1",
                        help="The address of the Elasticsearch host. Defaults to '127.0.0.1'. Currently only supports\
                        IP addresses")
    # Choose a protocol
    parser.add_argument("--protocol", type=str, default="http",
                        help="Protocol to use, either http or https. Defaults to http")

    # Test the cluster endpoint, check if we can hit the specified port
    parser.add_argument("--test", help="Checks if the given URL and port can \
                        be reached and outputs some helpful data", 
                        action="store_true" )
    # Set the es port we will be using, default of 9200
    parser.add_argument("--port", type=int, default=9200, help="The HTTP port of the\
                         Elasticsearch host. Defaults to 9200")
    
    args = parser.parse_args()
    f = EndPointConstructor(args)
    print(f)
# Construct a valid endpoint here, either composed of an
# IP address with an appropriate protocol and
# port utilized.

class EndPointConstructor():
    def __init__(self, args):
        self.protocol = args.protocol
        self.addr = args.addr
        self.port = args.port

    def __repr__(self):
        return f"{self.protocol}://{self.addr}:{self.port}"

# Map all possible cluster settings and parameters here
class ClusterStatus():
    # Get the current cluster master
    def cluster_settings(self, endpoint):
        pass

# Check the status of your indices here
class IndexStatus():
    # Return a list of all indices
    def index_list(self, endpoint):
        pass
    
if __name__ == '__main__':
    main()

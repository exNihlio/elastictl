#!/usr/bin/env python3

# We try to stay as close to standard library as possible.
import sys
import json
import os

# Do we have the things we need?

try:
    import argparse
except ModuleNotFoundError:
    print("elastictl requires argparse")
    print("Please run 'pip3 install argparse' before proceeding")
    sys.exit(1)

try:
    import httpx
except ModuleNotFoundError:
    print("elastictl requires httpx")
    print("Please run 'pip3 install httpx' before proceeding")
    sys.exit(1)

# Script specific utilities
# valp has the validate functions
from val_ip import validate_ipv4


def main():
    # Start the argument parser
    parser = argparse.ArgumentParser()
    # Set the cluster endpoint i.e. localhost
    parser.add_argument("--addr", type=str, default="127.0.0.1",
                        help="The address of the Elasticsearch host. Defaults to\
                        '127.0.0.1'. Currently only supports\
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

    parser.add_argument("--verbose", help="Enable verbose output of data",
                        action="store_true")

    # Build out args object
    args = parser.parse_args()
    # Are we verbose
    if args.verbose:
      verbose = args.verbose
    else:
      verbose = False

    # Construct out baseurl from the BaseURL class.
    baseurl = BaseURL(args)

    # Default action here: simply see if we hit an ES endpoint
    if args.test:
        pass
    else:
      status = EndpointValues(baseurl, verbose).node_status()
      print(status)

class BaseURL():
    def __init__(self, args):
        self.protocol = args.protocol
        self.addr = args.addr
        self.port = args.port
        self.baseurl = f"{self.protocol}://{self.addr}:{self.port}"
    def __repr__(self):
        return f"{self.protocol}://{self.addr}:{self.port}"

class EndpointValues():
    def __init__(self, baseurl, verbose):
        self.url = baseurl.baseurl
        self.verbose = verbose
    def cluster_settings(self):
        pass

    # Return a list of all indices
    def index_list(self):
        pass

    def node_status(self):
        es_status = httpx.get(self.url)
        if es_status.status_code != 200:
            return f"Error: Recieved: { es_status.status_code }"
        else:
            if self.verbose == True:
                # Get the full data from the endpoint
                return es_status.text
            elif self.verbose == False:
                # We just want to know if the cluster is working.
                es_json = json.loads(es_status.text)
                return f"Elasticsearch is up! Node: { eses__json['name'] }"

if __name__ == '__main__':
    main()

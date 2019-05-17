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
from valp import *


def main():
    argdict = {}
    # Start the argument parser
    parser = argparse.ArgumentParser()
    # Set the cluster endpoint i.e. localhost
    parser.add_argument("--addr", help="The address of the Elasticsearch \
                        host. Defaults to '127.0.0.1'. Currently only supports \
                        IP addresses", action="store_true")
    # Test the cluster endpoint, check if we can hit the specified port
    parser.add_argument("--test", help="Checks if the given URL and port can \
                        be reached and outputs some helpful data" )
    # Set the es port we will be using, default of 9200
    parser.add_argument("--port", help="The HTTP port of the \
                         Elasticsearch host. Defaults to 9200", \
                        action="store_true")
    
    args = parser.parse_args()

    if args.test:
        argdict['test'] = True
    else: 
        argdict['test'] = False

    if args.addr:
        argdict['addr'] = args.addr
    else:
        argdict['addr'] = "127.0.0.1"

    if args.port:
        argdict['port'] = args.port
    else:
        argdict['port'] = 9200

    endpoint = endPointConstructor(argdict)

    print(endpoint)

# Construct the endpoint and parameters we want to hit
def endPointConstructor(argdict):
    # Currently Elasticsearch only supports API calls 
    # over http.
    baseProto = "http://"
    try:
        argdict['port']
    except TypeError:
        print("Something went wrong. The parameters were incorrectly formatted")
        sys.exit(1)

    validIP = validateIPv4(argdict['addr'])

    if validIP == True:
        baseEndpoint = baseProto + argdict['addr']
    else:
        print("Possible improperly formatted IP address")
        print("Exiting")
        sys.exit(1)
    
    if argdict['port'] == 9200:
        baseEndpoint = baseEndpoint + ":" + str(argdict['port'])
    elif argdict['port'] <= 1024: 
        # Log warning the Elasticsearch port we're connecting to 
        # conflicts with other ports.
        print("Warning: 'port' uses a well-known port")
        print("Your Elasticsearch node may conflict with other services")
        baseEndpoint = baseEndpoint + str(argdict['port'])
    else:
        baseEndpoint = baseEndpoint + str(argdict['port'])

    endpoint = baseEndpoint

    return endpoint

# Map all possible cluster settings and parameters here
class clusterStatus():
    # Get the current cluster master
    def clusterMaster(self, endpoint):
        pass

# Check the status of your indices here
class indexStatus():
    # Return a list of all indices
    def indexList(self, endpoint):
        pass
    
if __name__ == '__main__':
    main()
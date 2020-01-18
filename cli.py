import argparse

def parser():
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
    return parser.parse_args()

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

    # Set the es port we will be using, default of 9200
    parser.add_argument("--port", type=int, default=9200, help="The HTTP port of the\
                         Elasticsearch host. Defaults to 9200")
    # Enable verbose mode
    parser.add_argument("--verbose", help="Enable verbose output of data",
                        action="store_true")

    parser.add_argument("--test", default=False, help="Test to see if Elasticsearch is up",
                        action="store_true")

    subparsers = parser.add_subparsers(help="REST API equivalent sub-commands")
    # Create the parser for index related functions
    index_parser = subparsers.add_parser("index", help="Index related functions")
    # This allows us to see which sub-command we've accessed
    index_parser.set_defaults(which='index')
    index_parser.add_argument("--name", type=str, help="Name of the index", required=True)
    index_group = index_parser.add_mutually_exclusive_group()
    index_group.add_argument("--get", action="store_true", help="Get an index")
    index_group.add_argument("--delete", action="store_true", help="Delete an index")
    index_group.add_argument("--create", action="store_true", help="Create an index")
    index_group.add_argument("--exists", action="store_true", help="Check if an index exists")

    # Create the parser for node related functions
    nodes_parser = subparsers.add_parser("node", help="Node related functions")
    # This allows us to see which sub-command we've accessed
    nodes_parser.set_defaults(which='node')
    nodes_parser.add_argument("--name", type=str, help="Name of the node")
    nodes_group = nodes_parser.add_mutually_exclusive_group()
    nodes_group.add_argument("--hot_threads", type=str, help="Return hot threads on specified node")
    nodes_group.add_argument("--stats", type=str, help="Return nodes stats")
    nodes_group.add_argument("--info", type=str, help="Return nodes info")

    # Create the parser for cluster related functions
    cluster_parser = subparsers.add_parser("cluster", help="Cluster related functions")
    cluster_group = cluster_parser.add_mutually_exclusive_group()
    # This allows us to see which sub-command we've accessed
    cluster_parser.set_defaults(which='cluster')
    cluster_group.add_argument("--health", type=str, help="Return the cluster health")
    cluster_group.add_argument("--state", type=str, help="Return the cluster state")
    cluster_group.add_argument("--stats", type=str, help="Return stats of the cluster")

    return parser.parse_args()

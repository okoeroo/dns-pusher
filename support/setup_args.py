import os
import argparse


def argparsing(scriptpath):
    parser = argparse.ArgumentParser(os.path.basename(scriptpath))
    parser.add_argument("-v", "--verbose",
                        dest="verbose",
                        help="Verbose mode. Default is off",
                        action="store_true",
                        default=False)
    parser.add_argument("-i", "--input",
                        dest="inputfilepath",
                        required=True,
                        type=str)
    parser.add_argument("--resolvers",
                        dest="resolvers",
                        help="comma separated list of resolvers",
                        required=False,
                        default="192.168.1.2",
                        type=str)
    parser.add_argument("--timeout",
                        dest="timeout",
                        help="The number of seconds to wait for a response from a server, before timing out.",
                        required=False,
                        default=15,
                        type=int)
    parser.add_argument("--lifetime",
                        dest="lifetime",
                        help="The total number of seconds to spend trying to get an answer to the question.",
                        required=False,
                        default=30,
                        type=int)
    parser.add_argument("--retry-on-servfail",
                        dest="retry_servfail",
                        help="should we retry a nameserver if it says SERVFAIL? The default is 'false'.",
                        action="store_true",
                        default=False)


    return parser.parse_args()


# Setup
def setup(argp: argparse.ArgumentParser) -> dict:
    config = {}

    config['exec'] = os.path.basename(__file__)
    config['verbose'] = argp.verbose
    config['inputfilepath'] = argp.inputfilepath
    config['resolvers'] = argp.resolvers.split(",")
    config['timeout'] = argp.timeout
    config['lifetime'] = argp.lifetime
    config['retry_servfail'] = argp.retry_servfail

    return config
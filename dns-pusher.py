from support.setup_args import setup, argparsing
from support.resolving import resolve
from support.files import read_file_strip_line_lower_case, parse_input_list
    

def main(config: dict) -> bool:
    input_list = read_file_strip_line_lower_case(config['inputfilepath'])
    items_to_resolve = parse_input_list(input_list)
    
    # Resolve the list
    for resolvable in items_to_resolve:
        resolve(config, resolvable['qname'], resolvable['qtype'])


if __name__ == "__main__":
    # Parse commandline arguments
    argp = argparsing(__file__)

    # Setup all the things
    config = setup(argp)
    
    # Main
    main(config)
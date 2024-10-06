import os

# Function to:
# - read the file, line by line
# - strip the line for prefixed and trailing whitespaces
# - lowercase the line
def read_file_strip_line_lower_case(file_path: str) -> list[str]:
    # Ignore
    if file_path is None:
        return None

    # Errors
    if not os.path.exists(file_path):
        raise f"the path {file_path} does not exist."

    if not os.path.isfile(file_path):
        raise f"the path {file_path} is not a file."

    # Read, strip, lower, append
    with open(file_path, 'r') as file:
        cleaned_lines = [line.strip().lower() for line in file.readlines()]
    return cleaned_lines

    
def parse_input_list(input_list: list[str]) -> list[dict]:
    output = []
    
    for item in input_list:
        # Extract values from the string
        qname = item.split('qname="')[1].split('"')[0]
        qtype = item.split('qtype="')[1].split('"')[0]
        rcode = item.split('rcode="')[1].split('"')[0]

        d = {}
        d['qname'] = qname
        d['qtype'] = qtype
        d['rcode'] = rcode

        output.append(d)
    
    return output
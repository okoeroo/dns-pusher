import sys
import dns.resolver


def resolve(config: dict, qname: str, qtype: str) -> dns.resolver.Answers:
    # Setup
    resolver                = dns.resolver.Resolver()
    resolver.nameservers    = config['resolvers']
    resolver.retry_servfail = config['retry_servfail']
    # resolver.timeout        = config['timeout']

    try:
        # DNS Resolve FQDN with specific resource type
        answers = resolver.resolve(qname, qtype)

        print_query = f"qname: {qname}, qtype: {qtype}"
        print_data = ""
        for r_data in answers:
            print_data = f"{print_data}, data: \"{str(r_data)}\""

        # Debug
        print(print_query, print_data)
        
        # Success
        return answers
        
    # Warnings
    except dns.resolver.NoNameservers:
        print(f"Resolver warning: NoNameservers: The query could not be processed by any of the available servers., qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)
    except dns.resolver.NXDOMAIN:
        print(f"Resolver warning: NXDOMAIN, qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)
    except dns.resolver.NoAnswer:
        print(f"Resolver warning: NoAnswer available, qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)
    
    # Errors
    except dns.resolver.NoMetaqueries:
        print(f"Resolver error: SERVFAIL: Server failed to process the query., qname=\"{qname}, qtype=\"{qtype}\"")
    except dns.exception.Timeout:
        print(f"Resolver error: Timeout reached, qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)
    except EOFError:
        print(f"Resolver error: EOF Error, qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)
    except Exception as e:
        print(f"Resolver error: \"{str(e)}\"EOF Error, qname=\"{qname}, qtype=\"{qtype}\"", file=sys.stderr)

    return None
    

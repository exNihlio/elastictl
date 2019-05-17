try:
    import ipaddress
except ImportError:
    print("elastictl requires 'ipaddress'")
    print("Please run 'pip3 install ipaddress' before proceeding")

def validateIPv4(input):
    try:
         ipaddress.IPv4Address(input)
    except AddressValueError:
        print("Possible improperly formatted IP address")
        return False

    return True

def validateIPv6(input):
    return False
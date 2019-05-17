import socket

# Stolen from https://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python
def validateIPv4(input):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except:
        return False
    
    return True
    
def validateIPv6(input):
    return False
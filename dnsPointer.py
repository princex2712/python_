import socket
def get_domain_name(ip_address):
    result = socket.gethostbyaddr(ip_address)
    return list(result)[0]
print(get_domain_name("108.158.58.146"))

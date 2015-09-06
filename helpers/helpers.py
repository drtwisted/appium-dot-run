__author__ = 'twisted'


def check_ip(ip):
    def is_valid_octet(octet):
        return 0 <= int(octet) <= 254

    ip = ip.split('.')
    if len(ip) != 4:
        return False
    elif is_valid_octet(ip[0]) and is_valid_octet(ip[1]) and \
            is_valid_octet(ip[2]) and is_valid_octet(ip[3]):
        return True
    else:
        return False


def write_to_file(fname, data):
    with open(fname, 'aw') as file:
        file.write(data)
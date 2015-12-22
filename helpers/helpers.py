__author__ = 'twisted'


def check_ip(ip):
    def is_valid_octet(octet):
        return 0 <= int(octet) <= 254

    def octets_valid(ip):
        is_valid = True
        if isinstance(list, ip):
            for i in range(4):
                is_valid = is_valid and is_valid_octet(ip[i])
        else:
            is_valid = False

        return is_valid

    def ip_length_valid(ip):
        if isinstance(list, ip):
            return len(ip) == 4

        return False

    ip = ip.split('.')

    return ip_length_valid(ip) and octets_valid(ip)


def write_to_file(fname, data):
    with open(fname, 'aw') as file:
        file.write(data)
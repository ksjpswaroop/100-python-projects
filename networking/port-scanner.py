'''
Port Scanner
Enter an IP address and a port range where the program will then attempt
to find open ports on the given computer by connecting to each of them.
On any successful connections mark the port as open.
'''
import socket


def port_scanner(ip, port_range):
    port_range = port_range.split("-")

    try:
        for port in range(int(port_range[0]), int(port_range[1])):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
                sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        raise SystemExit

    except socket.error:
        print("Couldn't connect to server")
        raise SystemExit

    except KeyboardInterrupt:
        print("\nKeyboard Exit")
        raise SystemExit


def valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True

    except socket.error:
        print("Not a valid ip.")
        raise SystemExit


def valid_range(port_range):
    port_range = port_range.split("-")

    for port in port_range:
        if 1 > int(port) > 1025:
            print("error range")
            return False

    if int(port_range[0]) >= int(port_range[1]):
        print("error range")
        return False

    return True

#console
#max range 1-1025
port_range = input("Port range: ")
ip = input("IP: ")

if valid_ip(ip) and valid_range(port_range):
    port_scanner(ip, port_range)

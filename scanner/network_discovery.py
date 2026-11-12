import nmap
import ipaddress

def network_discovery():

    print("\n===== NETSENTRY NETWORK DISCOVERY =====")

    target = input("Enter your authorized private network (example: 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(target, strict=False)

        if not network.is_private or network.prefixlen < 24:
            print("Enter a private network with /24 or smaller scope.")
            return

        scanner = nmap.PortScanner()

        print("\nScanning network...")
        
        scanner.scan(
            hosts=str(network),
            arguments="-sn"
        )

        print("\n===== ACTIVE DEVICES =====")

        found = False

        for host in scanner.all_hosts():

            if scanner[host].state() == "up":

                found = True

                print("\nIP Address:", host)

                hostname = scanner[host].hostname()

                print("Hostname:", hostname or "Unknown")

                print("Status: ACTIVE")

        if not found:
            print("No active devices found.")

    except ValueError:
        print("Invalid network address.")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    network_discovery()

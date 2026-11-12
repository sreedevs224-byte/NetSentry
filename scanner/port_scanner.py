import nmap
import ipaddress

def port_scanner():

    print("\n===== NETSENTRY PORT SCANNER =====")

    target = input("Enter target private IP: ")

    try:
        ip = ipaddress.ip_address(target)

        if not ip.is_private:
            print("Only private IP addresses are allowed.")
            return

        scanner = nmap.PortScanner()

        ports = "22,80,443,445,3306,3389,8080"

        print("\nScanning authorized target:", target)

        scanner.scan(
            hosts=target,
            arguments=f"-sT -Pn -p {ports}"
        )

        if target not in scanner.all_hosts():
            print("Target did not respond.")
            return

        print("\n===== PORT SCAN RESULTS =====")

        for port in scanner[target].all_tcp():

            state = scanner[target]['tcp'][port]['state']

            print(f"Port: {port} | Status: {state.upper()}")

    except ValueError:
        print("Invalid IP address.")

    except Exception as error:
        print("Scanner Error:", error)


if __name__ == "__main__":
    port_scanner()

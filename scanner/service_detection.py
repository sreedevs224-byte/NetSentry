import nmap
import ipaddress

def service_detection():

    print("\n===== NETSENTRY SERVICE DETECTION =====")

    target = input("Enter authorized private IP: ")

    try:
        ip = ipaddress.ip_address(target)

        if not ip.is_private:
            print("Private IP required!")
            return

        scanner = nmap.PortScanner()

        print("\nDetecting services...")

        scanner.scan(
            hosts=target,
            arguments="-sV -p 22,80,443,445,3306,8080"
        )

        if target not in scanner.all_hosts():
            print("Target not found!")
            return

        print("\n===== SERVICE RESULTS =====")

        for port in scanner[target].all_tcp():

            data = scanner[target]['tcp'][port]

            print("\nPort:", port)
            print("State:", data['state'])
            print("Service:", data['name'])
            print("Product:", data.get('product') or 'Unknown')
            print("Version:", data.get('version') or 'Unknown')

    except ValueError:
        print("Invalid IP address!")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    service_detection()

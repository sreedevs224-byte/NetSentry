import nmap
import ipaddress

def risk_analyzer():

    print("\n===== NETSENTRY RISK ANALYZER =====")

    target = input("Enter authorized private IP: ")

    try:
        ip = ipaddress.ip_address(target)

        if not ip.is_private:
            print("Private IP required!")
            return

        scanner = nmap.PortScanner()

        ports = "22,80,443,445,3306,3389,8080"

        scanner.scan(
            hosts=target,
            arguments=f"-sT -Pn -p {ports}"
        )

        if target not in scanner.all_hosts():
            print("Target not found!")
            return

        print("\n===== SECURITY ANALYSIS =====")

        for port in scanner[target].all_tcp():

            data = scanner[target]['tcp'][port]

            state = data['state']

            print(f"\nPort: {port}")
            print(f"State: {state.upper()}")

            if state == "filtered":

                risk = "UNKNOWN"
                message = "Traffic filtering detected."

            elif state == "closed":

                risk = "LOW"
                message = "No service accepting connections."

            elif port in [445, 3306, 3389]:

                risk = "HIGH"
                message = "Review whether this service needs network exposure."

            elif port in [22, 80, 443, 8080]:

                risk = "MEDIUM"
                message = "Review service configuration and access controls."

            else:

                risk = "REVIEW"
                message = "Manual security review recommended."

            print("Risk Level:", risk)
            print("Observation:", message)

        print("\n===== ANALYSIS COMPLETED =====")

    except ValueError:
        print("Invalid IP address!")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    risk_analyzer()


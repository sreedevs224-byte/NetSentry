from flask import Flask, render_template, request, send_file, session
import nmap
import ipaddress

from datetime import datetime
from reports.pdf_report import generate_report

app = Flask(__name__)

app.secret_key = "netsentry-local-development-key"


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    target = ""
    error = ""
    scan_time = ""

    if request.method == "POST":

        target = request.form.get("target", "").strip()

        # Clear previous scan data
        session.pop("results", None)
        session.pop("target", None)
        session.pop("scan_time", None)

        try:
            ip = ipaddress.ip_address(target)

            if not ip.is_private:
                raise ValueError("Private IP required!")

            scanner = nmap.PortScanner()

            ports = "22,80,443,445,3306,3389,8080"

            scanner.scan(
                hosts=target,
                arguments=f"-sT -Pn -p {ports}"
            )

            if target not in scanner.all_hosts():

                error = "Target not found!"

            else:

                for port in scanner[target].all_tcp():

                    data = scanner[target]["tcp"][port]

                    state = data["state"]

                    if state == "filtered":

                        risk = "UNKNOWN"
                        observation = "Traffic filtering detected."

                    elif state == "closed":

                        risk = "LOW"
                        observation = "No service accepting connections."

                    elif port in [445, 3306, 3389]:

                        risk = "REVIEW"
                        observation = "Review service exposure."

                    else:

                        risk = "MEDIUM"
                        observation = "Review service configuration."

                    results.append({

                        "port": port,
                        "state": state.upper(),
                        "service": data["name"],
                        "risk": risk,
                        "observation": observation

                    })

                # Save scan results
                scan_time = datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )

                session["results"] = results
                session["target"] = target
                session["scan_time"] = scan_time

        except ValueError as e:

            error = str(e) or "Invalid IP address!"

        except Exception as e:

            error = "Scanner error: " + str(e)

    else:

        results = session.get("results", [])
        target = session.get("target", "")
        scan_time = session.get("scan_time", "")

    # Port statistics
    stats = {

        "total": len(results),

        "open": sum(
            1 for r in results if r["state"] == "OPEN"
        ),

        "closed": sum(
            1 for r in results if r["state"] == "CLOSED"
        ),

        "filtered": sum(
            1 for r in results if r["state"] == "FILTERED"
        ),

        # Risk statistics
        "low": sum(
            1 for r in results if r["risk"] == "LOW"
        ),

        "medium": sum(
            1 for r in results if r["risk"] == "MEDIUM"
        ),

        "high": sum(
            1 for r in results if r["risk"] == "HIGH"
        ),

        "unknown": sum(
            1 for r in results if r["risk"] == "UNKNOWN"
        ),

        "review": sum(
            1 for r in results if r["risk"] == "REVIEW"
        )
    }

    return render_template(

        "index.html",

        results=results,
        target=target,
        error=error,
        stats=stats,
        scan_time=scan_time

    )


@app.route("/download")
def download():

    results = session.get("results")
    target = session.get("target")

    if not results or not target:

        return "Please run a scan first.", 400

    filename = generate_report(results, target)

    return send_file(

        filename,
        as_attachment=True,
        download_name="NetSentry_Report.pdf"

    )


if __name__ == "__main__":

    app.run(debug=True)

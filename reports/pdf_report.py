from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib.colors import HexColor
from datetime import datetime
from xml.sax.saxutils import escape
import os


def generate_report(results, target):

    filename = os.path.join(
        os.path.dirname(__file__),
        "NetSentry_Report.pdf"
    )

    # Calculate statistics
    stats = {
        "total": len(results),
        "open": sum(1 for r in results if r["state"] == "OPEN"),
        "closed": sum(1 for r in results if r["state"] == "CLOSED"),
        "filtered": sum(1 for r in results if r["state"] == "FILTERED"),
        "low": sum(1 for r in results if r["risk"] == "LOW"),
        "medium": sum(1 for r in results if r["risk"] == "MEDIUM"),
        "high": sum(1 for r in results if r["risk"] == "HIGH"),
        "unknown": sum(1 for r in results if r["risk"] == "UNKNOWN"),
        "review": sum(1 for r in results if r["risk"] == "REVIEW")
    }

    # PDF document
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=22 * mm,
        bottomMargin=20 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=25,
        textColor=HexColor("#007c91"),
        alignment=TA_CENTER,
        spaceAfter=15
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        textColor=HexColor("#007c91"),
        spaceBefore=15,
        spaceAfter=10
    )

    normal_style = styles["BodyText"]

    small_style = ParagraphStyle(
        "Small",
        parent=normal_style,
        fontSize=8,
        leading=11
    )

    story = []

    # Cover section
    story.append(Spacer(1, 45 * mm))

    story.append(
        Paragraph("NETSENTRY", title_style)
    )

    story.append(
        Paragraph(
            "SMART NETWORK SECURITY AUDITOR",
            ParagraphStyle(
                "Subtitle",
                parent=styles["Normal"],
                alignment=TA_CENTER,
                fontSize=13,
                textColor=HexColor("#475569")
            )
        )
    )

    story.append(Spacer(1, 25 * mm))

    cover_data = [
        ["SECURITY AUDIT REPORT"],
        [f"Target IP: {escape(target)}"],
        [f"Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"]
    ]

    cover_table = Table(
        cover_data,
        colWidths=[150 * mm]
    )

    cover_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#007c91")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("BACKGROUND", (0, 1), (-1, -1), HexColor("#e2e8f0")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 15),
        ("TOPPADDING", (0, 0), (-1, -1), 15),
        ("BOX", (0, 0), (-1, -1), 1, HexColor("#007c91"))
    ]))

    story.append(cover_table)

    story.append(Spacer(1, 25 * mm))

    story.append(
        Paragraph(
            "Confidentiality: This report is intended for authorized "
            "network security assessment purposes.",
            ParagraphStyle(
                "Notice",
                parent=normal_style,
                alignment=TA_CENTER,
                textColor=HexColor("#64748b")
            )
        )
    )

    story.append(PageBreak())

    # Statistics
    story.append(
        Paragraph("1. NETWORK SCAN STATISTICS", heading_style)
    )

    stats_data = [
        ["Metric", "Result"],
        ["Total Ports", str(stats["total"])],
        ["Open Ports", str(stats["open"])],
        ["Closed Ports", str(stats["closed"])],
        ["Filtered Ports", str(stats["filtered"])]
    ]

    stats_table = Table(
        stats_data,
        colWidths=[90 * mm, 50 * mm]
    )

    stats_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#007c91")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, HexColor("#e2e8f0")]),
        ("PADDING", (0, 0), (-1, -1), 9)
    ]))

    story.append(stats_table)

    # Risk summary
    story.append(
        Paragraph("2. RISK SUMMARY", heading_style)
    )

    risk_data = [
        ["Risk Category", "Count"],
        ["Low", str(stats["low"])],
        ["Medium", str(stats["medium"])],
        ["High", str(stats["high"])],
        ["Unknown", str(stats["unknown"])],
        ["Review Required", str(stats["review"])]
    ]

    risk_table = Table(
        risk_data,
        colWidths=[90 * mm, 50 * mm]
    )

    risk_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#007c91")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, HexColor("#e2e8f0")]),
        ("PADDING", (0, 0), (-1, -1), 9)
    ]))

    story.append(risk_table)

    # Detailed scan results
    story.append(
        Paragraph("3. DETAILED SCAN RESULTS", heading_style)
    )

    result_data = [[
        "Port",
        "State",
        "Service",
        "Risk",
        "Observation"
    ]]

    for item in results:

        result_data.append([
            str(item["port"]),
            escape(item["state"]),
            escape(item["service"]),
            escape(item["risk"]),
            Paragraph(
                escape(item["observation"]),
                small_style
            )
        ])

    result_table = Table(
        result_data,
        colWidths=[
            15 * mm,
            23 * mm,
            28 * mm,
            22 * mm,
            67 * mm
        ],
        repeatRows=1
    )

    result_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HexColor("#007c91")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [colors.white, HexColor("#e2e8f0")]),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("PADDING", (0, 0), (-1, -1), 6)
    ]))

    story.append(result_table)

    # Recommendations
    story.append(
        Paragraph("4. SECURITY RECOMMENDATIONS", heading_style)
    )

    recommendations = [
        "Review all open ports and confirm that each service is required.",
        "Check firewall rules and network access restrictions.",
        "Keep exposed services and software updated.",
        "Investigate filtered ports when further verification is necessary.",
        "Review service configurations and authentication controls."
    ]

    for recommendation in recommendations:

        story.append(
            Paragraph(
                "&#8226; " + escape(recommendation),
                normal_style
            )
        )

        story.append(Spacer(1, 6))

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "Note: Risk categories are preliminary rule-based indicators. "
            "Open ports do not automatically indicate vulnerabilities. "
            "This report is not a complete vulnerability assessment.",
            small_style
        )
    )

    # Header and footer
    def add_page_details(canvas, document):

        canvas.saveState()

        canvas.setFont("Helvetica", 8)

        canvas.setFillColor(HexColor("#64748b"))

        canvas.drawString(
            18 * mm,
            12 * mm,
            "NETSENTRY SECURITY REPORT"
        )

        canvas.drawRightString(
            A4[0] - 18 * mm,
            12 * mm,
            f"Page {document.page}"
        )

        canvas.restoreState()

    doc.build(
        story,
        onFirstPage=add_page_details,
        onLaterPages=add_page_details
    )

    return filename

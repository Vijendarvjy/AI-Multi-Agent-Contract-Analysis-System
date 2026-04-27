def generate_report(results: dict):
    report = "# Contract Analysis Report\n\n"

    for domain, analysis in results.items():
        report += f"## {domain.title()} Analysis\n"
        report += analysis + "\n\n"

    return report

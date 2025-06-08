class RecommendationReportAgent:
    def __init__(self):
        pass

    def run(self, customer_profile: dict, scored_opportunities: list) -> str:
        name = customer_profile.get("Customer Name", "Unknown")
        industry = customer_profile.get("Industry", "Unknown")
        revenue = customer_profile.get("Annual Revenue (USD)", "N/A")
        products = customer_profile.get("Current Products", "")
        location = customer_profile.get("Location", "N/A")

        report = []
        report.append(f"Research Report: Cross-Sell and Upsell Opportunities for **{name}**\n")

        report.append("###  Introduction:\n")
        report.append(
            f"This report analyzes the recent purchasing behavior of **{name}**, "
            f"a company in the **{industry}** sector, to identify targeted cross-sell and upsell opportunities. "
            f"Their recent engagement with products like **{products}** and their business profile "
            f"help shape the personalized recommendations in this report.\n"
        )

        # Customer Overview
        report.append("### Customer Overview:\n")
        report.append(f"- Industry: {industry}")
        report.append(f"- Revenue: ${revenue:,}")
        report.append(f"- Location: {location}")
        report.append(f"- Current Products: {products}\n")

        # Insights
        report.append("### Data-Driven Insights:\n")
        if scored_opportunities:
            for opp in scored_opportunities:
                product = opp['product']
                score = opp['score']
                reasons = "; ".join(opp['rationale'])
                report.append(f"- **{product}** (Score: {score}) — {reasons}")
        else:
            report.append("No significant cross-sell or upsell opportunities found.\n")

        # Recommendations
        report.append("\n###  Recommendations:\n")
        for i, opp in enumerate(scored_opportunities[:3], 1):  # Top 3
            product = opp['product']
            report.append(f"{i}. Recommend **{product}** based on usage trends and profile fit.")

        # Conclusion
        report.append("\n###  Conclusion:\n")
        report.append("Targeted campaigns based on these suggestions can enhance customer value and increase revenue.\n")

        return "\n".join(report)

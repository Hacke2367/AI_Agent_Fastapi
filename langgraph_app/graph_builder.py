from agents.customer_context import CustomerContextAgent
from agents.purchase_pattern import PurchasePattern
from agents.product_affinity import ProductAffinity
from agents.oppourtinty import OppurtunityScoring
from agents.report_genreator import RecommendationReportAgent

def run_graph(customer_id:str) -> dict:

    context_agent = CustomerContextAgent()
    profile = context_agent.run(customer_id)

    pattern_agent = PurchasePattern()
    pattern_data = pattern_agent.run(profile)

    affinity_agent = ProductAffinity()
    affinity_data = affinity_agent.run(profile)

    scoring_agent = OppurtunityScoring()
    scored_opportunities = scoring_agent.run(profile, pattern_data, affinity_data)

    report_agent = RecommendationReportAgent()
    report = report_agent.run(profile, scored_opportunities)

    return {
        "research_report": report,
        "recommendations": scored_opportunities
    }
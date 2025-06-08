class OppurtunityScoring:
    def __init__(self):
        pass

    def run(self, customer_profile: dict, pattern_data: dict, affinity_suggestions: list) -> list:

        priority = customer_profile.get("Customer Priority Rating", "Medium")
        synergy = customer_profile.get("Cross-Sell Synergy", "")
        synergy_keywords = synergy.split(",") if synergy else []

        scored_opportunities = []

        for product in pattern_data.get("missing_opportunities", []) + affinity_suggestions:
            score = 0
            rationale = []

            if product in synergy_keywords:
                score += 40
                rationale.append("Product mentioned in synergy list")

            if priority == "High":
                score += 30
                rationale.append("Customer is high priority")

            if product in affinity_suggestions:
                score += 20
                rationale.append("Product is a related product (affinity-based)")

            if score > 0:
                scored_opportunities.append({
                    "product": product,
                    "score": score,
                    "rationale": rationale
                })

        scored_opportunities.sort(key=lambda x: x["score"], reverse=True)
        return scored_opportunities


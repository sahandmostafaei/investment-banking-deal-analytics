def build_valuation_summary(
    dcf_value,
    comparable_value,
    precedent_value,
):
    return {
        "dcf_enterprise_value": dcf_value,
        "comparable_enterprise_value": comparable_value,
        "precedent_enterprise_value": precedent_value,
        "average_enterprise_value": (
            dcf_value
            + comparable_value
            + precedent_value
        ) / 3,
    }

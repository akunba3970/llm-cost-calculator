def estimate_cost(model, tokens):
    """
    Simple example cost estimator for LLM usage
    """

    pricing = {
        "gpt-4": 0.03 / 1000,
        "gpt-4-mini": 0.002 / 1000,
        "claude": 0.015 / 1000,
        "gemini": 0.002 / 1000
    }

    if model not in pricing:
        return "Unknown model"

    cost = tokens * pricing[model]

    return round(cost, 4)

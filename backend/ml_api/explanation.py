def explain_features(features):
    """
    Lightweight, rule-based explanations (SHAP-lite).
    Takes extracted feature dict and returns top reasons.
    """

    explanations = []

    if features.get("url_length", 0) > 75:
        explanations.append("Long URL length")

    if features.get("num_subdomains", 0) > 2:
        explanations.append("Multiple subdomains")

    if features.get("digit_ratio", 0) > 0.2:
        explanations.append("High number of digits in URL")

    if features.get("suspicious_word_count", 0) > 0:
        explanations.append("Suspicious keywords present")

    if features.get("count_special_chars", 0) > 5:
        explanations.append("Many special characters")

    return explanations[:3]

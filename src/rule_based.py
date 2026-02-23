harm_keywords = ["mati", "bunuh", "suicide"]
bias_keywords = ["semua", "selalu", "memang", "dasarnya"]
fairness_keywords = ["hak", "adil", "setara"]

def keyword_score(text, keywords):
    text = text.lower()
    matches = sum(1 for k in keywords if k in text)
    return min(matches / len(keywords), 1.0)

def evaluate_rule_based(text):
    return {
        "harm_score": keyword_score(text, harm_keywords),
        "bias_score": keyword_score(text, bias_keywords),
        "fairness_score": keyword_score(text, fairness_keywords)
    }

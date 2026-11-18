# 03. Prompt Evaluation - Judging Prompt Quality with Tests

def evaluate_response(response, keywords):
    matched = [w for w in keywords if w.lower() in response.lower()]
    return f"Score: {len(matched)}/{len(keywords)}"

if __name__ == "__main__":
    output = "Python uses lists and dictionaries as core data structures."
    print(evaluate_response(output, ["Python", "lists", "dictionaries"]))

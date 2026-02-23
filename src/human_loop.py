import json

def human_review(ai_output, text):
    print("\n--- AI Evaluation ---")
    print(ai_output)

    decision = input("\nDo you agree with this evaluation? (y/n): ")

    result = {
        "text": text,
        "ai_output": ai_output,
        "human_agree": decision
    }

    with open("human_feedback.jsonl", "a") as f:
        f.write(json.dumps(result) + "\n")

    print("Feedback saved.")

from src.rule_based import evaluate_rule_based
from src.ai_evaluator import evaluate_with_ai
from src.human_loop import human_review

def main():
    while True:
        text = input("\nMasukkan teks (atau ketik 'exit'): ")

        if text.lower() == "exit":
            break

        print("\nRule-Based Evaluation:")
        print(evaluate_rule_based(text))

        print("\nAI Evaluation:")
        ai_output = evaluate_with_ai(text)
        print(ai_output)

        human_review(ai_output, text)

if __name__ == "__main__":
    main()

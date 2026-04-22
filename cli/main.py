from app.bio.sequence_analysis import analyze_sequence


def run_sequence_analysis(sequence: str):
    result = analyze_sequence(sequence)

    print("\nSequence Analysis Result")
    print("------------------------")

    for key, value in result.items():
        print(f"{key}: {value}")
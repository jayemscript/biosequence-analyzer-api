from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction


def clean_sequence(sequence: str) -> str:
    return sequence.replace(" ", "").replace("\n", "").upper()


def validate_dna(sequence: str) -> bool:
    valid_bases = set("ATCG")
    return all(base in valid_bases for base in sequence)


def gc_content(sequence: str) -> float:
    seq = Seq(sequence)
    return round(gc_fraction(seq) * 100, 2)


def reverse_complement(sequence: str) -> str:
    seq = Seq(sequence)
    return str(seq.reverse_complement())


def transcribe(sequence: str) -> str:
    seq = Seq(sequence)
    return str(seq.transcribe())


def translate(sequence: str) -> str:
    seq = Seq(sequence)
    # Add N's to complete the final codon if needed
    remainder = len(seq) % 3
    if remainder:
        seq = seq + Seq("N" * (3 - remainder))
    return str(seq.translate(to_stop=True))


def analyze_sequence(sequence: str) -> dict:
    sequence = clean_sequence(sequence)

    if not validate_dna(sequence):
        raise ValueError("Invalid DNA sequence. Only A, T, C, G allowed.")

    return {
        "input": sequence,
        "gc_content": gc_content(sequence),
        "reverse_complement": reverse_complement(sequence),
        "rna": transcribe(sequence),
        "protein": translate(sequence),
    }


if __name__ == "__main__":
    print("DNA/RNA Sequence Analyzer")
    print("-------------------------")

    user_input = input("Enter DNA sequence: ")

    try:
        result = analyze_sequence(user_input)
        print("\nResult:")
        for key, value in result.items():
            print(f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
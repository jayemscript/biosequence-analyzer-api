import sys
from cli.main import run_sequence_analysis


def main():
    if len(sys.argv) < 3:
        return

    mode = sys.argv[1]
    command = sys.argv[2]
    input_value = sys.argv[3] if len(sys.argv) > 3 else None

    if mode == "test":

        if command == "--sequence_analysis":
            if not input_value:
                input_value = input("Enter DNA sequence: ")

            run_sequence_analysis(input_value)

        else:
            print(f"Unknown command: {command}")

    else:
        print(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()
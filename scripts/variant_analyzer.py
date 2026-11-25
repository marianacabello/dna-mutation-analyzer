
def validate_dna(sequence):
    """Check whether a DNA sequence contains only A, T, C and G."""
    sequence = sequence.upper().strip()
    return len(sequence) > 0 and all(base in "ATCG" for base in sequence)


def analyze_dna(sequence):
    """Calculate the length and nucleotide frequencies of a DNA sequence."""
    sequence = sequence.upper().strip()

    results = {
        "Length": len(sequence),
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G")
    }

    return results


def main():
    print("=== DNA Mutation Analyzer ===")
    sequence = input("Enter a DNA sequence: ")

    if not validate_dna(sequence):
        print("Error: The sequence must contain only A, T, C and G.")
        return

    results = analyze_dna(sequence)

    print("\nAnalysis results:")
    print(f"Sequence length: {results['Length']} bases")
    print(f"A: {results['A']}")
    print(f"T: {results['T']}")
    print(f"C: {results['C']}")
    print(f"G: {results['G']}")


if __name__ == "__main__":
    main()


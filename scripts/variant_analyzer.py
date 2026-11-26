
from pathlib import Path
import csv


def load_fasta(file_path):
    """Load a DNA sequence from a FASTA file."""
    content = Path(file_path).read_text(encoding="utf-8")
    lines = content.splitlines()

    if not lines or not lines[0].startswith(">"):
        raise ValueError("The file does not have a valid FASTA header.")

    header = lines[0]
    sequence = "".join(
        line.strip().upper()
        for line in lines[1:]
        if line.strip() and not line.startswith(">")
    )

    if not sequence or any(base not in "ATCGN" for base in sequence):
        raise ValueError("The FASTA sequence contains invalid characters.")

    return header, sequence


def analyze_dna(sequence):
    """Calculate sequence length and nucleotide counts."""
    sequence = sequence.upper().strip()

    return {
        "Length": len(sequence),
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "C": sequence.count("C"),
        "G": sequence.count("G"),
        "N": sequence.count("N"),
    }


def compare_sequences(reference, sample):
    """Find substitutions between two equal-length DNA sequences."""

    reference = reference.upper().strip()
    sample = sample.upper().strip()

    if len(reference) != len(sample):
        raise ValueError(
            "Both sequences must have the same length for this comparison."
        )

    differences = []

    for i in range(len(reference)):
        if reference[i] != sample[i]:
            differences.append({
                "position": i + 1,
                "reference": reference[i],
                "observed": sample[i],
            })

    return differences


def save_results(differences, output_path):
    """Save detected differences to a CSV file."""

    with open(output_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["position", "reference", "observed"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(differences)

    print(f"\nResults saved to: {output_path}")


def main():
    reference_path = Path("data") / "BRCA1.fasta"

    header, sequence = load_fasta(reference_path)
    results = analyze_dna(sequence)

    print("=== BRCA1 Reference Analyzer ===")
    print(f"Reference: {header}")
    print(f"Sequence length: {results['Length']:,} bases")

    print("\nNucleotide counts:")
    for base in ["A", "T", "C", "G", "N"]:
        print(f"{base}: {results[base]:,}")

    total = sum(results[base] for base in ["A", "T", "C", "G", "N"])
    print(f"\nTotal bases counted: {total:,}")
    print("Counts match sequence length:", total == results["Length"])


if __name__ == "__main__":
    main()



# Interactive comparison using a short BRCA1 reference fragment
header, reference = load_fasta("data/BRCA1.fasta")

start = 100
reference_fragment = reference[start:start + 20]

print("\n=== BRCA1 Sequence Comparison ===")
print(f"Reference fragment: {reference_fragment}")
print("Enter a DNA sequence of exactly 20 bases.")
sample = input("Your sequence: ").upper().strip()

if len(sample) != len(reference_fragment):
    print("Error: Your sequence must contain exactly 20 bases.")
elif any(base not in "ATCGN" for base in sample):
    print("Error: Use only A, T, C, G or N.")
else:
    differences = compare_sequences(reference_fragment, sample)

    
    results = []

    for difference in differences:
        results.append({
            "position": start + difference["position"],
            "reference": difference["reference"],
            "observed": difference["observed"],
        })

    if not results:
        print("No differences found in this fragment.")
    else:
        print("\nDifferences found:")
        for result in results:
            print(
                f"Reference file position: {result['position']} | "
                f"{result['reference']} > {result['observed']}"
            )

    output_path = Path("results") / "brca1_results.csv"
    save_results(results, output_path)


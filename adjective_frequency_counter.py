"""
Count adjective frequency in an NLTK corpus text.

This script lets a user choose an available NLTK corpus and text file,
then extracts adjectives and reports their total frequency.
"""

from collections import Counter

import nltk
from nltk.corpus import brown, gutenberg, inaugural, reuters, webtext


CORPORA = {
    "brown": brown,
    "gutenberg": gutenberg,
    "inaugural": inaugural,
    "reuters": reuters,
    "webtext": webtext,
}

ADJECTIVE_TAGS = {"JJ", "JJR", "JJS"}
EXCLUDED_WORDS = {"such"}


def choose_corpus():
    """Prompt the user to choose an available corpus."""
    print("Available corpora:")
    for name in CORPORA:
        print(f"- {name}")

    while True:
        choice = input("\nChoose a corpus: ").strip().lower()
        if choice in CORPORA:
            return choice, CORPORA[choice]

        print("Invalid corpus. Please choose one from the list.")


def choose_file(corpus):
    """Prompt the user to choose a file from the selected corpus."""
    file_ids = corpus.fileids()

    print("\nAvailable files:")
    for file_id in file_ids[:25]:
        print(f"- {file_id}")

    if len(file_ids) > 25:
        print(f"...and {len(file_ids) - 25} more")

    while True:
        choice = input("\nChoose a file ID: ").strip()
        if choice in file_ids:
            return choice

        print("Invalid file ID. Please copy one exactly from the list.")


def extract_adjectives(text):
    """Extract adjectives from text using NLTK POS tags."""
    tokens = nltk.word_tokenize(text)
    tagged_tokens = nltk.pos_tag(tokens)

    adjectives = []

    for word, tag in tagged_tokens:
        if tag in ADJECTIVE_TAGS and word.lower() not in EXCLUDED_WORDS:
            adjectives.append(word.lower())

    return adjectives


def format_results(corpus_name, file_id, adjective_counts):
    """Format adjective frequency results."""
    lines = [
        f"Corpus: {corpus_name}",
        f"File: {file_id}",
        f"Total adjectives: {sum(adjective_counts.values())}",
        f"Unique adjectives: {len(adjective_counts)}",
        "",
        "Most common adjectives:",
    ]

    for adjective, count in adjective_counts.most_common():
        lines.append(f"{adjective}: {count}")

    return "\n".join(lines)


def main():
    """Run the adjective counter workflow."""
    corpus_name, corpus = choose_corpus()
    file_id = choose_file(corpus)

    text = corpus.raw(file_id)
    adjectives = extract_adjectives(text)
    adjective_counts = Counter(adjectives)

    output_file = input("\nEnter output filename, e.g. adjective_counts.txt: ").strip()
    results = format_results(corpus_name, file_id, adjective_counts)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(results)

    print(f"\nSaved {sum(adjective_counts.values())} adjective tokens to {output_file}")


if __name__ == "__main__":
    main()

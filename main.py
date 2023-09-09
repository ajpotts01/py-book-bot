
def count_letters(text: str) -> dict[str, int]:
    letter_counts: dict[str, int] = {}

    for next_letter in text.lower():
        if not(next_letter in letter_counts.keys()):
            letter_counts[next_letter] = 0
        
        letter_counts[next_letter] += 1

    return letter_counts

def main() -> None:
    with open("books/frankenstein.txt") as f:
        contents: str = f.read()

        words: list[str] = contents.split() # Defaults to space?
        result: dict[str, int] = count_letters(str(words))

        letters: list[tuple] = [(k, v) for k, v in result.items() if k.isalpha()]
        letters = sorted(letters)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        for lc in letters:
            print(f"The '{lc[0]}' character was found {lc[1]} times")


if __name__ == "__main__":
    main()
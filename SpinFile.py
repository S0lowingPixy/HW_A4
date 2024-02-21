from Spinner import Spinner

def main():
    synonym_file = 'synonyms-simplified.txt'
    spinner = Spinner(synonym_file)

    with open('essay.txt', 'r') as file:
        original_text = file.read().lower().strip()

    print("Original:", original_text)

    for i in range(1, 4):
        changed_text = spinner.spin_text(original_text)
        print(f"Option {i}:", changed_text)
        original_text = changed_text

if __name__ == "__main__":
    main()
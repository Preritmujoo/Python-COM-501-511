# AIM: Create a text file "MYFILE.TXT" in python and ask the user to write separate 3 lines with three input statements from the user.

def extract_unique_words(file_name):
    unique_words = set()

    try:
        with open(file_name, 'r') as file:
            for line in file:
                words = line.split()

                words = [word.strip('.,!?()[]{}\'"') for word in words]
                words = [word.lower() for word in words]

                unique_words.update(words)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return []

    return sorted(unique_words)

def main():
    file_name = input("Enter the file name: ")
    unique_words = extract_unique_words(file_name)

    if unique_words:
        print("Unique words in alphabetical order:")
        for word in unique_words:
            print(word)

if _name_ == "_main_":
    main()

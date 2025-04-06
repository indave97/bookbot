def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents.split()

def get_num_letters(filepath):
    char_counts = {}  # Empty dictionary to store counts

    with open(filepath) as f:
        file_contents = f.read()

    if file_contents: 
        for char in file_contents:
            # Convert to lowercase
            char = char.lower()
            # Check if character exists in dictionary
            if char in char_counts:
                # If it exists, increment the count
                char_counts[char] += 1
            else:
                # If it doesn't exist, add it with count 1
                char_counts[char] = 1
    return char_counts

def report(filename, words, characters):

    print("============ BOOKBOT ============")
    print("Analyzing book found at", filename, "...")
    print("----------- Word Count ----------")
    print("Found",len(words),"total words")
    print("--------- Character Count -------")

    sorted_characters = sorted(characters.items(), key=lambda x:x[1], reverse=True)
    converted_characters = dict(sorted_characters)
    for character in converted_characters:
        if character.isalpha():
            print(f"{character}: {converted_characters[character]}")


    print("============= END ===============")

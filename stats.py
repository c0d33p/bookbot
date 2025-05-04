def get_num_words(path):
    letters = {}
    with open(path) as f:
        file_contents = f.read()
    content = file_contents.lower()
    word_count = len(content.split())
    for letter in content:
        if letter in letters.keys():
            letters[letter] = letters[letter] + 1
        elif letter.isalpha():
            letters[letter] = 1 
    return letters, word_count

def sort_letters(letters):
    sorted_letters = []
    for letter, num in letters.items():
        item_dict = {'letter': letter, 'num': num}
        sorted_letters.append(item_dict)
    return sorted_letters

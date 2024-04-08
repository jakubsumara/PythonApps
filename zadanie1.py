import json

with open("teksty.json", "r") as file:
    data = json.load(file)

text = " ".join([" ".join(dictionary.values()) for dictionary in data["teksty"]])

def process_text(text):
    text = text.lower()
    words = text.split()
    import string
    translator = str.maketrans("", "", string.punctuation)
    words = [word.translate(translator) for word in words]
    words = [word.capitalize() for word in words]
    words = [word for word in words if "a" in word or "A" in word]
    return words

words = process_text(text)

unique_words = set(words)
word_occurrences = {word: words.count(word) for word in unique_words}

result = {
    "unique_words": list(unique_words),
    "word_occurrences": word_occurrences
}

with open("results.json", "w") as file:
    json.dump(result, file, indent=4)
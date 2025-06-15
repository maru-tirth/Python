def is_pangram(sentence):
    sentence = sentence.lower()  # Convert to lowercase
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in sentence:
            return False
    return True

# Example usage
text = input("Enter a sentence: ")
if is_pangram(text):
    print("It is a pangram.")
else:
    print("It is not a pangram.")

def word_count(sentence):
    return len(sentence.split(" "))

if __name__ == "__main__":
    user_in = input("Enter a sentence: ")
    print(word_count(user_in))
word = input()
sentence = input()
asterisks = f"{'*' * len(word)}"

if word in sentence:
    print(sentence.replace(word, asterisks))

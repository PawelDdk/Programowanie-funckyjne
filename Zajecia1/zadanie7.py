words = ["python", "programowanie", "funkcyjne", "jest", "fajne", "chyba"]

filtered_words = list(filter(lambda x: len(x) > 5, words))

print(filtered_words)

import json
data=json.load(open("data.json"))

word=input("Enter the word you want to search: ")
output=data[word]
print(output)

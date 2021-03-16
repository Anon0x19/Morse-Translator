import json

def Translator_To_English(message):
    text2 = ""
    with open("dictionary.json", "r") as file:
        data = json.load(file)
        temp = message.split(" ")
        for i in temp:
            for j in data:
                if i==data[j]:
                    text2 += j + " "
    file.close()
    return(text2)
import json

def Translator_To_Morse(message):
    text = ""
    with open("dictionary.json", "r") as file:
        data = json.load(file)
        message = message.lower()
        message.replace(" ", "")
        for i in message:
            for j in data:
                if i==j:
                    text += data[j] + " "
    file.close()
    return(text)


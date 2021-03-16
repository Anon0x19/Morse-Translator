from EnglishToMorse import Translator_To_Morse
from MorseToEnglish import Translator_To_English

def main():
    print("""
    Welcome to the Morse code translator
    1) Translate to English
    2) Translate to Morse

    note: Translations to Morse will separate each chracter with a space and when translating to English it will put the entire message together
    """)
    in1 = int(input("Insert the option you'd like to use: "))
    if in1 == 1:
        message = str(input("Insert the message and separate each English character with space: "))
        print(Translator_To_English(message))
    elif in1 == 2:
        message = str(input("Insert the message you want to translate: "))
        print(Translator_To_Morse(message))


if __name__ == "__main__":
    main()
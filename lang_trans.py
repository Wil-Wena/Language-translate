# Translate one language to the other using the translate library!

from translate import Translator
def trans():
    global user_statement
    user_statement =input('Type the statement you want to translate: ')
    print()
    langauge_type = input('Which language will you like to translate it to? ')
    m = langauge_type.lower()
    if m == 'french':
        translator = Translator(to_lang="french")
        trans = translator.translate(user_statement)
    elif m == 'spanish':
        translator = Translator(to_lang="spanish")
        trans = translator.translate(user_statement)
    elif m == 'arabic':
        translator = Translator(to_lang="arabic")
        trans = translator.translate(user_statement)
    elif m == 'hindu':
        translator = Translator(to_lang="hindu")
        trans = translator.translate(user_statement)
    elif m == 'german':
        translator = Translator(to_lang="german")
        trans = translator.translate(user_statement)
    elif m == 'chinese':
        translator = Translator(to_lang="chinese")
        trans = translator.translate(user_statement)
    elif m == 'portugese':
        translator = Translator(to_lang="portugese")
        trans = translator.translate(user_statement)
    elif m == 'english':
        translator = Translator(from_lang="spanish", to_lang="english")
        trans = translator.translate(user_statement)
    else:
        print('Cannot translate your statement into the given language')
    return print(trans)

trans()


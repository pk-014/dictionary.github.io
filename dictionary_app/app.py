import nltk
from nltk.corpus import wordnet
from nltk import pos_tag

def search_word(word):
    synonyms=[]
    antonyms=[]
    definition=''
    examples=''
    pos=''
    try:
        pos=pos_tag([word],tagset='universal')
        syn=wordnet.synsets(word)
        definition=syn[0].definition()
        examples=syn[1].examples()
        for items in syn:
            for i in items.lemmas():
                if word in i.name():
                    continue
                else:
                    synonyms.append(i.name())
                if i.antonyms():
                    antonyms.append(i.antonyms()[0].name())
    except Exception as e:
        print(e)
        
    context={'synonyms':synonyms,'antonyms':antonyms,'definition':definition,'examples':examples,'pos':pos}
    return(context)


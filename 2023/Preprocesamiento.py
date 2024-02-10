# -*- coding: utf-8 -*-
try:
    import nltk
    print("NLTK esta instalado")
except:
    print("NLTK no esta instalado")
    import sys
    sys.exit(1)
'''
import nltk
nltk.download('punkt')
nltk.download('spanish')
'''

#--tokenizar es dividir un texto en palabras o sentencias------------------------------------------------------

oracion = """Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome."""
sentencias= nltk.sent_tokenize(oracion)
for sen in sentencias:
    print(sen)

palabras = nltk.data.load('tokenizers/punkt/spanish.pickle')
oracion = """Hola como esta. Yo bien"""
sentencias= nltk.sent_tokenize(oracion)
for sen in sentencias:
    print(sen)


palabras = nltk.data.load('tokenizers/punkt/spanish.pickle')
oracion = """Hola como esta. Yo bien"""
sentencias= nltk.word_tokenize(oracion)
for palabra in sentencias:
    print(palabra)


palabras = nltk.data.load('tokenizers/punkt/spanish.pickle')
oracion = """Hola como estas. Yo bien"""
token=  nltk.tokenize.regexp_tokenize(oracion, "[\w']+")
for palabra in token:
    print('>>',palabra)

#--Usar las Stopword. Stopword son palabras que no aportan nada al texto.--------------------------------------
''' 
import nltk
nltk.download('stopwords')
'''
#Voy a quitar las stop words
from nltk.corpus import stopwords
sw = stopwords.words('spanish')
print(sw)


oracion = """Hola como esta. Yo bien"""
sentencias= nltk.word_tokenize(oracion)
for palabra in sentencias:
    if palabra.lower() not in sw:
        print('>>', palabra)



#Stemming es el proceso de reducir las palabras a su raíz o base. ----------------------------
from nltk.stem import SnowballStemmer
# Crear una instancia del stemmer para español
stemmer_espanol = SnowballStemmer("spanish")
oracion = """Hola como esta. Yo bien"""
sentencias= nltk.word_tokenize(oracion)
for palabra in sentencias:
        print('>>', stemmer_espanol.stem(palabra))


#Lematizacion es el proceso de convertir una palabra a su forma base. ----------------------------
#ayuda a reducir la dimensionalidad del vocabulario.
import spacy
'''
python -m spacy download es_core_news_sm
Los perros corren por el parque y juegan felices. 
Los el
perros perro
corren correr
por por
el el
parque parque
y y
juegan jugar
felices feliz
'''
nlp = spacy.load('es_core_news_sm')
oracion = """Los perros corren por el parque y juegan felices. Los que corrian antes no eran felices"""
sentencias = nlp(oracion)
print(oracion)
for token in sentencias:
    print(token.text, token.lemma_)



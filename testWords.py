#! /usr/bin/env python3
# coding: utf-8

#from nltk.corpus import stopwords
#nltk.download('stopwords')
import re
import json

with open('stopwordsFr.json', encoding="utf-8") as json_stopwords:
	stopwords_list = json.load(json_stopwords)
print(stopwords_list['stopwords'])
print("################################")
#fr_stops = set(stopwords.words('french'))
#fr_stopsList = stopwords.words('french')
#print(fr_stopsList)
##############
#personal_list = ['il y a tellement de possibilités que je ne sais pas quel mot mettre comme exemple mais où et ou en sont tu ne trouves trouve pas hey salut bonjour grandpy dire']
#custom_stopwords = fr_stopsList + personal_list[0].split()
########################
#test_words = ['où', 'se', 'trouve', 'Paris', 'mais', 'il', 'sans', 'ce', 'et']
test_phrase= ['hey salut grandpy, je cherche la patinoire de Cherbourg ?']
############################
new_string = re.sub(r"[^a-zA-Zéèù-]"," ",test_phrase[0]) #expression régulière pour enlever les caractères spéciaux
print(new_string)
###################
#tri_phrase = test_phrase[0].split()
#print(tri_phrase)
test_phrase_clean = new_string.lower().split()
print(test_phrase_clean)
#print(custom_stopwords)
for word in test_phrase_clean:
	if word not in stopwords_list['stopwords']:
		print(word)


class Parser():
	def __init__(self, question):
		self.question = question

	def parse(self):
		self.special_characters()
		print("la phrase sans caractère spéciaux: ", self.question)
		#self.convert_lower()
		print("la phrase en minuscule: ", self.question)
		#self.convert_list()
		print("les mots restants en liste", self.question)

	def special_characters(self):
		self.question = re.sub(r"[^a-zA-Zéèùû-]"," ",self.question) #expression régulière pour enlever les caractères spéciaux

	def convert_lower(self):
		self.question = self.question.lower()

	def convert_list(self):
		self.question = self.question.split()

question_input = "hey salut grandpy, je cherche la patinoire de Cherbourg ?"
test = Parser(question_input)
test.parse()


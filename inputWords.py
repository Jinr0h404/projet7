#! /usr/bin/env python3
# coding: utf-8

#from nltk.corpus import stopwords
#nltk.download('stopwords')
import re
import json


with open('stopwordsFr.json', encoding="utf-8") as json_stopwords:
	stopwords_list = json.load(json_stopwords)


class Parser():
	def __init__(self, question):
		self.question = question
		self.keyword = []

	def parse(self):
		self.special_characters()
		self.convert_lower()
		self.convert_list()
		self.list_to_keyword()
		return self.keyword

	def special_characters(self):
		"""regular expression to remove special characters"""
		self.question = re.sub(r"[^a-zA-Zéèùû-]"," ",self.question)
		return self.question

	def convert_lower(self):
		self.question = self.question.lower()
		return self.question

	def convert_list(self):
		self.question = self.question.split()
		return self.question

	def list_to_keyword(self):
		""" browse the list and compare it to the stopword to keek only the
		words that are not in"""
		for word in self.question:
			if word not in stopwords_list['stopwords']:
				self.keyword.append(word)
		return self.keyword

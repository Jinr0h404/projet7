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
        #return self.question

    def convert_lower(self):
        self.question = self.question.lower()
        #return self.question

    def convert_list(self):
        self.question = self.question.split()
        #return self.question

    def list_to_keyword(self):
        """ browse the list and compare it to the stopword to keek only the
        words that are not in"""
        for word in self.question:
            if word not in stopwords_list['stopwords']:
                self.keyword.append(word)
        #return self.keyword

class Map():
    def __init__(self):
        self.width="600"
        self.height="450"
        self.style="border:0"
        self.loading="lazy"
        self.allowfullscreen = "allowfullscreen"
        self.src="'https://www.google.com/maps/embed/v1/place?key=AIzaSyDPxv70CaJvHkp4H7QQRYU5o1m7h3R6Cog&q="

    def generate_map(self, keyword):
        """method to generate complete url with keyword from user input for
        resquet google API"""
        for word in keyword:
            """concat keyword and + with the request URL for google API"""
            self.src= self.src + word + "+"
            """remove last + adding by loop and add ' for ending URL"""
        self.src = self.src[:-1] + "'"
        return self.src


#test class and method parse
question_input = 'Salut Grandpy, je veux aller au Louvre'
sut = Parser(question_input)
print(sut.parse())

map = Map()

map.generate_map(sut.keyword)
#! /usr/bin/env python3
# coding: utf-8

#from nltk.corpus import stopwords
#nltk.download('stopwords')
import re
import json
import os
import googlemaps
import wikipedia
gmaps = googlemaps.Client(key="AIzaSyDPxv70CaJvHkp4H7QQRYU5o1m7h3R6Cog")

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

#class Map():
#    def __init__(self):
#        self.width="600"
#        self.height="450"
#        self.style="border:0"
#        self.loading="lazy"
#        self.allowfullscreen = "allowfullscreen"
#        self.src="'https://www.google.com/maps/embed/v1/place?key=AIzaSyDPxv70CaJvHkp4H7QQRYU5o1m7h3R6Cog&q="
#
#    def generate_map(self, keyword):
#        """method to generate complete url with keyword from user input for
#        resquet google API"""
#        for word in keyword:
#            """concat keyword and + with the request URL for google API"""
#            self.src= self.src + word + "+"
#            """remove last + adding by loop and add ' for ending URL"""
#        self.src = self.src[:-1] + "'"
#        return self.src

class Google_position():
    def __init__(self):
        self.latitude = 0
        self.longitude = 0
        self.adresse = ''
        self.position_keyword = {}

    def locate_position(self, input_search):
        for word in input_search.keyword:
            geocode_result = gmaps.geocode(word, region="fr", language="fr")
            if len(geocode_result) > 0 :
                self.position_keyword = {"longitude" : geocode_result[0]["geometry"]["location"]["lng"],
                "latitude" : geocode_result[0]["geometry"]["location"]["lat"],
                "adresse" : geocode_result[0]["formatted_address"]}
                return self.position_keyword
                #print(word," se trouve à une longitude: ",longitude, "et une latitude: ",latitude, "son adresse est: ",adresse)


class Wiki():
    def __init__(self):
        self.title = None
        self.results = 1
        self.radius = 1000

    def wiki_article(self, latitude, longitude):
        article = wikipedia.geosearch(latitude, longitude, title= self.title, results= self.results, radius= self.radius)
        print(article)


#test class and method parse
question_input = 'Salut Grandpy, parle moi de l"arc-de-triomphe'
input_search = Parser(question_input)
input_search.parse()

#map = Map()
#map.generate_map(sut.keyword)
#print(map.src)


position = Google_position()
position.locate_position(input_search)
print(position.position_keyword)

wikipedia.set_lang("fr")
wiki_result = wikipedia.geosearch(48.8737917, 2.2950275, title=None, results=1, radius=1000)
print(wiki_result)
print(wikipedia.summary(wiki_result, sentences=0, chars=0, auto_suggest=True, redirect=True))
wiki_resultb = wikipedia.geosearch(48.85837009999999, 2.2944813, title=None, results=1, radius=1000)[0]
print(wiki_resultb)


article_wiki = Wiki()
latitudeB = 48.8737917
longitudeB = 2.2950275
article_wiki.wiki_article(latitudeB, longitudeB)

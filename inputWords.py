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
        #return self.keyword

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
    def __init__(self, input_search):
        self.latitude = 0
        self.longitude = 0
        self.adresse = ''
        self.input_search = input_search
        self.position_keyword = {}

    def locate_position(self):
        """method to import the latitude and longitude coordinates from
        the gmaps api with the keyword retrieved from the parsed list""" 
        for word in self.input_search.keyword:
            geocode_result = gmaps.geocode(word, region="fr", language="fr")
            if len(geocode_result) > 0 :
                self.position_keyword = {"longitude" : geocode_result[0]["geometry"]["location"]["lng"],
                "latitude" : geocode_result[0]["geometry"]["location"]["lat"],
                "adresse" : geocode_result[0]["formatted_address"]}
                return self.position_keyword


class Wiki():
    def __init__(self):
        self.title = None
        self.results = 1
        self.radius = 1000

    def wiki_article(self, latitude, longitude):
        """method to import information about a place with the latitude and
        longitude coordinates from the gmaps api"""
        wikipedia.set_lang("fr")
        article = wikipedia.geosearch(latitude, longitude, title= self.title, results= self.results, radius= self.radius)[0]
        summary = wikipedia.summary(article, sentences=0, chars=0, auto_suggest=True, redirect=True)
        print(article, summary)



def main():
    #test class and method parse
    question_input = 'Salut Grandpy, parle moi de l"arc-de-triomphe'
    input_search = Parser(question_input)
    input_search.parse()

    #google part
    position = Google_position(input_search)
    position.locate_position()
    print(position.position_keyword)

    #wiki part
    wikipedia.set_lang("fr")
    article_wiki = Wiki()
    article_wiki.wiki_article(position.position_keyword['latitude'], position.position_keyword['longitude'] )


if __name__ == "__main__":
    """execute main function of the file if he is run like main program"""
    main()
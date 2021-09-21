#! /usr/bin/env python3
# coding: utf-8

import re
import json
import googlemaps
import wikipedia
import os
from dotenv import load_dotenv
load_dotenv()
GOOGLEAPIKEY = os.environ.get('GOOGLEAPIKEY')
gmaps = googlemaps.Client(key=GOOGLEAPIKEY)

with open('stopwordsFr.json', encoding="utf-8") as json_stopwords:
    stopwords_list = json.load(json_stopwords)


class Parser():
    """Parser class contains all the methods to parse a sentence"""
    def __init__(self, question):
        self.question = question
        self.keyword = []

    def parse(self):
        self.special_characters()
        self.convert_lower()
        self.convert_list()
        self.list_to_keyword()

    def special_characters(self):
        """regular expression to remove special characters"""
        self.question = re.sub(r"[^a-zA-Zéèùûîïë-]", " ", self.question)

    def convert_lower(self):
        """method to convert all string in lower case"""
        self.question = self.question.lower()

    def convert_list(self):
        """method to convert a sentence in a list of words"""
        self.question = self.question.split()

    def list_to_keyword(self):
        """ browse the list and compare it to the stopword to keek only the
        words that are not in"""
        for word in self.question:
            if word not in stopwords_list['stopwords']:
                self.keyword.append(word)


class Google_position():
    """Google_position class takes words like args and return the latitude and
    the longitude from google maps api"""
    def __init__(self, input_search):
        self.latitude = 0
        self.longitude = 0
        self.adresse = ''
        self.input_search = input_search
        self.position_keyword = {}
        self.status = ""

    def locate_position(self):
        """method to import the latitude and longitude coordinates from
        the gmaps api with the keyword retrieved from the parsed list"""
        # for word in self.input_search.keyword:
        # geocode_result = gmaps.geocode(word, region="fr", language="fr")
        str_keyword = ' '.join(self.input_search.keyword)
        geocode_result = gmaps.geocode(str_keyword, region="fr", language="fr")
        print(geocode_result)
        if len(geocode_result) > 0:
            self.status = "ok"
            self.position_keyword = {
                "longitude":
                    geocode_result[0]["geometry"]["location"]["lng"],
                "latitude":
                    geocode_result[0]["geometry"]["location"]["lat"],
                "adresse": geocode_result[0]["formatted_address"]}
            return self.position_keyword
        else:
            self.status = "not_ok"


class Wiki():
    """Wiki class takes as attribute the wikipedia's api parameters for keep
    the first result"""
    def __init__(self):
        self.title = None
        self.results = 1
        self.radius = 1000
        self.summary = ""
        self.wiki_status = ""

    def wiki_article(self, latitude, longitude):
        """method to import information about a place with the latitude and
        longitude coordinates from the gmaps api"""
        wikipedia.set_lang("fr")
        article = wikipedia.geosearch(
            latitude,
            longitude,
            title=self.title, results=self.results, radius=self.radius)
        if len(article) > 0:
            self.wiki_status = "ok"
            self.summary = wikipedia.summary(
                article,
                sentences=0, chars=0, auto_suggest=True, redirect=True)
            return self.summary
        else:
            self.wiki_status = "not_ok"


def main(user_input):
    """main methode create an instance of the wiki class and the google
    class to return map and wikipedia info to the view"""
    question_input = user_input
    input_search = Parser(question_input)
    input_search.parse()

    # google part
    position = Google_position(input_search)
    position.locate_position()
    if position.status == "ok":
        # wiki part
        wikipedia.set_lang("fr")
        article_wiki = Wiki()
        article_wiki.wiki_article(
            position.position_keyword['latitude'],
            position.position_keyword['longitude'])
        if article_wiki.wiki_status == "ok":
            return {"status": position.status,
                    "wiki": article_wiki.summary,
                    "google_map": position.position_keyword}
        else:
            return {"status": "not_ok"}
    else:
        return {"status": position.status}


if __name__ == "__main__":
    """execute main function of the file if he is run like main program"""
    main()

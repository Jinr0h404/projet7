import inputWords


def test_main_return(mocker):
    question = "arc-de-triomphe"
    mocker.patch(
        "inputWords.googlemaps.client.Client.geocode",
        return_value=[
            {
                "address_components": [
                    {
                        "long_name": "Place Charles de Gaulle",
                        "short_name": "Pl. Charles de Gaulle",
                        "types": ["route"],
                    },
                    {
                        "long_name": "Paris",
                        "short_name": "Paris",
                        "types": ["locality", "political"],
                    },
                    {
                        "long_name": "Département de Paris",
                        "short_name": "Département de Paris",
                        "types": ["administrative_area_level_2", "political"],
                    },
                    {
                        "long_name": "Île-de-France",
                        "short_name": "IDF",
                        "types": ["administrative_area_level_1", "political"],
                    },
                    {
                        "long_name": "France",
                        "short_name": "FR",
                        "types": ["country", "political"],
                    },
                    {
                        "long_name": "75008",
                        "short_name": "75008",
                        "types": ["postal_code"],
                    },
                ],
                "formatted_address":
                "Pl. Charles de Gaulle, 75008 Paris, France",
                "geometry": {
                    "location": {"lat": 48.8737917, "lng": 2.2950275},
                    "location_type": "GEOMETRIC_CENTER",
                    "viewport": {
                        "northeast": {
                            "lat": 48.8751406802915,
                            "lng": 2.296376480291502,
                        },
                        "southwest": {
                            "lat": 48.8724427197085,
                            "lng": 2.293678519708498,
                        },
                    },
                },
                "place_id": "ChIJjx37cOxv5kcRPWQuEW5ntdk",
                "plus_code": {
                    "compound_code": "V7FW+G2 Paris, France",
                    "global_code": "8FW4V7FW+G2",
                },
                "types": [
                    "establishment",
                    "museum",
                    "point_of_interest",
                    "tourist_attraction",
                ],
            }
        ],
    )
    mocker.patch(
        "inputWords.wikipedia.geosearch",
        return_value="Tombe du Soldat inconnu (France)",
    )
    mocker.patch(
        "inputWords.wikipedia.summary",
        return_value="""La tombe du Soldat inconnu est une sépulture installée à Paris sous l'arc de triomphe de l'Étoile depuis le 11 novembre 1920. Elle accueille le corps d'un soldat , mort lors de la Première Guerre mondiale et reconnu français, pour commémorer symboliquement l'ensemble des soldats qui sont morts pour la France au cours de l'histoire. La sépulture, entourée de bornes de métal noir reliées entre elles par des chaînes, se compose d'une dalle de granite de Vire sur laquelle est inscrite l'épitaphe : « Ici repose un soldat français mort pour la Patrie — 1914 - 1918 ». En 1923, une flamme éternelle est ajoutée, ravivée tous les jours. Après la Seconde Guerre mondiale, est installé au pied de la tombe un bouclier de bronze chargé d'un glaive enflammé, offert par les Alliés à la gloire des armées françaises et en mémoire de la libération de Paris. L'expression « dalle sacrée », popularisée par le général Weygand, est utilisée par les associations d'anciens combattants pour désigner le tombeau et sa flamme. La garde du monument est assurée en permanence par un service spécialisé de la Police nationale.""",
    )
    input_search = inputWords.Parser(question)
    position = inputWords.Google_position(input_search)
    position.locate_position()
    article_wiki = inputWords.Wiki()
    article_wiki.wiki_article(
        position.position_keyword['latitude'],
        position.position_keyword['longitude'])
    expected_value = {"status": position.status, "wiki": article_wiki.summary,
                      "google_map": position.position_keyword}
    assert inputWords.main(question) == expected_value

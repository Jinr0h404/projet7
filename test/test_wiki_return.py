import inputWords


def test_wiki_article_return(mocker):
    lat = 48.8737917
    lon = 2.2950275
    mocker.patch(
        "inputWords.wikipedia.geosearch",
        return_value="Tombe du Soldat inconnu (France)",
    )
    mocker.patch(
        "inputWords.wikipedia.summary",
        return_value="""La tombe du Soldat inconnu est une sépulture installée à Paris sous l'arc de triomphe de l'Étoile depuis le 11 novembre 1920. Elle accueille le corps d'un soldat , mort lors de la Première Guerre mondiale et reconnu français, pour commémorer symboliquement l'ensemble des soldats qui sont morts pour la France au cours de l'histoire. La sépulture, entourée de bornes de métal noir reliées entre elles par des chaînes, se compose d'une dalle de granite de Vire sur laquelle est inscrite l'épitaphe : « Ici repose un soldat français mort pour la Patrie — 1914 - 1918 ». En 1923, une flamme éternelle est ajoutée, ravivée tous les jours. Après la Seconde Guerre mondiale, est installé au pied de la tombe un bouclier de bronze chargé d'un glaive enflammé, offert par les Alliés à la gloire des armées françaises et en mémoire de la libération de Paris. L'expression « dalle sacrée », popularisée par le général Weygand, est utilisée par les associations d'anciens combattants pour désigner le tombeau et sa flamme. La garde du monument est assurée en permanence par un service spécialisé de la Police nationale.""",
    )
    article_test = inputWords.Wiki()
    expected_value = """La tombe du Soldat inconnu est une sépulture installée à Paris sous l'arc de triomphe de l'Étoile depuis le 11 novembre 1920. Elle accueille le corps d'un soldat , mort lors de la Première Guerre mondiale et reconnu français, pour commémorer symboliquement l'ensemble des soldats qui sont morts pour la France au cours de l'histoire. La sépulture, entourée de bornes de métal noir reliées entre elles par des chaînes, se compose d'une dalle de granite de Vire sur laquelle est inscrite l'épitaphe : « Ici repose un soldat français mort pour la Patrie — 1914 - 1918 ». En 1923, une flamme éternelle est ajoutée, ravivée tous les jours. Après la Seconde Guerre mondiale, est installé au pied de la tombe un bouclier de bronze chargé d'un glaive enflammé, offert par les Alliés à la gloire des armées françaises et en mémoire de la libération de Paris. L'expression « dalle sacrée », popularisée par le général Weygand, est utilisée par les associations d'anciens combattants pour désigner le tombeau et sa flamme. La garde du monument est assurée en permanence par un service spécialisé de la Police nationale."""
    assert article_test.wiki_article(lat, lon) == expected_value

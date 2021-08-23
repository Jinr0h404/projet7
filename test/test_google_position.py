import inputWords



def test_google_maps_return(mocker):
	input_word = inputWords.Parser('arc-de-triomphe')
	input_word.parse()
	mocker.patch('inputWords.googlemaps.client.Client.geocode', return_value=[{'address_components': [{'long_name': 'Place Charles de Gaulle', 'short_name': 'Pl. Charles de Gaulle', 'types': ['route']}, {'long_name': 'Paris', 'short_name': 'Paris', 'types': ['locality', 'political']}, {'long_name': 'Département de Paris', 'short_name': 'Département de Paris', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'Île-de-France', 'short_name': 'IDF', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'France', 'short_name': 'FR', 'types': ['country', 'political']}, {'long_name': '75008', 'short_name': '75008', 'types': ['postal_code']}], 'formatted_address': 'Pl. Charles de Gaulle, 75008 Paris, France', 'geometry': {'location': {'lat': 48.8737917, 'lng': 2.2950275}, 'location_type': 'GEOMETRIC_CENTER', 'viewport': {'northeast': {'lat': 48.8751406802915, 'lng': 2.296376480291502}, 'southwest': {'lat': 48.8724427197085, 'lng': 2.293678519708498}}}, 'place_id': 'ChIJjx37cOxv5kcRPWQuEW5ntdk', 'plus_code': {'compound_code': 'V7FW+G2 Paris, France', 'global_code': '8FW4V7FW+G2'}, 'types': ['establishment', 'museum', 'point_of_interest', 'tourist_attraction']}])
	google = inputWords.Google_position(input_word)
	expected_value =  {'longitude': 2.2950275, 'latitude': 48.8737917, 'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'}
	assert google.locate_position() == expected_value
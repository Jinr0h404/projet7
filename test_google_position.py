import inputWords



def test_google_maps_return(mocker):
	
	mocker.patch('inputWords.Google_position.locate_position', return_value={'longitude': 2.2950275, 'latitude': 48.8737917, 'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'})

	expected_value =  {'longitude': 2.2950275, 'latitude': 48.8737917, 'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'}
	assert inputWords.Google_position.locate_position() == expected_value


def test_gmaps_return():
	#input_word = ["arc-de-triomphe"]
	input_word = inputWords.Parser('arc-de-triomphe').parse()
	expected_value =  {'longitude': 2.2950275, 'latitude': 48.8737917, 'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'}
	sut = inputWords.Google_position(input_word)
	assert sut.locate_position() == expected_value

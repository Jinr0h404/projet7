import inputWords

def test_google_maps_return(mocker):
	
	def mock_locate_position(self):
		position = {'longitude': 2.2950275,
		'latitude': 48.8737917,
		'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'}

		mocker.patch('inputWords.Google_position.locate_position', mock_locate_position)

		expected_value =  {'longitude': 2.2950275, 'latitude': 48.8737917, 'adresse': 'Pl. Charles de Gaulle, 75008 Paris, France'}
		assert Google_position.locate_position("arc-de-triomphe") == expected_value
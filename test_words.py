import inputWords

def test_return_without_special_characters():
	question = "rolala Il fait super beau! C'est rare, tu es sûr? Oui oui."
	expected_value = "rolala Il fait super beau  C est rare  tu es sûr  Oui oui "
	sut = inputWords.Parser(question)

	assert sut.special_characters() == expected_value

def test_return_lower():
	question = "rolala Il fait super beau  C est rare  tu es sûr  Oui oui "
	expected_value = "rolala il fait super beau  c est rare  tu es sûr  oui oui "
	sut = inputWords.Parser(question)

	assert sut.convert_lower() == expected_value

def test_convert_string_to_list():
	question = "rolala il fait super beau  c est rare  tu es sûr  oui oui "
	expected_value = ['rolala', 'il', 'fait', 'super', 'beau', 'c', 'est', 'rare', 'tu', 'es', 'sûr', 'oui', 'oui']
	sut = inputWords.Parser(question)

	assert sut.convert_list() == expected_value

def test_list_to_keyword():
	list_string = ['rolala', 'il', 'fait', 'super', 'beau', 'c', 'est', 'rare', 'tu', 'es', 'sûr', 'oui', 'oui']
	expected_value = ['rolala', 'sûr']
	sut = inputWords.Parser(list_string)

	assert sut.list_to_keyword() == expected_value
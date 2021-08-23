import inputWords

def test_return_without_special_characters():
	question = "rolala ^ ! / :; Il fait super beau! :) C'est rare, tu es sûr? on va à la tour-effeil!."
	expected_value = ['rolala', 'sûr', 'tour-effeil']
	sut = inputWords.Parser(question)
	sut.parse()
	assert sut.keyword == expected_value

def test_return_lower():
	question = "Rolala Il FAIT super beau  C'est rare!  tu es sûr?  On va à la Tour-Effeil!. "
	expected_value = ['rolala', 'sûr', 'tour-effeil']
	sut = inputWords.Parser(question)
	sut.parse()
	assert sut.keyword == expected_value

def test_final_parse():
	question = "rolala Il fait super beau! C'est rare, tu es sûr? On va à la Tour-effeil!."
	expected_value = ['rolala', 'sûr', 'tour-effeil']
	sut = inputWords.Parser(question)
	sut.parse()
	assert sut.keyword == expected_value
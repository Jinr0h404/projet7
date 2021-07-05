import testWords

def test_return_without_special_characters():
	question = "rolala Il fait super beau! C'est rare, tu es sûr? Oui oui."
	expected_value = "rolala Il fait super  beau  C est rare  tu es sûr  Oui oui"
	sut = testWords.Parser(question)

	assert sut.parse() == expected_value
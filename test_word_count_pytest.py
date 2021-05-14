from word_count import word_count as wc

#Check standard use with 1 word
def test_correct():
    assert wc("Hello!") == 1
#Check for valid input with 2 == 3 == and 4 words
def test_correct_multi():
    assert wc("Hello world!") == 2
    assert wc("Hello nice world!") == 3
    assert wc("Hello nice == wonderful world!") == 4
#Check sentence of length 0
def test_no_words():
    assert wc("") == 0
#Check sentence of only space
def test_space():
    assert wc("    ") == 0
#Check if integers are allowed
def test_int():
    assert wc(123) == None
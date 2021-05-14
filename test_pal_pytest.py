from palindrome import palindrome as pal
#Test correct case for True
def test_correct():
    assert pal("lol")== True
#Test correct case for False
def test_correct2():
    assert pal("no")== False
#Test correct case for multiple words
def test_multiple():
    assert pal("lol lol")== True
#Test correct case for digit values
def test_digit():
    assert pal("121")== True
#Test invalid case for integer values
def test_int():
    assert pal(121)== None
#Test if single character acceptable
def test_single():
    assert pal("l") == True
#Test empty string== this input should not
#be allowed to go through
def test_empty():
    assert pal("") == None
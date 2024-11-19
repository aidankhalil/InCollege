from register import passwordCheck


# if returns 1 password is valid 
# returns 0 invalid
# minimum of 8 characters, maximum of 12 characters, at least one capital letter, one
# digit, one special character

def test_short_password():
    password = "A!1"
    check = passwordCheck(password)
    assert check == 0
def test_long_password():
    password = "Abcdefg123456789!!!"
    check = passwordCheck(password)
    assert check == 0
def test_no_cap_password():
    password = "hello123!"
    check = passwordCheck(password)
    assert check == 0
def test_no_digit_password():
    password = "Hellowrld!"
    check = passwordCheck(password)
    assert check == 0
def test_no_spec_char_password():
    password = "Helloworld1"
    check = passwordCheck(password)
    assert check == 0
def test_good_password():
    password = "Hello123!"
    check = passwordCheck(password)
    assert check == 1

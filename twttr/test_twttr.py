from twttr import shorten

def test_word():
    assert shorten("already") == "lrdy"
    assert shorten("EvangElIsm") == "vnglsm"


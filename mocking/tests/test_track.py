from lib.track import *

def test_can_see_properties_of_track():
    track1 = Track("I like you", "Post Malone")
    assert track1.title == "I like you"
    assert track1.artist == "Post Malone" 

def test_matches():
    track1 = Track("I like you", "Post Malone")
    track2 = Track("44 bars", "Logic")
    assert track1.matches("like")
    assert track1.matches("Post")

def test_partial_match_in_title():
    track1 = Track("I like you", "Post Malone")
    assert track1.matches('li')

def test_partial_match_in_artist():
    track1 = Track("I like you", "Post Malone")
    assert track1.matches('os')

def test_keyword_not_in_title_or_artist():
    track1 = Track("I like you", "Post Malone")
    assert track1.matches('x') == False
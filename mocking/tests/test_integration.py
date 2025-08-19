from lib.music_library import *
from lib.track import *

def test_can_add_track_to_library():
    music_library = MusicLibrary()
    track1 = Track("I like you", "Post Malone")
    music_library.add(track1)
    assert music_library.tracks == [track1]

def test_can_search_with_keyword():
    music_library = MusicLibrary()
    track1 = Track("I like you", "Post Malone")
    track2 = Track("44 bars", "Logic")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search("like") == [track1]

def test_no_results_from_search():
    music_library = MusicLibrary()
    track1 = Track("I like you", "Post Malone")
    track2 = Track("44 bars", "Logic")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search("hate") == []

def test_keyword_partial_match_in_search():
    music_library = MusicLibrary()
    track1 = Track("I like you", "Post Malone")
    track2 = Track("44 bars", "Logic")
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.search("li") == [track1]

def test_keyword_partial_match_both_tracks_in_search():
    music_library = MusicLibrary()
    track1 = Track("I like you", "Post Malone")
    track2 = Track("44 bars", "Logic")
    track3 = Track("Live a little", "Karan")
    music_library.add(track1)
    music_library.add(track2)
    music_library.add(track3)
    assert music_library.search("li") == [track1,track3]
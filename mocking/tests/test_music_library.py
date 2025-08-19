from lib.music_library import *
from unittest.mock import Mock
import pytest

def test_library_initially_empty():
    music_library = MusicLibrary()
    assert music_library.tracks == []

def test_can_search_with_keyword_using_fake_classes():
    music_library = MusicLibrary()
    track1 = FakeMatchingTrack()
    track2 = FakeNotMatchingTrack()
    
    music_library.add(track1)
    music_library.add(track2)
    
    assert music_library.search("like") == [track1]


class FakeMatchingTrack():
    def matches(self,keyword):
        return True
    
class FakeNotMatchingTrack():
    def matches(self,keyword):
        return False
    
def test_can_search_with_keyword_using_mock_classes():
    music_library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()

    track1.matches.return_value = True
    track2.matches.return_value = False
    
    music_library.add(track1)
    music_library.add(track2)
    
    assert music_library.search("like") == [track1]

def test_can_add_tracks_and_list():
    music_library = MusicLibrary()
    track1 = Mock()
    track2 = Mock()
    music_library.add(track1)
    music_library.add(track2)
    assert music_library.tracks == [track1,track2]
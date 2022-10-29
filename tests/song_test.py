import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Highway to hell", "Rock", 100)
        self.song_2 = Song("The House of the Rising Sun", "Rock", 200)
        self.song_3 = Song("Ain't No Rest for the Wicked", "Rock", 180)
        self.song_4 = Song("Levitating", "Pop", 50)
        self.song_5 = Song("Before you go", "Pop", 190)
        self.song_6 = Song("Bad habits", "Pop", 70)


    def test_song_has_song_title(self):
        self.assertEqual("Before you go", self.song_5.song_title)


    def test_song_has_genre(self):
        self.assertEqual("Pop", self.song_6.genre)


    def test_song_has_difficulty(self):
        self.assertEqual(200, self.song_2.difficulty)




import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Highway to hell", "Rock", 100)
        self.song_2 = Song("The House of the Rising Sun", "Rock", 200)
        self.song_3 = Song("Ain't No Rest for the Wicked", "Rock", 180)
        self.song_4 = Song("Levitating", "Pop", 50)
        self.song_5 = Song("Before you go", "Pop", 190)
        self.song_6 = Song("Bad habits", "Pop", 70)
        self.song_7 = Song("Rock of Ages", "Rock", 85)
        self.song_8 = Song("I kissed a girl", "Pop", 40)

        self.guest_1 = Guest("Luis", 100, "Bad habits", 560.20)
        self.guest_2 = Guest("Gintare", 160, "Ain't No Rest for the Wicked", 549.30)
        self.guest_3 = Guest("Cordu", 140, "Highway to hell", 559.80)
        self.guest_4 = Guest("Kaija", 210, "The House of the Rising Sun", 539.10)
        self.guest_5 = Guest("Oliwia", 150, "Bad habits", 545.90)
        self.guest_6 = Guest("Alistair", 180, "Levitating", 563.20)

        
        self.rock_mix = []
        self.pop_mix = []
        

        self.room_1 = Room("Rock", self.rock_mix, 5, 100.00)
        self.room_2 = Room("Pop", self.pop_mix, 8, 150.60)


    def test_room_name(self):
        self.assertEqual("Rock", self.room_1.name)


    def test_room_has_a_mix(self):
        self.assertEqual(0, len(self.room_1.mix))

    def test_add_song_to_mix(self):
        self.rock_mix.add_song_to_mix(self.song_1)
        # self.rock_mix.append(self.song_1)
        self.assertEqual(1, len(self.room_1.mix))
    

    def test_room_capacity(self):
        self.assertEqual(8, self.room_2.capacity)


    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)



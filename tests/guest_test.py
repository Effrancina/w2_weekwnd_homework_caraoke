import unittest
from src.guest import Guest
from src.song import *

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest_1 = Guest("Luis", 100, "Bad habits", 560.20)
        self.guest_2 = Guest("Gintare", 160, "Ain't No Rest for the Wicked", 549.30)
        self.guest_3 = Guest("Cordu", 140, "Highway to hell", 559.80)
        self.guest_4 = Guest("Kaija", 210, "The House of the Rising Sun", 539.10)
        self.guest_5 = Guest("Oliwia", 150, "Bad habits", 545.90)
        self.guest_6 = Guest("Alistair", 180, "Levitating", 563.20)
        
    def test_guest_name(self):
        self.assertEqual("Alistair", self.guest_6.name)


    def test_guest_skill_level(self):
        self.assertEqual(210, self.guest_4.skill_level)


    def test_guest_favourite_song(self):
        self.assertEqual("Ain't No Rest for the Wicked", self.guest_2.favourite_song)
    

    def test_guest_has_money(self):
        self.assertEqual(545.90, self.guest_5.wallet)


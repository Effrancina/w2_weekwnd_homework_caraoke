class Room:
    def __init__(self, name, mix, capacity, till):
        self.name = name
        self.mix = mix
        self.capacity = capacity
        self.till = till
        

    def add_song_to_mix(self, song_to_add):
        self.room.mix_1.append(song_to_add)

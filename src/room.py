class Room:
    def __init__(self, name, capacity, till):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.mix = []
        self.singers = []
        
    def add_song_to_room(self, song):
        self.mix.append(song)
   

    def check_singer_in_to_room(self, singer):
        if self.singers.__len__() <= 7:
            self.singers.append(singer)
        else:
            print("Apologies, this room is full at the moment.")

    def check_singer_out_of_room(self, singer):
        if self.singers.__len__() >= 1:
            self.singers.pop(singer)
            print("Bye bye!")
        elif self.singers.__len__() == 0:
            print("Everyone already left, silly!")
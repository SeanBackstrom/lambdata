

#Creates a song class to instantiate song objects
class Song:
    def __init__(self, tempo, genre):
        self.tempo = tempo
        self.genre = genre

    #Song method for user to print stats
    def songstats(self):
        print("The song tempo is ", self.tempo,
        "and the genre is ", self.genre)

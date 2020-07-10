import unittest
from songclass import Song

class SongTests(unittest.TestCase):

    def test_istempoint(self):
        """test the tempo is an integer."""
        
        song1 = Song(135, 'Rock')

        self.assertEqual(type(song1.tempo), int)



if __name__ == '__main__':
    #this conditional is for code that will be run
    #when we execute our file from the command line
    unittest.main()
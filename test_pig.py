import unittest
import pig


class GeneralTesting(unittest.TestCase):
    
    def test_Player(self):
        test1 = pig.Player('connor')
        self.assertEqual(test1.name, 'connor')
        self.assertEqual(test1.turn_total, 0)
        self.assertEqual(test1.overall_total, 0)

    def test_Die(self):
        test1 = pig.Die()
        roll = test1.roll()
        self.assertIsInstance(roll, int)

    def test_Turn(self):
        die = pig.Die()
        players = (pig.Player('one'), pig.Player('two'))
        test = pig.Game(die, players)
        self.assertEqual(test.turn(players[0]), 'Player one — current game total:0')
    



if __name__ == '__main__':

    unittest.main()
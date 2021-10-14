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

    def test_GamePlayerCount(self):
        test1 = pig.Game()
        test2 = pig.Game(5)
        self.assertEqual(test1.players, 2)
        self.assertEqual(test2.players, 5)
    
    def test_GamePlay(self):
        test1 = pig.Game()
        self.assertEqual(test1.play(), "one")


if __name__ == '__main__':

    unittest.main()
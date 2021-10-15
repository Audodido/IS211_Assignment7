
class Test:

    def __init__(self):

        self.totals = [0, 0, 0]

    def is_game_over(self):
        for t in self.totals:
            print(t)
            if t >= 20:
                return True
            else:
                return False

t = Test()

while not t.is_game_over():
    print(t.totals)
    t.totals[0] += 1
    t.totals[1] += 2

print("done")





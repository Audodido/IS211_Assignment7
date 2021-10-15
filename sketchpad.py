
class Test:

    def __init__(self):

        self.totals = [0, 3, 0]

    def is_game_over(self):
        for t in range(len(self.totals)):
            print(self.totals[t])
            if self.totals[t] >= 20:
                return True
        else:
            return False

t = Test()

# t.is_game_over()

while not t.is_game_over():
    t.totals[2] += 3
    t.totals[0] += 1
    print(t.totals)

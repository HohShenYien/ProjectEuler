# Maps each number to value
nums = {str(i): i for i in range(2, 10)}
nums.update({"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14})
# Maps the signs to value
signs = {"D": 1, "C": 2, "H": 3, "S": 4}

class Poker:
    def __init__(self, hand: "[str]"):
        # Turn the cards into purely numbers and sort it for easier manipulation
        self.hand = [(nums[card[0]], signs[card[1]]) for card in hand]
        self.hand.sort()

        # Checking all possible combinations
        self.check234()
        self.checkStraight()
        self.checkFlush()

    def check234(self):
        # Counts the numbers and place the card with largest sign into
        # suitable list
        notPair = self.hand.copy()
        self.pairs = []
        self.triple = []
        self.four = []

        count = 1
        for i in range(1, 5):
            if self.hand[i][0] == self.hand[i - 1][0]:
                count += 1
            else:
                if count == 2:
                    # Remove pairs, to be used for largest
                    notPair.remove(self.hand[i - 1])
                    notPair.remove(self.hand[i - 2])
                    self.pairs.append(self.hand[i - 1])
                elif count == 3:
                    self.triple.append(self.hand[i - 1])
                elif count == 4:
                    self.four.append(self.hand[i - 1])
                count = 1

        # For final element
        if count == 2:
            notPair.remove(self.hand[i ])
            notPair.remove(self.hand[i - 1])
            self.pairs.append(self.hand[i])
        elif count == 3:
            self.triple.append(self.hand[i])
        elif count == 4:
            self.four.append(self.hand[i])
        self.largest = notPair[-1]

    def checkStraight(self):
        # Checking consecutive, a bit tricky on 'wheel' straight i.e A2345
        # Luckily straight is not cyclic
        # I am dealing with wheel by adding a '1' if last card is A and first card is 2
        self.straight = []
        tmp = self.hand
        if tmp[-1][0] == 14 and tmp[0][0] == 2:
            tmp = [(1, 0)] + tmp[:-1]

        for i in range(1, 5):
            if tmp[i][0] != tmp[i - 1][0] + 1:
                return

        self.straight.append(tmp[-1])

    def checkFlush(self):
        # Check if all cards are in the same sign,
        # If yes, then get the largest card
        self.flush = []
        tmp = self.hand[0][1]
        for _, sign in self.hand[1:]:
            if sign != tmp:
                return

        self.flush.append(self.hand[-1])

    def helper(self, selfA, thatA, selfB=True, thatB=True, key=0):
        if selfA and selfB:
            if thatA and thatB:
                # Both have the same combination, so check which one is larger
                if key == None:
                    return selfA > thatA
                # For pairs: make sure different number
                if selfA[0][key] != thatA[0][key]:
                    return selfA[0][key] > thatA[0][key]
            else:
                # self has but that doesn't
                return True
        elif thatA and thatB:
            # that has but self doesn't
            return False

        return None

    def __gt__(self, that):
        # Time for comparison!!!
        # All have similar logic
        # Up to some point I realized I could simplify the codes with a helper function....
        # Then I realized I could further simplify using a list, but that'll be less readable so nvm
        # Checking from royal flush to highest

        # Royal flush and straight flush together
        tmp = self.helper(self.flush, that.flush, self.straight, that.straight, None)
        if tmp != None:
            return tmp

        # four of a kind
        tmp = self.helper(self.four, that.four)
        if tmp != None:
            return tmp

        # Full house
        tmp = self.helper(self.triple, that.triple, self.pairs, that.pairs)
        if tmp != None:
            return tmp

        # Flush
        tmp = self.helper(self.flush, that.flush, key=None)
        if tmp != None:
            return tmp

        # Straight
        tmp = self.helper(self.straight, that.straight, key=None)
        if tmp != None:
            return tmp

        # Three
        tmp = self.helper(self.triple, that.triple)
        if tmp != None:
            return tmp

        # 2 pairs
        if len(self.pairs) == 2:
            if len(that.pairs) == 2:
                # Check from larger pair
                for i in [1, 0]:
                    if self.pairs[i][0] != that.pairs[i][0]:
                        return self.pairs[i][0] > that.pairs[i][0]

            else:
                return True
        elif len(that.pairs) == 2:
            return False

        # 1 pair
        tmp = self.helper(self.pairs, that.pairs)
        if tmp != None:
            return tmp

        # largest element
        return self.largest > that.largest

res = 0
with open("p054_poker.txt", "r") as f:
    for line in f.readlines():
        hand = line.split(" ")
        p1 = Poker(hand[:5])
        p2 = Poker(hand[5:])
        res += (p1 > p2)

print(res)

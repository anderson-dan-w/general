#!/usr/local/bin/python3
import collections

order = list("23456789TJQKA")
suits = list("SCDH")

class Hand(object):
    (STRAIGHT_FLUSH, FOUR, FULL_HOUSE, FLUSH, STRAIGHT, THREE,
     TWO_PAIR, PAIR, HIGH) = range(8, -1, -1)
    def __init__(self, cards):
        self.cards = cards
        self.numbers = [card[0] for card in self.cards]
        self.suits = [card[1] for card in self.cards]
        self.counts = collections.Counter(self.numbers)
        self.indices = sorted(order.index(n) for n in self.numbers)
        self.value = self.setHandValue()

    def __str__(self):
         return "Hand({}) - {}".format(" ".join(self.cards),
                self.description())

    def description(self):
        descr = ""
        names = ["High", "Pair", "Two Pair", "Three", "Straight",
                 "Flush", "Full House", "Four", "Straight Flush"]
        descr += names[self.value]
        ordered_cards = [order[n] for n in self.comparisonKey()[1:]]
        if self.value in (self.FULL_HOUSE, self.TWO_PAIR):
            descr += " {} {}".format(*ordered_cards[:2])
            if self.value == self.TWO_PAIR:
                descr += " and {} high".format(ordered_cards[2])
        elif not self.value == self.HIGH:
            descr += " {}".format(ordered_cards[0])
            descr += " and {} high".format(ordered_cards[1])
        else:
            descr += " {}".format(ordered_cards[0])
        return descr

    def comparisonKey(self):
        key = [self.value]
        ordered_cards =sorted(self.counts, key=lambda n: (self.counts[n],
                            order.index(n)), reverse=True)
        key += [order.index(c) for c in ordered_cards]
        return key

    def setHandValue(self):
        if self.isStraightFlush():
            return self.STRAIGHT_FLUSH
        if self.isFourOfAKind():
            return self.FOUR
        if self.isFullHouse():
            return self.FULL_HOUSE
        if self.isFlush():
            return self.FLUSH
        if self.isStraight():
            return self.STRAIGHT
        if self.isThreeOfAKind():
            return self.THREE
        if self.isTwoPair():
            return self.TWO_PAIR
        if self.isPair():
            return self.PAIR
        return self.HIGH

    def isFlush(self):
        return len(set(self.suits)) == 1

    def isStraight(self):
        if len(set(self.numbers)) != len(self.numbers):
            return False
        return (self.indices[-1] - self.indices[0]) == (len(self.numbers) - 1)

    def isStraightFlush(self):
        return self.isFlush() and self.isStraight()

    def isMultiples(self, n):
        return n in self.counts.values()

    def isFourOfAKind(self):
        return self.isMultiples(4)

    def isThreeOfAKind(self):
        return self.isMultiples(3)

    def isPair(self):
        return self.isMultiples(2)

    def isTwoPair(self):
        return sum(1 for v in self.counts.values() if v == 2) == 2

    def isFullHouse(self):
        return self.isThreeOfAKind() and self.isPair()

wins = 0
with open("poker.txt") as fh:
    lines = fh.read().split("\n")

for line in lines:
    cards = line.split(" ")
    if len(cards) != 10:
        continue
    first = Hand(cards[:5])
    second = Hand(cards[5:])
    if first.comparisonKey() > second.comparisonKey():
        wins += 1
        print("{} beats {}".format(first, second))
    else:
        print("{} lost to {}".format(first, second))

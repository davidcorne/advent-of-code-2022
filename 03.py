#!py -3

import unittest

def priority(item):
    pass

def common_item(rucksack):
    pass

def sum_of_priorities(backpacks):
    pass

def main():
    with open("03-input.txt", "r") as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    print(sum_of_priorities(lines))

class ThreeTester(unittest.TestCase):

    def test_common_item(self):
        ruck_1 = 'vJrwpWtwJgWrhcsFMMfFFhFp'
        self.assertEqual(common_item(ruck_1), 'p')
        ruck_2 = 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'
        self.assertEqual(common_item(ruck_2), 'L')
        ruck_3 = 'PmmdzqPrVvPwwTWBwg'
        self.assertEqual(common_item(ruck_3), 'P')
        ruck_4 = 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'
        self.assertEqual(common_item(ruck_4), 'v')
        ruck_5 = 'ttgJtRGJQctTZtZT'
        self.assertEqual(common_item(ruck_5), 't')

    def test_priorities(self):
        self.assertEqual(priority('p'), 16)
        self.assertEqual(priority('L'), 38)
        self.assertEqual(priority('P'), 42)
        self.assertEqual(priority('v'), 22)
        self.assertEqual(priority('t'), 20)
        self.assertEqual(priority('s'), 19)

    def test_sum(self):
        rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw',
            ]
        self.assertEqual(sum_of_priorities(rucksacks), 157)

unittest.main(exit=False)
main()

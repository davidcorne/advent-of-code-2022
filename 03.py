#!py -3

import unittest

def priority(item):
    # Is there a better way of doing this? upper and lower case are opposite to ascii so ord doesn't help
    return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(item) + 1

def common_item(rucksack):
    assert len(rucksack) % 2 == 0
    compartment_1 = rucksack[0:len(rucksack) // 2]
    compartment_2 = rucksack[len(rucksack) // 2:]
    assert rucksack == compartment_1 + compartment_2
    set_1 = set(compartment_1)
    set_2 = set(compartment_2)
    common = set_1.intersection(set_2)
    assert len(common) == 1
    return common.pop()

def find_badge(backpack_1, backpack_2, backpack_3):
    set_1 = set(backpack_1)
    set_2 = set(backpack_2)
    set_3 = set(backpack_3)
    badge = set_1.intersection(set_2, set_3)
    assert len(badge) == 1
    return badge.pop()

def sum_of_badges(backpacks):
    assert len(backpacks) % 3 == 0
    badges = []
    for i in range(len(backpacks) // 3):
        start = 3 * i
        badges.append(find_badge(backpacks[start], backpacks[start+1], backpacks[start+2]))
    return sum(priority(b) for b in badges)

def main():
    with open("03-input.txt", "r") as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    print(sum_of_badges(lines))

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

    def test_find_badge(self):
        badge = find_badge('vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg')
        self.assertEqual(badge, 'r')
        badge = find_badge('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw')
        self.assertEqual(badge, 'Z')
    
    def test_sum(self):
        rucksacks = ['vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg',
            'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
            'ttgJtRGJQctTZtZT',
            'CrZsJsPPZsGzwwsLwLmpwMDw',
            ]
        self.assertEqual(sum_of_badges(rucksacks), 70)

unittest.main(exit=False)
main()

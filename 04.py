#!py -3

import unittest

def string_to_assignment_set(assignment):
    start, end = assignment.split('-')
    start = int(start)
    end = int(end)
    assert start <= end
    return set(range(start, end + 1))

def find_assignments(line):
    assignments = line.split(',')
    assert len(assignments) == 2
    return string_to_assignment_set(assignments[0]), string_to_assignment_set(assignments[1])

def contained_assignment(line):
    assignments_1, assignments_2 = find_assignments(line)
    return assignments_1.issubset(assignments_2) or assignments_2.issubset(assignments_1)

def count_contained_assignments(lines):
    current_count = 0
    for line in lines:
        if contained_assignment(line):
            current_count += 1
    return current_count

def main():
    with open("04-input.txt", "r") as input_file:
        lines = [l.strip() for l in input_file.readlines()]
    print(count_contained_assignments(lines))

class FourTester(unittest.TestCase):

    def test_string_to_assignment(self):
        assignment_set = string_to_assignment_set('44-44')
        self.assertEqual(assignment_set, {44})

    def test_assignments(self):
        line = "2-4,6-8"
        assignments_1, assignments_2 = find_assignments(line)
        self.assertEqual(assignments_1, {2,3,4})
        self.assertEqual(assignments_2, {6,7,8})
        line = "22-30,1-2"
        assignments_1, assignments_2 = find_assignments(line)
        self.assertEqual(assignments_1, {22,23,24,25,26,27,28,29,30})
        self.assertEqual(assignments_2, {1,2})

    def test_contained_assignment(self):
        non_contained = '2-4,6-8'
        self.assertFalse(contained_assignment(non_contained))
        contained = '2-8,3-7'
        self.assertTrue(contained_assignment(contained))

    def test_count_contained_assignments(self):
        lines = [
            '2-4,6-8',
            '2-3,4-5',
            '5-7,7-9',
            '2-8,3-7',
            '6-6,4-6',
            '2-6,4-8'
        ]
        self.assertEqual(count_contained_assignments(lines), 2)

unittest.main(exit=False)
main()

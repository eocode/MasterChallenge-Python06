def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def divider(number):
        assert type(number) == int, "Only numbers"
        return number / n
    return divider


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):

        def setUp(self):
            self.division = [5, 3, 15, "15"]

        def test_closure_make_division_by(self):
            division = make_division_by(self.division[1])
            self.assertEqual(self.division[0], division(self.division[2]))

    # unittest.main()
    run()

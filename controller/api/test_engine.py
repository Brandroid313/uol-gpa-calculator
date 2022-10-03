# ------------------------------ Imports (Start) ------------------------------

# Native modules
import unittest

# Third party modules

# Custom modules
import engine

# ------------------------------ Imports (End) --------------------------------

# ------------------------------ Classes (Start) ------------------------------


class APITest(unittest.TestCase):

    def test_connect_algo_to_db(self):
        """Scenario: Connect algorithm to database

        Given algo_request <- 1
        And db_response <- 2
        Then connect_algo_to_db(algo_request, db_request) = 2
        """

        algo_request = 1
        db_response = 2

        result = False
        if engine.connect_algo_to_db(algo_request, db_response) == 1:
            result = True

        self.assertEqual(True, result)

    def test_connect_db_to_algo(self):
        """Scenario: Connect database to algorithm

        Given db_request <- 1
        And algo_response <- 2
        Then connect_db_to_algo(db_request, algo_response) = 2
        """

        db_request = 1
        algo_response = 2

        result = False
        if engine.connect_db_to_algo(db_request, algo_response) == 1:
            result = True

        self.assertEqual(True, result)


# ------------------------------ Classes (End) --------------------------------

# ------------------------------ Auto-Execute (Start) -------------------------

# The easiest way to run unittest tests is to include this at the bottom of
# each test file
if __name__ == "__main__":
    unittest.main()

# ------------------------------ Auto-Execute (End) ---------------------------

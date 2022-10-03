import unittest
import algo
import alg_sand
import utility

dic_List_level_4 = [
    {'grade': 75,
     'weight': 1,
     'credits': 15
     },

    {'grade': 75,
     'weight': 1,
     'credits': 15
     },

    {'grade': 75,
     'weight': 1,
     'credits': 15
     }
]

dic_List_mult_levels = [
    {'grade': 75,
     'weight': 1,
     'credits': 15
     },

    {'grade': 75,
     'weight': 1,
     'credits': 15
     },

    {'grade': 75,
     'weight': 1,
     'credits': 15
     },

    {'grade': 75,
     'weight': 3,
     'credits': 15
     },

    {'grade': 75,
     'weight': 3,
     'credits': 15
     },

    {'grade': 75,
     'weight': 3,
     'credits': 15
     },

    {'grade': 75,
     'weight': 5,
     'credits': 15
     }
]

dic_List_onTarget_test = [
    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     }
]
# This dictionary assumes 6 classes total in the degree, 2 at each level; two
# are ' missing'
# One from level 5 and one from level 6
dic_List_onTarget_test_2 = [
    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },
]

dic_List_onTarget_test_full_course = [
    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 1,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 3,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },

    {'grade': 100,
     'weight': 5,
     'credits': 15
     },
]


class TestForAlgo(unittest.TestCase):
    def test_list_of_dictionaries_sum_and_divde_by_credits(self):
        res = algo.degree_gpa(dic_List_level_4)
        self.assertEqual(res, 75)

    def test_list_of_dictionaries_multiple_levels(self):
        res = algo.degree_gpa(dic_List_level_4)
        self.assertEqual(res, 75)

    def test_onTarget_various_weights(self):  # This test assumes one class at each level, and level 5 is missing
        res = alg_sand.targetGrade(dic_List_onTarget_test, 80)
        self.assertEqual(res, 64)

    def test_onTarget_missing_weights(self):  # This test assumes 2 classes at each level, and handles multiple missing classes from various levels
        res = alg_sand.targetGrade_2(dic_List_onTarget_test_2, 80)
        self.assertEqual(res, 55)

    def test_onTarget_full_course(self):  # Test over a full courseload, missing the final
        res = algo.on_target(dic_List_onTarget_test_full_course, 100)
        self.assertEqual(res, 100)

    def test_onTarget_grade_not_possible(self):  # Test over a full courseload, missing the final
        res = algo.on_target(dic_List_onTarget_test_full_course, 120)
        self.assertEqual(res, "Grade not possible, enter a lower target grade")

    def test_utility_algo_returns_list(self):  # Test over a full courseload, missing the final
        res = utility.make_dict(75, 1, 15)
        self.assertEqual(res, dic_List_level_4[0])

    def test_module_grade_calc_cooursework_and_final_only(self):
        res = algo.module_grade(80, 50, 100, 50)
        self.assertEqual(res, 90)


unittest.main(argv=['ignored', '-v'], exit=False)

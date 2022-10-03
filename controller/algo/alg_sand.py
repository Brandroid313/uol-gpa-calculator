from decimal import Decimal, getcontext

### Below are the Test functions used/iterated over to pass unittests to
# devlop functions above ###


def targetGrade(grades_dict, target):
    """ Test function for the on Target feature; an early iteration proof of concept;
        Calculates the grades needed to achieve the target grade

    Args:
        grades_dict (Python List of dictionaries; integers): The List contains dictionaries,
        which in turn contain the values of Grade, weight and credits for each class taken

        target (integer): [The desired target grade the student wants to achieve]

    Returns:
        [integer]: [A single integer value representing the
         grades needed to achive the target grade]
    """
    gradeIn = 0
    for i in range(len(grades_dict)):
        gradeIn = gradeIn + grades_dict[i]['grade'] * grades_dict[i]['weight']
    # Need to multiple (the total credits for degree * their weights sum) to target grade
    # Need to divide by the weights of the classes left that haven't been taken
    gradeOut = ((9 * target) - gradeIn) / 5 # Nine is the sum of the weights for all classes, 5 is the weight of the leftover class not yet taken
    return gradeOut

# Mock degree with only 6 total classes, two in each level
def targetGrade_2(grades_dict, target):
    """ Test function for the on Target feature; an early iteration proof of conept;
        Calculates the grades needed to achieve the target grade, with 6 classes or
        2 classes at each level; was testing if it could get thr correct missing weights
        of classes not taken

    Args:
        grades_dict ([Python List of dictionaries; integers]): [The List contains dictionaries, 
        which in turn contain the values of Grade, weight and credits for each class taken]

        target ([integer]): [The desired target grade the student wants to achieve]

    Returns:
        [integer]: [A single integer value representing the 
         grades needed to achive the target grade]
    """
    gradeIn = 0
    total_credits_in_degree = 270 # this is the mock class version with only 6 classes total
    total_classes_degree = total_credits_in_degree / 15
    credits_taken = 0
    for i in range(len(grades_dict)):
        gradeIn = gradeIn + grades_dict[i]['grade'] * grades_dict[i]['weight']
        credits_taken = credits_taken + grades_dict[i]['credits'] * grades_dict[i]['weight']
    # Need to multiple (the total credits for degree * their weights sum) to target grade
    # Need to divide by the weights of the classes left that haven't been taken
    missing_weights_sum = (total_credits_in_degree - credits_taken) / 15
    gradeOut = ((total_classes_degree * target) - gradeIn) / missing_weights_sum # Nine is the sum of the weights for all classes, 5 is the weight of the leftover class not yet taken
    return gradeOut

def dmmy(arg1, arg2):
    """[summary]

    Args:
        arg1 ([type]): [description]
        arg2 ([type]): [description]

    Returns:
        [type]: [description]
    """
    argNew = arg1 + arg2
    return argNew

    def make_dict(grades, weight, credits):
        """makes a dict from the data given to pass into a list

        Args:
            grade (int): grade from the database
            weight (int): the weight of the class
            credits (int): the unwieghted credits for the class
            the credits should be 15 per class, 30 for the final
        """
        new_dict = {"grade": grades,
                    "weight": weight,
                    "credits": credits}
        return new_dict

def module_grade(coursework1, weight_1, coursework2, weight_2):
    """takes the grades of a module and calculates grade earned

       Will take the overall coursework grade earned, and the weight
       of that courserwork, as well as the final ( or second coursework)
       and returns the final grade earned for class. Coursework1 should
       contain the total earned from the combined score of midterms and quizzes

    Args:
        coursework1 (int): an integer that represents the grade
         earned in the first coursework
        weight_1 (int): the total percentage that the courserwork1 is
         worth for that class
        courserwork2 (int): Usually the final exam or project; the final grade
         earned for the module
        weight_2 ([type]): The total percentage of the class that
         coursework2 is worth for that class
    """

    getcontext().prec = 2

    first_coursework = ( Decimal(weight_1) / Decimal(100) ) * Decimal(coursework1)

    second_coursework = ( Decimal(weight_2) / Decimal(100) ) * Decimal(coursework2)

    grade = first_coursework + second_coursework

    return grade

gr = module_grade(80, 50, 100, 50)
print(gr)



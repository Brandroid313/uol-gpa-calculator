# Fantastic functions and where to find them

## Grade Calculation functions 
Can be found in the algo.py folder. The path is controller > algo > algo.py

### degree_gpa 
This function takes a list of dictionaries and outputs the gpa earned so far in the degree. Note that the grade that is produced is for the overall degree as a whole.

Each dictionary in the list should contain the grade, weight and credits associated with that class.

Example data structure the function takes 
~~~python 

example_dict = [
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

~~~

The function 

~~~python 
def degree_gpa(dic_List):
    """ Calculates the current gpa, as a percentage, with the grades so far

    Args:
        dic_List (Python List of dictionaries; integers):
        The List contains dictionaries,
        which in turn contain the values of Grade, weight and credits for each
        class taken

    Returns:
        integer: Returns an intger value, between 0 ~ and 100, that is the
        percatage value
        representing the overall grade for the degree so far; if all classe
        taken, the grade earned
        if not, then what the current grade standing is
    """
    gpa = 0
    credits = 0
    for i in range(len(dic_List)):
        gpa = gpa + dic_List[i]['grade'] * dic_List[i]['weight']
        credits = credits + dic_List[i]['credits'] * dic_List[i]['weight']
    credits = credits / 15
    gpa = gpa / credits
    return gpa

~~~

### module_grade
This function takes the courework 1 and coursework 2 grades and their percentages of that module, and ouputs the grade earned in that module

The arguments are the coursework 1 grade ( which includes all graded coursework and the midterm) and the coursework 2 grade ( which is generally the Final). 

The modules so far are divded into type 1 or 2 grade schemes, which means the weights( or percetnages ) of the couorsework and finals would be either 30% 70% or 50% 50%. 

The function 
~~~python 
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

    first_coursework = (Decimal(weight_1) / Decimal(100)) * Decimal(coursework1)

    second_coursework = (Decimal(weight_2) / Decimal(100)) * Decimal(coursework2)

    grade = first_coursework + second_coursework

    return grade

~~~

### on_target 
This function takes a list of dictionaries representing the grades, weights and credits of each class taken so far, and an integer number that represents the " target " grade the student would like to achieve.  It outputs one grade that if achived in all the remaining classes, will resulst in the grade desired. 
It will also output a string message that will tell the student to input a differnt target grade if the deisred grade is too high or low and impossible to achive given previous grades. The message will specify whether the grade deisred is too high or too low.

~~~python
def on_target(in_grades_dict, target):
    """ Function to give a minimum average remaining classes would need
        to acheive final target grade.

        This would be an average number that would populate
        all remaining classes not yet taken, even on multiple levels.

        Example dictionary data type:
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

    Args:
        in_grades_dict (Python List of dictionaries; integers): The List
        contains dictionaries,which in turn contain the values of Grade,
        weight and credits for each class taken

        target (integer): The target grade the student is hoping to acheive

    Returns:
        int: Returns a single integer value representing the minimum grades
        needed in all the remaining classes to acheive targer grade,
        regardless of Level; for example if only level 4 classes have been
        taken, it would output one value that if achieved in all the remaining
        levels will hold true

             OR

        String: If the value returned is less than 0 (target grade is too
        small; i.e got many good grades and will make the target even if
        a 0 is earned) or greater than 100(The student cannot acheivee even if
        all remaining scores are perfect) then returns a message that grade is
        not possible
    """
    gradeIn = 0
    total_credits_in_degree = 1080  # Total weighted credits in the degree
    # 15 credits per class,Final counts as two
    total_classes_degree = total_credits_in_degree / 15
    credits_taken = 0
    # interate over the list of dictionaries
    for i in range(len(in_grades_dict)):
        gradeIn = gradeIn + in_grades_dict[i]['grade'] * in_grades_dict[i]['weight']
        credits_taken += in_grades_dict[i]['credits'] * in_grades_dict[i]['weight']
    missing_weights_sum = (total_credits_in_degree - credits_taken) / 15
    gradeOut = ((total_classes_degree * target) - gradeIn) / missing_weights_sum

    # In the event that the target grade is not possible
    error_message_1 = "Grade not possible, enter a lower target grade"
    error_message_2 = "Grade not possible, enter a higher new target grade"

    # if gradeOut > 100 or gradeOut < 0: # need to add if the grade desired is
    # too low or too high return error_message
    if gradeOut > 100:
        return error_message_1
    elif gradeOut < 0:
        return error_message_2
    else:
        return int(gradeOut)
~~~

## Utility functions
Can be found in the utility.py file. The path is controller > algo > utlity.py

### make_dict 
This function takes the grades, weight and credits from the data base and returns a dict. This function should be used to create a list of these dictionaries to be fed to the grade calculation functions above 

The function 

~~~python
def make_dict(grades, weight, credits):
    """makes a dict from the data given to pass into a list

    Args:
        grade (int): grade from the database
        weight (int): the weight of the class
        credits (int): the unweighted credits for the class
        the credits should be 15 per class, 30 for the final
    """
    new_dict = {"grade": grades,
                "weight": weight,
                "credits": credits}
    return new_dict

~~~
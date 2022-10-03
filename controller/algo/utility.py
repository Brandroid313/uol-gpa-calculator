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

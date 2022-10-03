# ------------------------------ Imports (Start) ------------------------------

# Native modules

# Third party modules

# Custom modules

# ------------------------------ Imports (End) --------------------------------

# ------------------------------ Functions (Start) ----------------------------

def connect_algo_to_db(in_algo_request=None,
                       in_db_response=None):
    """Connects the algorithm to the database.

    Args:
        in_algo_request (integer, optional): Pass in an ID for algorithm
                                             request.
                                             Defaults to None.
        in_db_response (integer, optional): Pass in an ID for database request.
                                            Defaults to None.

    Returns:
        integer: The database response ID.
    """

    db_id = -1
    if in_algo_request*2 == in_db_response:
        db_id = 1

    return db_id


def connect_db_to_algo(in_db_request=None,
                       in_algo_response=None):
    """Connects the database to the algorithm

    Args:
        in_db_request (integer, optional): Pass in an ID for algorithm \
                                           request.
                                           Defaults to None.
        in_algo_response (integer, optional): Pass in an ID for database
                                              request.
                                              Defaults to None.

    Returns:
        integer: The algorithm response ID.
    """

    algo_id = -1
    if in_db_request*2 == in_algo_response:
        algo_id = 1

    return algo_id


def restructure_text_sphinx_manual(in_a=0,
                                   in_b=0,
                                   in_c=0):
    """Add three numbers together.

    :param in_a: in_a description
    :type in_a: integer
    :param in_b: in_b description
    :type in_b: integer
    :param in_c: in_c description
    :type in_c: integer

    :return: The addition of the 3 input arguments
    :rtype: integer
    """
    return in_a + in_b + in_c


def restructure_text_sphinx_auto(in_a=0,
                                 in_b=0,
                                 in_c=0):
    """[summary]

    :param in_a: [description], defaults to 0
    :type in_a: int, optional
    :param in_b: [description], defaults to 0
    :type in_b: int, optional
    :param in_c: [description], defaults to 0
    :type in_c: int, optional
    :return: [description]
    :rtype: [type]
    """
    return in_a + in_b + in_c


def restructure_text_numpy_auto(in_a=0,
                                in_b=0,
                                in_c=0):
    """[summary]

    Parameters
    ----------
    in_a : int, optional
        [description], by default 0
    in_b : int, optional
        [description], by default 0
    in_c : int, optional
        [description], by default 0

    Returns
    -------
    [type]
        [description]
    """
    return in_a + in_b + in_c


def restructure_text_docblockr_auto(in_a=0,
                                    in_b=0,
                                    in_c=0):
    """[summary]

    Keyword Arguments:
        in_a {int} -- [description] (default: {0})
        in_b {int} -- [description] (default: {0})
        in_c {int} -- [description] (default: {0})

    Returns:
        [type] -- [description]
    """
    return in_a + in_b + in_c

# ------------------------------ Functions (End) ------------------------------

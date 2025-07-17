def give_bmi(height, weight):
    """
    Computes the BMI for given heights and weights lists.
    Returns a list of BMI values.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    for h in height:
        if not isinstance(h, (int, float)):
            raise TypeError("Height list must contain only numbers.")

    for w in weight:
        if not isinstance(w, (int, float)):
            raise TypeError("Weight list must contain only numbers.")
    bmi_list = []
    for h, w in zip(height, weight):
        bmi_list.append(w / (h ** 2))
    return bmi_list


def apply_limit(bmi, limit):
    """
    Returns a list of booleans where
    True means the BMI is greater than the limit.
    """
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list must contain only numbers.")
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")
    result = []
    for b in bmi:
        if b > limit:
            result.append(True)
        else:
            result.append(False)
    return result

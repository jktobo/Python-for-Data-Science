# import numpy as np

# def give_bmi(height: list[int | float], weight: list[int | float]) -> list[float]:
#     if len(height) != len(weight):
#         raise ValueError("Height and weight lists must have the same length.")
#     # print("LENGHT: ", len(height))
#     if not all(isinstance(h, (int, float)) for h in height):
#         raise TypeError("Height list must contain only numbers.")
#     if not all(isinstance(w, (int, float)) for w in weight):
#         raise TypeError("Weight list must contain only numbers.")

#     height_arr = np.array(height)
#     weight_arr = np.array(weight)
#     bmi = weight_arr / (height_arr ** 2)
#     return bmi.tolist()

# def apply_limit(bmi: list[float], limit: int) -> list[bool]:
#     if not all(isinstance(b, (int, float)) for b in bmi):
#         raise TypeError("BMI list must contain only numbers.")
#     return [b > limit for b in bmi]

# def main():
#     height = [2.71, 1.15]
#     weight = [165.3, 38.4]

#     bmi = give_bmi(height, weight)
#     print(bmi, type(bmi))
#     print(apply_limit(bmi, 26))

# if __name__ == "__main__":
#     main()

def give_bmi(height, weight):
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
    for b in bmi:
        if not isinstance(b, (int, float)):
            raise TypeError("BMI list must contain only numbers.")

    result = []
    for b in bmi:
        if b > limit:
            result.append(True)
        else:
            result.append(False)

    return result


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

if __name__ == "__main__":
    main()
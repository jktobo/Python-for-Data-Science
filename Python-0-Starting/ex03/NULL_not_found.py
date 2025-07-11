
def NULL_not_found(object: any) -> int:
    
    if object is None:
        print(f"Nothing: None {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: nan {type(object)}")
    elif isinstance(object, int) and type(object) is not bool and object == 0:
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str) and object == '':
        print(f"Empty: {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: {object} {type(object)}")
    else:
        print(f"Type not Found")
        return 1
    return 0

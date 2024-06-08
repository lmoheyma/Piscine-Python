def NULL_not_found(object: any) -> int:
    object_type = type(object)

    if object is None:
        print(f"Nothing : {object} {object_type}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese : {object} {object_type}")
    elif isinstance(object, int) and not isinstance(object, bool) \
            and object == 0:
        print(f"Zero : {object} {object_type}")
    elif isinstance(object, str) and object == "":
        print(f"Empty : {object_type}")
    elif isinstance(object, bool) and not object:
        print(f"Fake : {object} {object_type}")
    else:
        print("Type not found")
        return 1
    return 0

def validate_age(age):
    if(age>0):
        return True
    else:
        raise ValueError("Age Can not be less the then zero")
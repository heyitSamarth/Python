def validate_age(age):
    if(age<0):
        raise ValueError("Age Can not be less the then zero")
    
    
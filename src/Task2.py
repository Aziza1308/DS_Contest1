def typeBasedTransformer(**newdata):
    for key, value in newdata.items():
        if type(value) == int or type(value) == float:
            value = value**2
        elif type(value) == str:
            value=value[::-1]
        elif type(value) == bool:
            value = not value
        elif type(value) == list or type(value) == tuple:
            value = value[::-1]
        elif type(value) == dict:
            value = {v: k for k, v in value.items()}

        print(value)

typeBasedTransformer(name='Aziza', age=19, disabled = False, list=[98, 45, 943], dictionary={'y':89})
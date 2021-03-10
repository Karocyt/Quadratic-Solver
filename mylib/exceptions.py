class CustomError(Exception):
    pass

class MismatchingExponentError(CustomError):
    pass

class InvalidExpression(CustomError):
    pass

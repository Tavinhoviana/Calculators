class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
        self.name = "UnprocessableEntity"
        self.status_code = 422

try: 
    print("Estou no try")
    raise HttpUnprocessableEntityError("lancando exception")

except Exception as exception:
    print("Estou no error")
    print(exception.name)
    print(exception.status_code)
    print(exception.message)


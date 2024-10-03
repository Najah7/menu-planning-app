class RakutenAPIError(Exception):
    def __init__(self, message, response):
        super().__init__(message)
        self.response = response


    def __str__(self):
        return self.message
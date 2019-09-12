class ApiError(Exception):

    def __init__(self, message):
        Exception.__init__(self, message)


class ApiConnectionError(ApiError):

    def __init__(self, message, cause):
        ApiError.__init__(self, message)
        self.cause = cause


def in_request(cause):
    msg = "API request failed with %s" % cause
    return ApiConnectionError(msg, cause)


def invalid_json(cause):
    msg = "Server responded invalid JSON string"
    return ApiConnectionError(msg, cause)


class InvalidRequestError(ApiError):

    def __init__(self, message, bad_value):
        ApiError.__init__(self, message)
        self.bad_value = bad_value


class InvalidResponseError(ApiError):

    def __init__(self, message, bad_value):
        ApiError.__init__(self, message)
        self.bad_value = bad_value

from .error import ApiError as RootError
from . import data_types


class ErrorResponseError(RootError):

    def __init__(self, message, status, data):
        RootError.__init__(self, message)
        self.status = status
        self.data = data


class InvalidRequestError(ErrorResponseError):

    def __init__(self, status, raw_data):
        data = data_types.ErrorData(raw_data)
        message = '%s: %s' % ('InvalidRequestError', data.error.message)
        ErrorResponseError.__init__(self, message, status, data)


class AuthenticationError(ErrorResponseError):

    def __init__(self, status, raw_data):
        data = data_types.ErrorData(raw_data)
        message = '%s: %s' % ('AuthenticationError', data.error.message)
        ErrorResponseError.__init__(self, message, status, data)


class CardError(ErrorResponseError):

    def __init__(self, status, raw_data):
        data = data_types.ErrorData(raw_data)
        message = '%s: %s' % ('CardError', data.error.message)
        ErrorResponseError.__init__(self, message, status, data)


class ApiError(ErrorResponseError):

    def __init__(self, status, raw_data):
        data = data_types.ErrorData(raw_data)
        message = '%s: %s' % ('ApiError', data.error.message)
        ErrorResponseError.__init__(self, message, status, data)

class ApiError(Exception):
    pass


class BadToken(ApiError):
    pass


class MethodError(ApiError):
    pass

import httpx


class PulsechainException(Exception):
    pass


class PulseChainAPIException(PulsechainException):
    pass


class PulseChainTimeoutException(PulseChainAPIException):
    pass


class PulseChainServerError(PulseChainAPIException):
    pass


class PulseChainUnprocessableEntityException(PulseChainAPIException):
    def __init__(self, response: httpx.Response):
        super().__init__(response.json()["message"])


class PulseChainBadRequestException(PulseChainAPIException):
    def __init__(self, response: httpx.Response):
        super().__init__(response.json()["message"])


class PulseChainUnknownException(PulseChainAPIException):
    pass


class PulseChainBadParamException(PulsechainException):
    pass

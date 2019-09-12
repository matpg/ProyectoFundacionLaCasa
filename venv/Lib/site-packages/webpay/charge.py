from . import data_types


class Charge:

    def __init__(self, client):
        self.__client = client

    def create(self, *args, **kwargs):
        """Create a charge object with given parameters.
        In live mode, this issues a transaction.

        Args:
            - ChargeRequestCreate
            - Value convertible to ChargeRequestCreate
            - kwargs corresponds to ChargeRequestCreate

        Returns:
            the API response in ChargeResponse
        """
        req = data_types.ChargeRequestCreate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('post', 'charges', req)
        return data_types.ChargeResponse(raw_response)

    def retrieve(self, *args, **kwargs):
        """Retrieve a existing charge object by charge id.

        Args:
            - ChargeIdRequest
            - Value convertible to ChargeIdRequest
            - kwargs corresponds to ChargeIdRequest

        Returns:
            the API response in ChargeResponse
        """
        req = data_types.ChargeIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'get', 'charges' + '/' + str(req.id), req)
        return data_types.ChargeResponse(raw_response)

    def refund(self, *args, **kwargs):
        """Refund a paid charge specified by charge id.
        Optional argument amount is to refund partially.

        Args:
            - ChargeRequestRefund
            - Value convertible to ChargeRequestRefund
            - kwargs corresponds to ChargeRequestRefund

        Returns:
            the API response in ChargeResponse
        """
        req = data_types.ChargeRequestRefund.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'post', 'charges' + '/' + str(req.id) + '/' + 'refund', req)
        return data_types.ChargeResponse(raw_response)

    def capture(self, *args, **kwargs):
        """Capture a not captured charge specified by charge id.

        Args:
            - ChargeRequestWithAmount
            - Value convertible to ChargeRequestWithAmount
            - kwargs corresponds to ChargeRequestWithAmount

        Returns:
            the API response in ChargeResponse
        """
        req = data_types.ChargeRequestWithAmount.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'post', 'charges' + '/' + str(req.id) + '/' + 'capture', req)
        return data_types.ChargeResponse(raw_response)

    def all(self, *args, **kwargs):
        """List charges filtered by params.

        Args:
            - ChargeListRequest
            - Value convertible to ChargeListRequest
            - kwargs corresponds to ChargeListRequest

        Returns:
            the API response in ChargeResponseList
        """
        req = data_types.ChargeListRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('get', 'charges', req)
        return data_types.ChargeResponseList(raw_response)

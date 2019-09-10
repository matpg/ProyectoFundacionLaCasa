from . import data_types


class Token:

    def __init__(self, client):
        self.__client = client

    def create(self, *args, **kwargs):
        """Create a token object with given parameters.

        Args:
            - TokenRequestCreate
            - Value convertible to TokenRequestCreate
            - kwargs corresponds to TokenRequestCreate

        Returns:
            the API response in TokenResponse
        """
        req = data_types.TokenRequestCreate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('post', 'tokens', req)
        return data_types.TokenResponse(raw_response)

    def retrieve(self, *args, **kwargs):
        """Retrieve a token object by token id.

        Args:
            - TokenIdRequest
            - Value convertible to TokenIdRequest
            - kwargs corresponds to TokenIdRequest

        Returns:
            the API response in TokenResponse
        """
        req = data_types.TokenIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'get', 'tokens' + '/' + str(req.id), req)
        return data_types.TokenResponse(raw_response)

from . import data_types


class Account:

    def __init__(self, client):
        self.__client = client

    def retrieve(self, *args, **kwargs):
        """Retrieve information of the current user.

        Args:
            - EmptyRequest
            - Value convertible to EmptyRequest
            - kwargs corresponds to EmptyRequest

        Returns:
            the API response in AccountResponse
        """
        req = data_types.EmptyRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('get', 'account', req)
        return data_types.AccountResponse(raw_response)

    def delete_data(self, *args, **kwargs):
        """Delete all test data of this account.

        Args:
            - EmptyRequest
            - Value convertible to EmptyRequest
            - kwargs corresponds to EmptyRequest

        Returns:
            the API response in DeletedResponse
        """
        req = data_types.EmptyRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'delete', 'account' + '/' + 'data', req)
        return data_types.DeletedResponse(raw_response)

from . import data_types


class Customer:

    def __init__(self, client):
        self.__client = client

    def create(self, *args, **kwargs):
        """Create a customer object with given parameters.

        Args:
            - CustomerRequestCreate
            - Value convertible to CustomerRequestCreate
            - kwargs corresponds to CustomerRequestCreate

        Returns:
            the API response in CustomerResponse
        """
        req = data_types.CustomerRequestCreate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('post', 'customers', req)
        return data_types.CustomerResponse(raw_response)

    def retrieve(self, *args, **kwargs):
        """Retrieve a customer object by customer id.
        If the customer is already deleted, "deleted" attribute becomes true.

        Args:
            - CustomerIdRequest
            - Value convertible to CustomerIdRequest
            - kwargs corresponds to CustomerIdRequest

        Returns:
            the API response in CustomerResponse
        """
        req = data_types.CustomerIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'get', 'customers' + '/' + str(req.id), req)
        return data_types.CustomerResponse(raw_response)

    def update(self, *args, **kwargs):
        """Update an existing customer with specified parameters.

        Args:
            - CustomerRequestUpdate
            - Value convertible to CustomerRequestUpdate
            - kwargs corresponds to CustomerRequestUpdate

        Returns:
            the API response in CustomerResponse
        """
        req = data_types.CustomerRequestUpdate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'post', 'customers' + '/' + str(req.id), req)
        return data_types.CustomerResponse(raw_response)

    def delete(self, *args, **kwargs):
        """Delete an existing customer.

        Args:
            - CustomerIdRequest
            - Value convertible to CustomerIdRequest
            - kwargs corresponds to CustomerIdRequest

        Returns:
            the API response in CustomerResponse
        """
        req = data_types.CustomerIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'delete', 'customers' + '/' + str(req.id), req)
        return data_types.CustomerResponse(raw_response)

    def all(self, *args, **kwargs):
        """List customers filtered by params.

        Args:
            - BasicListRequest
            - Value convertible to BasicListRequest
            - kwargs corresponds to BasicListRequest

        Returns:
            the API response in CustomerResponseList
        """
        req = data_types.BasicListRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('get', 'customers', req)
        return data_types.CustomerResponseList(raw_response)

    def delete_active_card(self, *args, **kwargs):
        """Delete a card data of a customer.

        Args:
            - CustomerIdRequest
            - Value convertible to CustomerIdRequest
            - kwargs corresponds to CustomerIdRequest

        Returns:
            the API response in CustomerResponse
        """
        req = data_types.CustomerIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'delete', 'customers' + '/' + str(req.id) + '/' + 'active_card', req)
        return data_types.CustomerResponse(raw_response)

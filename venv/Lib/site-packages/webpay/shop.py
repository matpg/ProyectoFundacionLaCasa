from . import data_types


class Shop:

    def __init__(self, client):
        self.__client = client

    def create(self, *args, **kwargs):
        """Create a shop object with given parameters.

        Args:
            - ShopRequestCreate
            - Value convertible to ShopRequestCreate
            - kwargs corresponds to ShopRequestCreate

        Returns:
            the API response in ShopResponse
        """
        req = data_types.ShopRequestCreate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('post', 'shops', req)
        return data_types.ShopResponse(raw_response)

    def retrieve(self, *args, **kwargs):
        """Retrieve a shop object by shop id.

        Args:
            - ShopIdRequest
            - Value convertible to ShopIdRequest
            - kwargs corresponds to ShopIdRequest

        Returns:
            the API response in ShopResponse
        """
        req = data_types.ShopIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'get', 'shops' + '/' + str(req.id), req)
        return data_types.ShopResponse(raw_response)

    def update(self, *args, **kwargs):
        """Update an existing shop with specified parameters.

        Args:
            - ShopRequestUpdate
            - Value convertible to ShopRequestUpdate
            - kwargs corresponds to ShopRequestUpdate

        Returns:
            the API response in ShopResponse
        """
        req = data_types.ShopRequestUpdate.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'post', 'shops' + '/' + str(req.id), req)
        return data_types.ShopResponse(raw_response)

    def alter_status(self, *args, **kwargs):
        """Alter the test shop's status to the specified one.

        Args:
            - ShopRequestAlterStatus
            - Value convertible to ShopRequestAlterStatus
            - kwargs corresponds to ShopRequestAlterStatus

        Returns:
            the API response in ShopResponse
        """
        req = data_types.ShopRequestAlterStatus.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'post', 'shops' + '/' + str(req.id) + '/' + 'alter_status', req)
        return data_types.ShopResponse(raw_response)

    def all(self, *args, **kwargs):
        """List shops filtered by params.

        Args:
            - BasicListRequest
            - Value convertible to BasicListRequest
            - kwargs corresponds to BasicListRequest

        Returns:
            the API response in ShopResponseList
        """
        req = data_types.BasicListRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('get', 'shops', req)
        return data_types.ShopResponseList(raw_response)

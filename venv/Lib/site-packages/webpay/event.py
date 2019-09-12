from . import data_types


class Event:

    def __init__(self, client):
        self.__client = client

    def retrieve(self, *args, **kwargs):
        """Retrieve an event object by event id.

        Args:
            - EventIdRequest
            - Value convertible to EventIdRequest
            - kwargs corresponds to EventIdRequest

        Returns:
            the API response in EventResponse
        """
        req = data_types.EventIdRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request(
            'get', 'events' + '/' + str(req.id), req)
        return data_types.EventResponse(raw_response)

    def all(self, *args, **kwargs):
        """List events filtered by params.

        Args:
            - EventListRequest
            - Value convertible to EventListRequest
            - kwargs corresponds to EventListRequest

        Returns:
            the API response in EventResponseList
        """
        req = data_types.EventListRequest.create(
            kwargs if len(args) == 0 else args[0])
        raw_response = self.__client._request('get', 'events', req)
        return data_types.EventResponseList(raw_response)

from . import charge, customer, token, event, shop, recursion, account, data_types, error, error_response

import requests
import json
import copy


class WebPay:

    """Main interface of webpay.
    """

    _default_headers = {

        'Content-Type': "application/json",

        'Accept': "application/json",

        'User-Agent': "Apipa-webpay/2.2.3 python",

        'Accept-Language': "en",
    }

    _auth = None

    def __init__(self, auth_token, options={}, **kwargs):
        """Instantiate webpay client

        Attributes:
        - auth_token: Authorization information.
        - `options`: Connection options.
        """
        kwargs.update(options)
        self._options = kwargs
        self._headers = copy.copy(self._default_headers)

        self._headers['Authorization'] = 'Bearer ' + auth_token
        self.charge = charge.Charge(self)
        self.customer = customer.Customer(self)
        self.token = token.Token(self)
        self.event = event.Event(self)
        self.shop = shop.Shop(self)
        self.recursion = recursion.Recursion(self)
        self.account = account.Account(self)

    def set_accept_language(self, value):
        self._headers['Accept-Language'] = value

    def receive_webhook(self, request_body):
        try:
            decoded = json.loads(request_body)
            return data_types.EventResponse(decoded)
        except ValueError as exc:
            raise error.ApiConnectionError(
                'Webhook request body is invalid JSON string', exc)

    def _request(self, method, path, param_data):
        def flatten_rec(value, prefix, dest):
            if type(value) is dict:
                for k, v in value.items():
                    flatten_rec(v, '%s[%s]' % (prefix, k), dest)
            elif type(value) is list:
                for v in value:
                    flatten_rec(v, prefix + '[]', dest)
            elif value is True:
                dest[prefix] = 'true'
            elif value is False:
                dest[prefix] = 'false'
            else:
                dest[prefix] = value

        def flatten_query_params(hash_value):
            flat = {}
            for k, v in hash_value.items():
                flatten_rec(v, k, flat)
            return flat

        try:
            r = requests.request(method, self._options.get('api_base', 'https://api.webpay.jp/v1') + "/" + path,
                                 params=flatten_query_params(
                                     param_data.query_params()),
                                 data=json.dumps(param_data.request_body()),
                                 headers=self._headers,
                                 auth=self._auth)
        except Exception as exc:
            raise error.in_request(exc)
        return self._process_response(r)

    def _process_response(self, r):
        status = r.status_code
        try:
            data = r.json()
        except Exception as exc:
            raise error.invalid_json(exc)

        if status >= 200 and status < 300:
            return data
        else:
            if status == 400:
                raise error_response.InvalidRequestError(status, data)
            if status == 401:
                raise error_response.AuthenticationError(status, data)
            if status == 402:
                raise error_response.CardError(status, data)
            if status == 404:
                raise error_response.InvalidRequestError(status, data)
            if True:
                raise error_response.ApiError(status, data)
            raise Exception("Unknown error is returned")

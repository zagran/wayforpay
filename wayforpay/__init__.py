from .api import Api


__all__ = ["WayForPay"]


class WayForPay:
    def __init__(self, merchant_account, merchant_key):
        self.merchant_account = merchant_account
        self.merchant_key = merchant_key
        self.api = Api(self.merchant_account, self.merchant_key)

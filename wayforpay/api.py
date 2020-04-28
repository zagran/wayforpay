import requests

from .constants import API_URL
from .utils import generate_signature


# noinspection PyMethodMayBeStatic
class Api:
    def __init__(self, merchant_account, merchant_key, merchant_domain):
        self.merchant_account = merchant_account
        self.merchant_key = merchant_key
        self.merchant_domain = merchant_domain

    def _query(self, params, url=API_URL):
        response = requests.post(url, json=params)
        return response.json()

    def verify(self, data, return_url=""):
        """
        Cart verification and receiving token(Verify)
        :param data:
        :param return_url:
        :return:
        """
        # merchantAccount, merchantDomainName, orderReference, amount, currency
        signature_data = f"{self.merchant_account};{self.merchant_domain};1;0;UAH"
        params = {
            "transactionType": "VERIFY",
            "merchantAccount": self.merchant_account,
            "merchantAuthType": "SimpleSignature",
            "merchantDomainName": self.merchant_domain,
            "merchantSignature": generate_signature(self.merchant_key, signature_data),
            "apiVersion": 1,
            "orderReference": data["order_id"],
            "amount": "0",
            "currency": "UAH",
            "card": data["number"],
            "expMonth": data["date"].strip().split("/")[0],
            "expYear": "20" + "/".join((data["date"]).split("/")[1:]).strip(),
            "cardCvv": data["cvv"],
            "cardHolder": data["cardholder"],
            "clientFirstName": data["cardholder"].strip().split(" ")[0],
            "clientLastName": " ".join((data["cardholder"] + " ").split(" ")[1:]).strip(),
            "clientCountry": "UA",
            "clientEmail": data["email"],
            "clientPhone": data["phone"],
        }
        if return_url:
            params["return_url"] = return_url
        response = self._query(params)
        return response

import json
from pydantic import ValidationError
import requests
from models import account, cards, transactions


class ExtendAPI:
    def __init__(self):
        self.api_endpoint = "https://api.paywithextend.com/"
        self.header = {
            "content-type": "application/json",
            "Accept": "application/vnd.paywithextend.v2021-03-12+json",
        }

    def signin(self, email: str, password: str) -> account.Account:
        url = self.api_endpoint + "signin"
        body = {"email": email, "password": password}
        try:
            res = requests.post(url, headers=self.header, json=body)
            if res.status_code >= 300:
                return None
            return account.Account.parse_raw(res.text)
        except ValidationError as ve:
            print("Failed to create account: {}".format(ve))
        except Exception as e:
            print("Failed to signin: {}".format(e))

    def get_user(self, bearer_token: str, id="me") -> account.User:
        """
        Get user information:
        "me" refers to currently authenticated user
        """
        url = self.api_endpoint + "users/{id}".format(id=id)
        header = self.header.copy()
        header["Authorization"] = "Bearer {}".format(bearer_token)

        try:
            res = requests.get(url, headers=header)
            if res.status_code >= 300:
                return None
            return account.User.parse_raw(res.text)
        except ValidationError as ve:
            print("Failed to create account: {}".format(ve))
        except Exception as e:
            print("Failed to get account: {}".format(e))

    def get_cards(self, bearer_token, query_params) -> cards.Cards:
        # TODO Handle for query parameters
        url = self.api_endpoint + "virtualcards"

        header = self.header.copy()
        header["Authorization"] = "Bearer {}".format(bearer_token)
        try:
            res = requests.get(url, headers=header)
            if res.status_code >= 300:
                return None
            print(res.text)
            return cards.Cards.parse_raw(res.text)
        except ValidationError as ve:
            print("Failed to create account: {}".format(ve))
        except Exception as e:
            print("Failed to get account: {}".format(e))

    def get_transaction_list(
        self, bearer_token, card_id
    ) -> transactions.TransactionList:
        url = self.api_endpoint + "virtualcards/" + card_id + "/transactions"

        header = self.header.copy()
        header["Authorization"] = "Bearer {}".format(bearer_token)
        try:
            res = requests.get(url, headers=header)
            if res.status_code >= 300:
                return None
            return transactions.TransactionList.parse_raw(res.text)
        except ValidationError as ve:
            print("Failed to create account: {}".format(ve))
        except Exception as e:
            print("Failed to get account: {}".format(e))

    def get_transaction_detail(
        self, bearer_token, transaction_id
    ) -> transactions.Transaction:
        url = self.api_endpoint + "transactions/" + transaction_id
        header = self.header.copy()
        header["Authorization"] = "Bearer {}".format(bearer_token)
        try:
            res = requests.get(url, headers=header)
            if res.status_code >= 300:
                return None
            return transactions.Transaction.parse_raw(res.text)
        except ValidationError as ve:
            print("Failed to create account: {}".format(ve))
        except Exception as e:
            print("Failed to get account: {}".format(e))

    def signout(self, bearer_token: str):
        url = self.api_endpoint + "signout"
        header = self.header.copy()
        header["Authorization"] = "Bearer {}".format(bearer_token)
        try:
            res = requests.delete(url, headers=header)

            if "msg" not in json.loads(res.text):
                raise Exception("Failed to signout")
        except Exception as e:
            print("Failed to signin: {}".format(e))

#!/usr/bin/env python3

import cmd
import datetime
import getpass

from models.account import Account
from models.cards import Cards
from util.api import ExtendAPI


class ExtendShell(cmd.Cmd):
    banner = "Welcome to Extend CLI. Type help or ? to list commands.\n"
    prompt = "(Extend CLI) >"
    file = None
    extend_account: Account
    cards: Cards

    def __init__(self):
        super().__init__()
        self.extend_account = None
        self.cards = None

        self.api = ExtendAPI()

    def do_test(self, arg) -> None:
        "Test Interpreter"
        print("My arg is {}".format(arg))

    def do_login(self, arg) -> None:
        "Sign into Extend account"
        email = input("email: ")
        password = getpass.getpass()
        try:
            self.extend_account = self.api.signin(email=email, password=password)
            if self.extend_account:
                print("Success")
            else:
                print("Failed to login")

        except Exception:
            print("Failed to login")
            pass

    def do_logout(self, arg) -> None:
        if self.extend_account:
            try:
                self.api.signout(self.extend_account.token)
            except Exception:
                pass
            finally:
                self.extend_account = None
                self.cards = None

    def do_user(self, arg) -> None:
        "Get information about a user"
        if not self.extend_account:
            print("Not signed in")
            try:
                self.do_login(None)
            except Exception:
                return
        id = arg if arg else "me"
        user = self.api.get_user(id=id, bearer_token=self.extend_account.token)
        print(user.dict())

    def do_cards(self, arg) -> None:
        "List all virtual cards available to your user, including the available balance remaining"
        if not self.extend_account:
            print("Not signed in")
            try:
                self.do_login(arg)
            except Exception:
                return
        params = {}
        self.cards = self.api.get_cards(
            bearer_token=self.extend_account.token, query_params=params
        )
        self.cards.pretty_print()

    def do_transactions(self, arg) -> None:
        "List the transactions associated with your virtual card."
        if not self.extend_account:
            print("Not signed in")
            try:
                self.do_login(None)
            except Exception:
                return
        if not self.cards:
            try:
                self.cards = self.api.get_cards(
                    bearer_token=self.extend_account.token, query_params={}
                )
            except Exception:
                return

        card_number = 0
        if not arg:
            self.cards.pretty_print()
            card_number = int(input("Select card number: "))
        else:
            card_number = int(arg)
        if card_number > len(self.cards.virtualCards):
            print(
                "Invalid card number. Card number must be between 0 and {}".format(
                    len(self.cards.virtualCards)
                )
            )
            return

        card_id = self.cards.virtualCards[card_number].id
        transaction_list = self.api.get_transaction_list(
            bearer_token=self.extend_account.token, card_id=card_id
        )
        transaction_list.pretty_print()

    def do_transaction_detail(self, arg) -> None:
        "View the details for each individual transaction you’ve made."
        if not self.extend_account:
            print("Not signed in.")
            try:
                self.do_login(arg)
            except Exception:
                return
        transaction_id = arg
        try:
            transaction = self.api.get_transaction_detail(
                self.extend_account.token, transaction_id
            )
            transaction.pretty_print()
        except Exception as e:
            print("Failed to get transaction detail: {}".format(e))

    def do_exit(self, arg) -> bool:
        "Close the app"
        return self.do_EOF(arg)

    def do_EOF(self, arg) -> bool:
        "Logout of extend account and close shell"
        print()
        print("Logging out")
        # Logout script
        try:
            self.do_logout(arg)
        except Exception:
            return False
        return True


if __name__ == "__main__":
    ExtendShell().cmdloop()

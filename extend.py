import cmd
import datetime
import getpass
from prettytable import PrettyTable

from models.account import Account
from models.cards import Cards
from util.api import ExtendAPI


class ExtendShell(cmd.Cmd):
    banner = "Welcome to Extend CLI. Type help or ? to list commands.\n"
    prompt = "(Extend CLI) >"
    file = None
    extend_account: Account = None
    cards: Cards = None
    api = ExtendAPI()

    def do_test(self, arg) -> None:
        "Test Interpreter"
        print("My arg is {}".format(arg))

    def do_login(self, arg) -> None:
        "Sign into Extend account"
        email = input("email: ")
        password = getpass.getpass()
        self.extend_account = self.api.signin(email=email, password=password)
        print(self.extend_account.dict())

    def do_user(self, arg) -> None:
        "Get information about a user"
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
        else:
            id = arg if arg else "me"
            user = self.api.get_user(id=id, bearer_token=self.extend_account.token)
            print(user.dict())

    def do_cards(self, arg) -> None:
        "List all virtual cards available to your user, including the available balance remaining"
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
        else:
            id = arg if arg else "me"
            params = {}
            self.cards = self.api.get_cards(
                bearer_token=self.extend_account.token, query_params=params
            )
            print(self.cards.dict())

    # TODO
    def do_transactions(self, arg) -> None:
        "List the transactions associated with your virtual card."
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
            return
        if not self.cards:
            self.cards = self.api.get_cards(
                bearer_token=self.extend_account.token, query_params={}
            )

        card_number = 0
        if not arg:
            table = PrettyTable(
                ["Card Number", "Card ID", "Name", "Last 4", "Exp Date"]
            )
            for index, card in enumerate(self.cards.virtualCards):
                card_id = card.id
                name = card.displayName
                last4 = card.last4
                exp_date = datetime.datetime.strptime(
                    card.expires, "%Y-%m-%dT%H:%M:%S.%f%z"
                ).strftime("%m/%Y")
                table.add_row([index, card_id, name, last4, exp_date])
            print(table)

            card_number = int(input("Select card number:"))
        else:
            if int(arg) > len(self.cards.virtualCards):
                print(
                    "Invalid card number. Card number must be between 0 and {}".format(
                        len(self.cards.virtualCards)
                    )
                )
                return

            card_number = int(arg)

        card_id = self.cards.virtualCards[card_number].id
        transaction_list = self.api.get_transaction_list(
            bearer_token=self.extend_account.token, card_id=card_id
        )
        print(transaction_list.dict())

    # TODO
    def do_transaction_detail(self, arg) -> None:
        "View the details for each individual transaction you’ve made."
        pass

    def do_EOF(self, line) -> bool:
        "Logout of extend account and close shell"
        print()
        print("Logging out")
        # Logout script
        if self.extend_account:
            self.api.signout(self.extend_account.token)
        return True


if __name__ == "__main__":
    ExtendShell().cmdloop()

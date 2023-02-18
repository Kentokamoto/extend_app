import cmd
import getpass

from models.account import Account
from util.api import ExtendAPI


class ExtendShell(cmd.Cmd):
    banner = "Welcome to Extend CLI. Type help or ? to list commands.\n"
    prompt = "(Extend CLI) >"
    file = None
    extend_account: Account = None
    api = ExtendAPI()

    def do_test(self, arg) -> None:
        'Test Interpreter'
        print("My arg is {}".format(arg))

    def do_login(self, arg) -> None:
        'Sign into Extend account'
        email = input("email: ")
        password = getpass.getpass()
        self.extend_account = self.api.signin(email=email,
                                              password=password)
        print(self.extend_account.dict())

    def do_user(self, arg) -> None:
        'Get information about a user'
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
        else:
            id = arg if arg else "me"
            user = self.api.get_user(id=id,
                                        bearer_token=self.extend_account.token)
            print(user.dict())

    def do_cards(self, arg) -> None:
        'List all virtual cards available to your user, including the available balance remaining'
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
        else:
            id = arg if arg else "me"
            cards = self.api.get_cards(bearer_token=self.extend_account.token)
            print(cards.dict())

    # TODO
    def do_transactions(self, arg) -> None:
        'List the transactions associated with your virtual card.'
        pass

    # TODO
    def do_transaction_detail(self, arg) -> None:
        'View the details for each individual transaction you’ve made.'
        pass

    def do_EOF(self, line) -> bool:
        'Logout of extend account and close shell'
        print()
        print("Logging out")
        # Logout script
        if self.extend_account:
            self.api.signout(self.extend_account.token)
        return True

if __name__ == '__main__':
    ExtendShell().cmdloop()

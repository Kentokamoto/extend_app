import cmd
import getpass

from models.account import Account
from util.api import ExtendAPI


class ExtendShell(cmd.Cmd):
    banner = "Welcome to Extend CLI. Type help or ? to list commands.\n"
    prompt = "(Extend CLI) >"
    file = None
    extend_account: Account
    api = ExtendAPI()

    def do_test(self, arg) -> None:
        'Test Interpreter'
        print("My arg is {}".format(arg))

    def do_login(self, arg) -> None:
        'Sign into Extend account'
        email = input("email: ")
        password = getpass.getpass()
        print("email: {}".format(email))
        print("password: {}".format(password))
        self.extend_account = self.api.signin(email=email,
                                              password=password)
        print(self.extend_account.dict())

    def do_user(self, arg) -> None:
        if not self.extend_account:
            print("Not signed in. Type login to sign into an existing Extend account")
        else:
            id = arg if arg else "me"
            user = self.api.get_user(id=id,
                                        bearer_token=self.extend_account.token)
            print(user.dict()) 

    def do_EOF(self, line) -> bool:
        'Logout of extend account and close shell'
        print()
        print("Logging out")
        # Logout script
    
        return True

if __name__ == '__main__':
    ExtendShell().cmdloop()

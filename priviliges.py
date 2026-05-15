import user
class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges)

class Admin(user.User):
    """"""

    def __init__(self,first_name,last_name,password,age):
        super().__init__(first_name,last_name,password,age)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])
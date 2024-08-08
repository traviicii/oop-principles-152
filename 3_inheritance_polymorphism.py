
# Inheritance and Polymorphism

#-- Inheritance : Extending a parent class and giving it extended/additional functionality and characteristics
    #-- Inheritance allows a child class to inherit attributes and methods from another class (parent class)

# General functionality --> more specific functionality

#-- Polymorphism : Objects from different classes (sub classes) responding similarly to the same method in their own uniwue way
    #-- achieved through method overrriding, where a subclass provides a specific implementation of a method that's already defined in the parent class (superclass)

# Parent class (superclass)
class User():

    def __init__(self, email, password, username):
        self.email = email
        self._password = password # protected attribute
        self.username = username

    # All methods are inherited by the subclass (child class)
    def user_info(self):
        print(f"User: {self.username} can be contacted at {self.email}")

    # Setter
    def set_password(self, new_pass):
        self._password = new_pass

    # Getter
    def get_username(self):
        print(self.username)


# Class that inherits from User
class Admin(User):

    def __init__(self, email, _password, username, admin_id, isadmin = True):
        super().__init__(email, _password, username)
        self.admin_id = admin_id
        self.isadmin = isadmin

    def user_info(self):
        print(f"Admin: #{self.admin_id} {self.username} can recieve support tickets at {self.email}")

    # getter
    def get_password(self):
        print(self._password)

# Instantiate a User class object
billy_bob = User('billy@email.com', '1234', 'billy-b')
billy_bob.user_info()

# instantiate an Admin class object
travis = Admin('traviscpeck@codingtemple.com', '1234', 'traviicii', 1)
travis.user_info()


billy_bob.get_username()
billy_bob.set_password("this is the new password now")

travis.get_username()

travis.set_password('123456789')
travis.get_password()
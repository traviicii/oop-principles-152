
# Encapsulation : Bundling data and methods within a class, controlling access to them

#-- Public Attributes : Are accessible from anywhere, both inside and outside of the class they're defined in

#-- Private Attributes : indicated by a double underscore (dunder) preceding the attribute name -> __name
    #-- Accessible only within the class that it's defined in. Useful for securing and hiding data

#-- Protected Attributes : Indicated by a single underscore preceding -> _name
    #-- Accessible in both the class it's defined in, as well as any subclasses


class Smartphone():

    def __init__(self, model, credit_card, operating_system):
        self.model = model # public attribute
        self.__wallet = credit_card # private attribute, only accessible within this class
        self._operating_system = operating_system # protected attribute, accessible within this class and any subclasses

    def get_info(self):
        print(f"Model: {self.model}")
        print(f"Wallet: ****-****-****-{self.__wallet[-4:]}")
        print(f"OS: {self._operating_system}")
    
    def get_wallet(self): # need a 'getter' in order to decide how a user can access and view the __wallet. this information is completely under our controll
        return self.__wallet
    
    def set_wallet(self, new_card): # creating a 'setter' to controll how my __wallet information is altered
        flag = False
        for i in new_card:
            if i.isdigit():
                flag = True
                continue
            else:
                flag = False
                print("Please enter a valid credit card number (no dashes or spaces)!")
                break

        if flag: # after checking all the characters, if it's a valid card number, then we'll change the __wallet to the new card
            self.__wallet = new_card
            print(f"New card set to: {new_card[-4:]}")


iphone = Smartphone("iPhone XS", '1111-1111-2222-0000', 'iOS 13')

# print(iphone.__wallet) # will not work, private attribute

# Getters and  Setters

# Getters : Method used to access any attribute (including private and protected), since they are not accessible otherwise

print(iphone.get_wallet())
iphone.__wallet = '12345678' # We can't do this because __wallet is private and not accessible from here, only within the class itself
print(iphone.get_wallet()) #__wallet remains unchanged
iphone.get_info()

# Setters : Method used to set any attribute (including priate and protected attributes)

iphone.set_wallet('4321123478907654')


class Student():
    name = ""
    age = 15
    hobby = "PE"
    nationality = "Brazil"
    #constructor
    def __init__(self):
        print("Making a new student.")
    def change_details(self):
        self.name = input("What is your name: ")
        self.hobby = input("What is your favourite hobby: ")
        self.age = int(input("How old are you: "))
        self.nationality = input("What is your nationality: ")
    def show_details(self):
        print("Showing details.")
        print(self.name)
        print(self.age)
        print(self.hobby)
        print(self.nationality)


pupil = Student()
pupil.change_details()
pupil.show_details()


class MobilePhone():
    brand = ""
    model = ""
    battery = 100
    price = 0
    def __init__(self):
        print("Customizing an mobile phone.")
    def customize_phone(self):
        self.brand = input("What brand is your phone: ")
        self.model = input("What type of model is your phone: ")
        self.battery = int(input("What is your battery percentage: "))
        self.price = float(input("How much will your mobile phone cost: "))
    def display_phone(self):
        print("Displaying phone details.")
        print(self.brand)
        print(self.model)
        print(self.battery)
        print(self.price)

    def battery_decrease(self):
        self.battery -= 2
        print("Your battery percentage has now decreased by 2% and is it currently at: " + str(self.battery))


IPhone = MobilePhone()
IPhone.customize_phone()
IPhone.display_phone()
IPhone.battery_decrease()






    
     
# Question one: make a class about your family
class Family:
    def __init__(self, family_country, family_race, family_name, family_generation_number, family_size, family_type, family_status, family_address ):
        self.country = family_country
        self.race = family_race
        self.name = family_name
        self.generation_number = family_generation_number
        self.size = family_size
        self.type = family_type
        self.status = family_status
        self.address = family_address
        self.amount_of_relatives = []
    def current_family_size(self):
        new_family_size = self.size + 1
        print("Your family just had another child, the new family size is {size}".format(size = new_family_size))
    def next_generation(self):
        next_generation_number = self.generation_number + 1
        print("The next generations number will be {number}".format(number = next_generation_number))
    def relates(self, relative):
        if self.name ==  relative.name:
            self.amount_of_relatives.append(relative)
            relative.amount_of_relatives.append(self)
            print("Your family and {} family are related".format(relative.name))
        else:
            print("Your family and {} are not related".format(relative.name))
    def __repr__(self):
        description = "The {name} family is a {status} {race} family who live in {country} and have a generation number of {number}. They are a {type} family and have a family size of {size} and have {rel} relatives".format(name = self.name, status = self.status, race = self.race, country = self.country, number = self.generation_number, type = self.type, size = self.size, rel = len(self.amount_of_relatives))
        return description

family1 = Family("Nigeria", "black", "Etok-Akpan", 5.12, 5, "Nuclear", "rich", "No.1234")
family2 = Family("American", "black", "Etuk-Akpan", 5.11, 5, "Nuclear", "average", "No.3214")
family1.relates(family2)
print(family1)
family2.relates(family1)
print(family2)
family1.current_family_size()
family2.current_family_size()
family1.next_generation()
family2.next_generation()

# Question 2: create a class about a social media user
class User:
    def __init__(self, user_number, user_password, user_name, user_numbers, user_status):
        self.number = user_number
        self.password = user_password
        self.name = user_name
        self.chats_numbers = user_numbers
        self.status = user_status
    def login(self, password):
        if password == self.password:
            print("Welcome {name}".format(name = self.name))
        else:
            print("Invalid password")
    def chat_number(self):
        print("{name} you have {num} chats".format(name = self.name, num = len(self.chats_numbers)))
    def stats(self):
        print("you posted {stat} as your status and you have {num} viewers".format(stat = self.status, num = len(self.chats_numbers)))

user1 = User(9131155758, "davdav", "David", [32455653, 22244567, 12355678], "I am a sigma")
user1.login("dada")
user1.chat_number()
user1.stats()

class Hospital_patient:
    def __init__(self, patient, problem):
        self.patient = patient
        self.sickness = problem
    def sicknes(self):
        if self.sickness == "head ache":
            print("{} take paracetamor to cure your headache".format(self.patient))
        elif self.sickness == "malaria":
            print("{} take malaria drugs".format(self.patient))
        elif self.sickness == "fever":
            print("{} take malaria drug".format(self.patient))
        elif self.sickness == "ebola":
            print("{} you would have to go for admission".format(self.patient))
        elif self.sickness == "HIV/AIDS":
            print("{} you would have to go for admission".format(self.patient))
        else:
            print("This is not a sickness")
patient = Hospital_patient("daniel", "malaria")
patient.sicknes()

class Hospital_staff:
    def __init__(self, staff_name, staff_keynumber):
        self.staff_name = staff_name
        self.staff_keys = staff_keynumber
        self.registered_keys = 54321
    def inputed_key(self):
            if self.staff_keys == self.registered_keys :
                print("Welcome {} ".format(self.staff_name))
            else:
                print("Invalid user attempt")
staff = Hospital_staff("russel", 54321)
staff.inputed_key()
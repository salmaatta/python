#class methods
class member:
    users_num =0

    @classmethod
    def show_users_count(cls):
        print (f"We have {cls.users_num} users in our system")
    
    @staticmethod
    def hello():
        
        print("Hello new user")

    def __init__(self, first_name, middle_name, last_name , gender):

        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender 

        member.users_num +=1

    def full_name(self):

        return f"{self.fname} {self.mname} {self.lname}"

    def say_hello(self):
        if self.gender =="male" :
            return f" Hello Mr {self.fname}"
        else:
            return f"Hello Mrs {self.fname}"
    def get_all_info(self):
        return f"{self.say_hello()} , Your full name is : {self.full_name()}"
    

member_one = member("salma", "sherif", "atta","female")
member_two = member("ola", "abdallah","nahla","female")
member_three = member("omar", "ahmed", "omar","male")

print(member_one.get_all_info())

#print(member.users_num)

member.show_users_count()

member.hello() 


         
        


#class attributes defined outside the constructor 
class member:
    not_allowed_names=["hello","shit"]
    users_num=0

    def __init__(self, first_name, middle_name, last_name , gender):
        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender

        member.users_num+=1
    def full_name(self):
        if self.fname in member.not_allowed_names:
            raise ValueError("Not allowed name")
        else:

            return f"{self.fname} {self.mname} {self.lname}"
    
    def hello(self):
        if self.gender =="male":
            return f"Hello Mr {self.fname}"
        else:
            return f"Hello Mrs {self.fname} "
    def get_all_info(self):
        return f" {self.hello()}, Your full name is {self.full_name()} "
    
    def delete_user(self):
        member.users_num -=1
        return f"User {self.fname} is deleted"

member_one = member("salma", "sherif", "atta","female")
member_two = member("ola", "abdallah","nahla","female")
member_three = member("omar", "ahmed", "omar","male")
member_four =member ("shit","salma","ahmed","male")

print(member.users_num)
#print(member_three.get_all_info())
print(member_four.delete_user())

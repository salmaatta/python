class member:
    def __init__(self, first_name, middle_name, last_name , gender):
        self.fname = first_name

        self.mname = middle_name

        self.lname = last_name

        self.gender = gender
    def full_name(self):
        return f"{self.fname} {self.mname} {self.lname}"
    
    def hello(self):
        if self.gender =="male":
            return f"Hello Mr {self.fname}"
        else:
            return f"Hello Mrs {self.fname} "
    def get_all_info(self):
        return f" {self.hello()}, Your full name is {self.full_name()} "


member_one = member("salma", "sherif", "atta","female")
member_two = member("ola", "abdallah","nahla","female")
member_three = member("omar", "ahmed", "omar","male")

#print(member_one.fname,member_one.mname,member_one.lname)
#print(member_two.fname)
#print(member_three.fname)
#print(member_three.full_name())
#print(member_three.hello())
print(member_three.get_all_info())
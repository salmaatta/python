class skill:
    def __init__(self):
        self.skills = ["c++","html","python"]

    def __str__(self):
        return f"This is my skills=>{self.skills}"
    
    def __len__(self):
        return len(self.skills)

profile = skill()
print(profile)
print(len(profile))

profile.skills.append("php")
print(len(profile))


#mystr = "salma"
#print(str.upper(mystr))


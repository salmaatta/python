name="salma"
country="Egypt"
course= "python"
course_price= 100
student="true"
if country =="Egypt" or country =="ksa" or country=="qatar":
    print(f"Hi { name} because u r from {country}")
    if student =="true":
        print(f"the\"{course}\"discount is %{course_price-80}")
    else:
        print("you don't have a discount") 




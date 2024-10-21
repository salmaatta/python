def addition (n1 , n2):
    if type(n1)!= int or type(n2)!=int:
        print("only integers allowed")
    else :
        print(n1+n2)

addition(int(input("Enter a number")),int(input("Enter another number")))
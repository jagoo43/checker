character=input("okease enter your character")
if character>="0" and character<="9":
    print("your charcter is a number")
elif character>="a" and character<="z" or character>="A" and character<="Z":
    print("your character is an alphabhet")
else:
    print("your chracter is a unique character")
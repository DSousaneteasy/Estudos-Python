value=input("Type less than 6 characters:")
LetterNum=1
for Letter in value:
    print("Letter", LetterNum, "is", Letter)
    LetterNum+=1
else:
    print("the string is blank.")

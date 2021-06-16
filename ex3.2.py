score = input("Enter Score: ")
sc = float(score)
if sc <0.0 or sc>1.0:
    print("error")
    quit()
elif sc<0.6:
    print("F")
elif sc>=0.6 and sc<0.7:
    print("D")
elif sc>=0.7 and sc<0.8:
    print("C")
elif sc>=0.8 and sc<0.9:
    print("B")
elif sc>=0.9:
    print("A")

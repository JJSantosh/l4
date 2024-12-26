amt=int(input("Enter amount"))
n1=amt//100
n2=(amt%100)//50
n3=((amt%100)%750)//10
print("notes of rupees 100 are:",n1)
print("notes of rupees 50 are:",n2)
print("notes of rupees 10 are:",n3)
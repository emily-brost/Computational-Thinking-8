# Beginning: create variables
Emily = 0
Emma = 0


# Middle: ask questions
print("")
print("Are you more like Emma or Emily?")
print("")


answer = input("Do you prefer A) hearts, or B) stars?   ")
if answer =="A":
    Emily += 1
elif answer =="B":
    Emma += 1


answer = input("Do you prefer A) dark red, or B) light purple?   ")
if answer =="A":
    Emma += 1
elif answer =="B":
    Emily += 1


answer = input("Do you prefer listening to A) Olivia Rodrigo, or B) Sabrina Carpenter?   ")
if answer =="A":
    Emily += 1
elif answer =="B":
    Emma += 1


answer = input("Would you name you dog A) Lilo, or B) Colby?   ")
if answer =="A":
    Emma += 1
elif answer =="B":
    Emily += 1


answer = input("Do you prefer watching A) The Office, or B) Friends?   ")
if answer =="A":
    Emily += 1
elif answer =="B":
    Emma += 1


# End: determine results
print("")

if Emily > Emma:
    print("You are more like Emily!")
elif Emma > Emily:
    print("You are more like Emma!")
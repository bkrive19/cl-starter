def clear(): 
    from os import system, name 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')
clear()
print("In this story- you can't choose where you were born. You can't choose how you were born.")
print("Here... you are a Teragate. A race that is in a far, unreachable location.")
print ("In a dimension filled with organic materials that your race can eat. You being born from a mother tree just like everyone else. Your race has been living in boredom for centuries.")
print('But then one day...')
print("A rip was revealed in your world. This rip is something that'll change your race's way of living FOREVER.")
print("You see Teragates gathering around this dimensional rip...")

def gotorip():
    answer=input("Will you follow them? yes or no?")
    if answer == "yes":
         print("You Went to see what's up.")
         rip()
         pass
    elif answer =="no":
        print("You ignored the excitement.")
        end1()
    else:
        print("yes or no?")
        gotorip()
        pass
gotorip()
pass

def end1():
    print("You went back to go eat. After a couple of hours you noticed that everyone was gone... You realize your alone.")
    wait()
    def wait():
        answer = input ("Will you wait for them, or do you want to check out your mother tree? Check, or wait?")
    if answer == "check":
        print("You went to go check the tree that gae birth to you.")
        birthplace()
        pass
    elif answer == "wait":
        print("You waited a day later. No one came.")
        wait()
    else:
        print ("check or wait?")
        wait()

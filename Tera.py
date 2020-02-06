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

def firstbite():
    print(" ")
    print("Finally after years of boredom- your free! Your in a black place..")
    print ("You see light. You walk towards it, but for some reason you feel lighter in mass.")
    print("Your out! There's a lot of organic material- like in your world, but green and delicate, more alive. You realize that your're a ghost..")
    print(" ")
    answer = input ("You see a slow animal and a berry bush. Will you perfer a plant, or an easy meat meal?")
    if answer == "meat"
    print ("You ate the animal alive. You start to gain mass- your----------------")



def rip():
    print(" ")
    print("Every one is just celebrating! You see some Teragates fall in the rip, and some jump in and out, but they seem tranparent now...")
    answer = input ("You really want to see what's beyond the rip. go, or stay?")
    if answer == "stay":
        end1()
    elif answer == "go": 
        firstbite()
        
    else:
        print("go or stay?")
        rip()

def birthplace():
    print(" ")
    print("You went back to the tree. The tree that gives birth to your race. You're the fruit of the tree. The only one now...")
    print("You waited there for an hour. Waiting for something to happen. Then....")
    print(" ")
    print("The tree speaks! Saying in a soft accent,- YOU ARE THE ONLY CHILD I HAVE WHO CARED TO COME AND VISIT ME BEFORE LEAVING.")
    print("I'M GLAD YOU KNOW WHO GAVE BIRTH TO YOU. SEAL THE RIP AND COME AND EAT WITH ME...")
    from pyfiglet import Figlet

    fig = Figlet(font='graffiti')
    banner = fig.renderText("SECRET end")

    print(banner)



def end1():
    print(" ")
    print("You went back to go eat. After a couple of hours you noticed that everyone was gone... You realize your alone.")
    wait()

def wait():
    answer = input ("Will you wait for them, or do you want to check out your mother tree? Check, or wait?")
    if answer == "check":
        print("You went to go check the tree that gae birth to you.")
        birthplace()
        
    elif answer == "wait":
        print("You waited a day later. No one came.")
        wait()

    else:
        print ("check or wait?")
        wait()
        
def gotorip():
    answer=input("Will you follow them? yes or no?")
    if answer == "yes":
         print("You Went to see what's up.")
         rip()
        
    elif answer =="no":
        print("You ignored the excitement.")
        end1()
    else:
        print("yes or no?")
        gotorip() 
gotorip()


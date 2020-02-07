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

def killpoint():
    x=0


def k4():
    print(" ")
    print("The Teragate looks really mad that you took the child, so he runs off- but you hear more screaming, so you followed the screaming")
    print("You manage to reach the Teragates prey. They are all little kids. You and the Teragate are staring at eachothers eyes- he looks as strong as you.")
    answer =input ("Will you kill and eat the kids for yourself, or will you save them and kill the Teragate? Who will you kill- the kids or the teragate? ")
    if answer =="kids":
        print("You consumed all of them- very quick. Your body reinforeces its self. You've grown stronger. You decide to kill the Teragate as well")
        print("His shock and fear taste just as good as the kids!")
        killpoint() +=4
        print(x)
        end()
        pass
    elif answer =="teragate":
        print("You have a brawl with him. You took three blows- you returned the punches. You're leaking red liquid- so is the Teragate...")
        print("Finally- your so close to dieing, but you killed one of your kind to save the kids. You realized that they all ran off while you were fighting...")
        end()
        pass
    else:
        print("teragate, or the kids?!")
        k4()

def k3():
    print(" ")
    print("You hear a child's voice screaming for help- you start to run towards it while avoiding the main public path.")
    print("There is a little boy running from another Teragate- He's running towards your direction.")
    answer = input (" Will you kill him or will you help him? eat, or help?")
    if answer =="kill":
        print("You killed the little thing- his screams and fear taste so good! You feel very strong.")
        killpoint() +=1
        print(x)
        k4()
        
    elif answer == "help":
        print ("You grabbed him- he is scared, so you pet him. The Tearagate looks really mad, so you ran off to bring the child to a safe publical place.")
        k4()
        
    else:
        print("kill or help? What are you going to do to him?")
        k3()



def k2():
    print(" ")
    print("You move on. You're now exploring in the forest. You see another person, but they see you! They are scared- will you eat her, or spare her?")
    answer = input ("Kill, or spare?")
    if answer =="kill":
        print("You killed her. She's screaming in fear. It tastes so good- you gained some short claws. Later you hear a child calling for help")
        killpoint() += 1
        print (x)
        k3()
        
    elif answer == "spare":
        print ("You show a gesture of mercy. She is very suprised that you have some emotion. She takes a picture and some notes, but she heard someone calling her name for help- she runs off.")
        k3()
    else:
        print("kill or spare!")
        k2()


def k1():
    print(" ")
    print ("You see an animal, but it looks smart- if not maybe as smart as you.")
    print ("You realize eating from a new dimension makes you stronger. The person doesn't see you...")
    answer = input ("Do you want to kill him??? Kill or don't kill? ")
    if answer =="kill":
        print("You killed the person. You can see it's pain and fear- it taste good. You gained some teeth.")
        killpoint() += 1
        print (x)
        k2()
        
    elif answer == "don't kill":
        print ("You spared the being. You just spectated it- he's picking up a little girl from a cabin. You feel like you made a right choice.")
        k2()
        
    else:
        print("kill or don't kill!")
        k1()

def firstbite():
    print(" ")
    print("Finally after years of boredom- your free! Your in a black place..")
    print ("You see light. You walk towards it, but for some reason you feel lighter in mass.")
    print("Your out! There's a lot of organic material- like in your world, but green and delicate, more alive. You realize that your're a ghost..")
    print(" ")
    answer = input ("You see a slow animal and a berry bush. Will you perfer a plant, or an easy meat meal?")
    if answer == "meat":
        print ("You ate the animal alive. You start to gain mass- your ghost forms a skeleton and fresh flesh for your new body!")
        k1()
        
    elif answer == "plant":
        print("You ate the berries. Your ghost forms a skeleton and some fresh flesh around your hip and head.")
        k1()
        
    else:
        print("plant, or meat. Eat, so you can materialize!")
        firstbite()


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


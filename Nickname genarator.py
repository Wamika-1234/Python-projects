import random
personality=["Nice","Annoying", "Arrogant", "Shy", "Cruel", "Tame", "Bold"]
Nice=[" Wet blanket","The nice one","Nice person"]
Annoying=["Flea","Rat","Microorganisim"]
Arrogant=["The witch","The cruel one","Trash bag"]
Shy=["Mouse","Hamster","The shy one"]
character=(input("What kind of person are you? Are you Nice,Annoying,Arrogant or Shy"))
first_name=(input("What is your fist name?"))
last_name=(input("What is your last name?"))
if character=="Nice":
    print("Your nickname is ",first_name, random.choice(Nice), last_name )
elif character=="Arrogant":
    print("Your nickname is ",first_name, random.choice(Arrogant), last_name )
elif character=="Annoying":
    print("Your nickname is ",first_name, random.choice(Annoying), last_name )
elif character=="Shy":
    print("Your nickname is ",first_name, random.choice(Shy), last_name )
else:
    print("You did not choose the right personality")
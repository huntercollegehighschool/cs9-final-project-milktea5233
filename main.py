"""
Name(s): Rachel Chen
Name of Project: Escape Room
"""
import os 
print("Storyline: The notorious serial killer known as Barry the Chopper was imprisoned fifteen years ago. Now, he has escaped, and you—the citizen who saw him on the run and reported him to the police—are his next victim. You have been chased into an abandoned office building, where Barry was once employed before turning to murder, and the front entrance has just caved in on itself. The only way out is through the back entrance, but it was locked many years ago, and you don't know the password to get out. Find the password to the keypad and escape the building...before Barry finds you first.")
print("\n")
print("Are you ready? You may wish to have a paper and pencil to take notes.") 
start = input("\nEnter 1 to begin and 2 to exit. ")
inventory_items = []
codereplace = []
newcode = 0
key1 = "Silver key"
paper = "Paper slip"
photo = "Photo"
key2 = "Bronze key"
note = "Sticky note"
a = ["a"]
b = 0
c = []


def cubicle1():
  print("There's an office chair and a desk. Enter 1 to sit in the chair. Enter 2 to examine the desk. Enter 3 to exit the cubicle. ")
  cubicle_one = input("\nEnter your choice here: ")
  if cubicle_one == "1":
    os.system('clear')
    print("You sit down. It's not a very comfortable chair. If you were the one using this cubicle, you would've brought a pillow or two.")
    print("\n")
    cubicle1()
  elif cubicle_one == "2":
    os.system('clear')
    print("A name plate on the desk reads: 'Employee #25'. You go through each of the three drawers in the desk. They're all empty, except for some used tissues. Ew.")
    print("\n")
    cubicle1()
  elif cubicle_one == "3":
    os.system('clear')
    cubicles()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    cubicle1()
def cubicle2():
  print("There's an office chair, a desk, a calendar, and a wastebasket. Enter 1 to sit in the chair. Enter 2 to examine the desk. Enter 3 to look through the calendar. Enter 4 to look through the wastebasket. Enter 5 to exit the cubicle. ")
  cubicle_two = input("\nEnter your choice here: ")
  if cubicle_two == "1":
    os.system('clear')
    print("You sit in the chair. It creaks loudly, and you hesitatantly spin around on its wheels for a second. You hear a snap, and then the chair breaks. You fall to the ground. Oops.")
    print("\n")
    cubicle2()
  if cubicle_two == "2":
    os.system('clear')
    if paper not in inventory_items:
      print("A name plate on the desk reads, 'Employee #66.' Two of the drawers are empty. A third drawer is locked. Would you like to try unlocking it? Enter 1 if yes. Enter 2 if not. ")
      drawer = input("\nEnter your choice here: ")
      if drawer == "1":
        if key1 in inventory_items or key2 in inventory_items:
          os.system('clear')
          print("Inventory: ", inventory_items)
          print("\n")
          drawer_key = input("What key would you like to use? ")
          if drawer_key == "Silver key":
            os.system('clear')
            print("The drawer unlocks. There's a slip of paper that says, 'It should've been me.' What could that mean?")
            inventory_items.append(paper)
            print("\nItem obtained: Paper slip. Check your inventory to see what you have.")
            print("\n")
            cubicle2()
          elif drawer_key == "Bronze key":
            os.system("clear")
            print("It doesn't seem like this key fits. Try a different key.")
            print("\n")
            print("A name plate on the desk reads, 'Employee #66.' Two of the drawers are empty. A third drawer is locked. Would you like to try unlocking it? Enter 1 if yes. Enter 2 if not. ")
            drawer = input ("\nEnter your choice here: ")
          else:
            os.system('clear')
            print("You can't unlock the drawer with that. Come back with the right key.")
            print("\n")
            cubicle2()
        elif key1 not in inventory_items and key2 not in inventory_items:
          os.system('clear')
          print("You don't have any keys in your inventory. Come back when you've obtained a key.")
          print("\n")
          cubicle2()
        else:
          os.system('clear')
          print("That's not a valid course of action.")
          print("\n")
          cubicle2()
      if drawer == "2":
        os.system("clear")
        cubicle2()
      else:
        os.system('clear')
        print("That's not a valid course of action.")
        print("\n")
        cubicle2()
    if paper in inventory_items:
      os.system("clear")
      print("A name plate on the desk reads, 'Employee #66. The drawers are empty.")
      print("\n")
      cubicle2()
  if cubicle_two == "3":
    os.system('clear')
    print("The calendar has no marked dates. Weird. What's the point of having a calendar if they didn't even use it?")
    print("\n")
    cubicle2()
  if cubicle_two == "4":
    os.system('clear')
    print("There's a crumpled up sheet of paper. You pull it out of the wastebasket. It's a page from the calendar. When you smooth it out, you see that January 19th, 1999 is circled. Underneath, it reads, 'Promotion!'")
    print("\n")
    cubicle2()
  if cubicle_two == "5":
    os.system('clear')
    cubicles()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    cubicles()  
def cubicle3():
  print("There's an office chair, a desk, and a small cabinet on the desk. Enter 1 to sit in the office chair. Enter 2 to examine the desk. Enter 3 to look through the cabinet. Enter 4 to exit the cubicle. ")
  cubicle_three = input("\nEnter your choice here: ")
  if cubicle_three == "1":
    os.system('clear')
    print("You sit down in the chair. There's nothing special here. Maybe you should stop wasting time...before Barry finds you.")
    print("\n")
    cubicle3()
  elif cubicle_three == "2":
    os.system('clear')
    if photo not in inventory_items:
      if b not in c:
        print("A nameplate on the desk reads, 'Employee #65.' There's a photo frame on the desk. You pick it up to look at it more closely. There's a man smiling widely at the camera, and he has an arm around someone else's shoulder. You freeze when you notice who the other person is: Barry. Who is the smiling man, and how did he know Barry?") 
        inventory_items.append(photo)
        print("\nItem obtained: 'Photo.' Check your inventory to see what you have.")
        print("\n") 
        cubicle3()
      elif b in c:
        print("A nameplate on the desk reads, 'Employee #65.' There's a photo frame on the desk. You pick it up to look at it more closely. There's a man smiling widely at the camera, and he has an arm around someone else's shoulder. You freeze when you notice who the other person is: Barry. Upon further inspection, you realize that the other man is in one of the Employee of the Year photos. How did they know each other?")
        inventory_items.append(photo)
        print("\nItem obtained: 'Photo.' Check your inventory to see what you have.")
        print("\n") 
        cubicle3()
    if photo in inventory_items:
      os.system("clear")
      print("A nameplate on the desk reads, 'Employee #65. There's a scribble on the desk that reads, 'I hate my job.' It seems really boring to work in an office.")
      print("\n")
      cubicle3()
  elif cubicle_three == "3":
    if key2 not in inventory_items:
      os.system("clear")
      print("Most of the cabinets are empty. Inside one of them, however, is a box with a combination lock on it. Would you like to try unlocking it? Enter 1 if yes. Enter 2 if no. ")
      cabinetbox = input("\nEnter your choice here: ")
      if cabinetbox == "1":
        os.system('clear')
        boxlock = input("Enter the 4-digit password: ")
        if boxlock == "0119":
          print("The box unlocks. Inside is a small, bronze key. What's this for?")
          inventory_items.append(key2)
          print("\n")
          print("Item obtained: Bronze key. Check your inventory to see what you have.")
          print("\n")
          cubicle3()
        elif boxlock != "0119":
          os.system('clear')
          print("That's not the right code.")
          print("\n")
          cubicle3()
      elif cabinetbox == "2":
        os.system("clear")
        cubicle3()
      else:
        os.system("clear")
        print("That's not a valid course of action.")
        cubicle3()
    if key2 in inventory_items:
      os.system("clear")
      print("The cabinets are really dusty, and you sneeze.")
      print("\n")
      cubicle3()
  elif cubicle_three == "4":
    os.system("clear")
    print("\n")
    cubicles()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    cubicles()
def cubicle4():
  print("There's an office chair and a desk. Enter 1 to sit in the chair. Enter 2 to examine the desk. Enter 3 to exit the cubicle. ")
  cubicle_four = input("\nEnter your choice here: ")
  if cubicle_four == "1":
    os.system('clear')
    print("You sit down in the chair. The leather is old and torn. This office really needs better chairs.")
    print("\n")
    cubicle4()
  elif cubicle_four == "2":
    os.system('clear')
    print("A nameplate on the desk reads, 'Employee #89.' The desk is empty, and so are its drawers. There's nothing here.")
    print("\n")
    cubicle4()
  elif cubicle_four == "3":
    os.system('clear')
    print("\n")
    cubicles()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    cubicles()
def cubicles():
  print("There are four cubicles in the room. Enter 1 to examine the first cubicle. Enter 2 to examine the second cubicle. Enter 3 to examine the third cubicle. Enter 4 to examine the fourth cubicle. Enter 5 to interact with something else. ")
  pick_cubicle = input("\nEnter your choice here: ")
  if pick_cubicle == "1":
    os.system("clear")
    cubicle1()
  elif pick_cubicle == "2":
    os.system("clear")
    cubicle2()
  elif pick_cubicle == "3":
    os.system("clear")
    cubicle3()
  elif pick_cubicle == "4":
    os.system("clear")
    cubicle4()
  elif pick_cubicle == "5":
    os.system("clear")
    game()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    cubicles()
def window():
   os.system('clear')
   print("You peer out the first floor window carefully. The sun is beginning to set, and you fearfully wonder what will happen to you when nighttime comes.")
   print("\n")
   returntogame = input("Enter any key to return to the room. ")
   if returntogame == "a":
     game()
   else:
     game()
def plants():
  if newcode not in codereplace: 
    print("There's a potted plant underneath the keypad. Enter 1 to try and move the plant. Enter 2 to examine the plant more closely. Enter 3 to interact with something else. ")
    plant_action = input("\nEnter your choice here: ")
    if plant_action == "1":
      os.system('clear')
      print("You struggle to push the potted plant for a moment. It's surprisingly heavy. After a few moments, you scoot it far enough and discover a panel in the wall. There's a keyhole, and after trying the door, you find that it's locked. Maybe the key is somewhere in the room...")
      codereplace.append(newcode)
      print("\n")
      plants()
    elif plant_action == "2":
      os.system('clear')
      if key1 in inventory_items:
        os.system('clear')
        print("The leaves are looking a little dry. Someone should water this plant more.")
        print("\n")
        plants()
      elif key1 not in inventory_items:
        os.system('clear')
        print("You examine the leaves and stalks of the plant. Suddenly, a glint of light catches your eye. You reach into the plant and find a silver key. What could it be used for?")
        inventory_items.append(key1)
        print("\n")
        print("Item obtained: 'Silver key.' Check your inventory to see what you have.")
        print("\n")
        plants()
    elif plant_action == "3":
      game()
    else:
      os.system('clear')
      print("That's not a valid course of action.")
      print("\n")
      plants()
  if newcode in codereplace:
    print("Enter 1 to examine the plant more closely. Enter 2 to interact with something else. ")
    plant_action = input("\nEnter your choice here: ")
    if key1 in inventory_items:
      if plant_action == "1":
        os.system('clear')
        print("The leaves are looking a little dry. Someone should water this plant more.")
        print("\n")
        plants()
      elif plant_action == "2":
        game()
      else:
        os.system("clear")
        print("That's not a valid course of action.")
        print("\n")
        plants()
    elif key1 not in inventory_items:
      if plant_action == "1":
        os.system('clear')
        print("You examine the leaves and stalks of the plant. Suddenly, a glint of light catches your eye. You reach into the plant and find a silver key. What could it be used for?")
        inventory_items.append(key1)
        print("\n")
        print("Item obtained: 'Silver key.' Check your inventory to see what you have.")
        print("\n")
        plants()
      elif plant_action == "2":
        game()
      else:
        os.system("clear")
        print("That's not a valid course of action.")
        print("\n")
        plants()
def photos():
  print("There are four photos hanging on the wall, each captioned 'Employee of the Year.' Enter 1 to examine the first photo up close. Enter 2 to examine the second photo up close. Enter 3 to examine the third photo up close. Enter 4 to examine the fourth photo up close. Enter 5 to interact with something else. ")
  photo_action = input("\nEnter your choice here: ")
  if photo_action == "1":
    os.system("clear")
    print("A duck wearing a sailor's hat is in the photo. In the caption, it reads: 'Donald Duck. Employee #45. Employee of the Year: 1996.'")
    print("\n")
    photos()
  elif photo_action == "2":
    os.system("clear")
    print("A older man with a severe expression is in the photo. In the caption, it reads, 'James Bond. Employee #71. Employee of the Year: 1998.'")
    print("\n")
    photos()
  elif photo_action == "3":
    os.system("clear")
    print("A man wearing glasses and a red tie smiles in the photo. In the caption, it reads, 'Tony Fisher. Employee #80. Employee of the Year: 1997.'")
    print("\n")
    photos()
  elif photo_action == "4":
    c.append(b)
    if photo in inventory_items:
      os.system("clear")
      print("A lanky man with searing-red hair is in the photo. You squint at the image for a second, wondering why he looks familiar. Then, you realize: it's the same man in the photo with Barry. In the caption, it reads, 'Ronald McDonald. Employee #65. Employee of the Year: 1999.'")
      print("\n")
      photos()
    elif photo not in inventory_items:
      os.system("clear")
      print("A lanky man with searing-red hair is in the photo. In the caption, it reads, 'Ronald McDonald. Employee #65. Employee of the Year: 1999.'")
      print("\n")
      photos()
  elif photo_action == "5":
    game()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    photos()

def keypad():
  guesses = len(a)
  print("Enter the 8-digit code. Warning: once you reach three failed attempts, an alarm will go off. Alternatively, enter R to interact with something else. ")
  keypad_code = input("\nEnter the code here: ")
  while keypad_code != '45807166' and keypad_code != 'R' and guesses < 3:
    os.system('clear')
    print('Incorrect passcode. You have', 3 - guesses, "guess(es) left.")
    print("\n")
    print("Enter the 8-digit code. Warning: once you reach three failed attempts, an alarm will go off. Alternatively, enter R to interact with something else. ")
    keypad_code = input("\nEnter the code here: ")
    guesses = guesses + 1
    a.append("b") 
  if keypad_code == '45807166':
    os.system('clear')
    print("The door unlocks, and you race out of the room just as a crash sounds behind you. As you look over your shoulder, Barry the Chopper grins behind you, having just broken through the collapsed front door. You slam the door shut behind you and run through the streets. You may have made it out of the room, but you're not free of Barry just yet. The end.")
  elif keypad_code != "R" and guesses == 3:
    os.system('clear')
    print("An alarm sounds, and you freeze. You desperately hit the keypad, trying to get the alarm to shut off, but it doesn't seem like that's where the speaker is. You hear crashing from behind you, and moments later, Barry the Chopper breaks through the remnants of the front door. He grins, sending chills down your spine, and you've only just opened your mouth to scream when he throws a large butcher knife at you, and everything goes dark. The end.")
  elif keypad_code == "R":
    game()

def panel():
  if note not in inventory_items:
    print("Would you like to try unlocking the panel? Enter 1 if yes. Enter 2 if not. ")
    panel_action = input("\nEnter your choice here: ")
    if panel_action == "1":
      if key1 in inventory_items or key2 in inventory_items:
        os.system("clear")
        print("Inventory: ", inventory_items)
        print("What key would you like to use? Please enter the item name as it is written in your inventory. ")
        panel_key = input("\nEnter your choice here: ")
        if panel_key == "Bronze key":
          os.system("clear")
          print("The panel unlocks. The inside of it is a small, hollowed-out section in the wall. It seems like it's empty for a moment, but then you notice a folded up sticky note inside. You take it out and open it. It reads, 'They're in the wrong order. Remember, age before beauty. '")
          inventory_items.append(note)
          print("\n")
          print("Item obtained: Sticky note. Check your inventory to see what you have.")
          print("\n")
          exit = input("Enter any key to interact with something else. ")
          if exit == "a":
            game()
          else:
            game()
        elif panel_key == "Silver key":
          os.system("clear")
          print("Hm...it doesn't look like this key fits. Try something else instead.")
          print("\n")
          panel()
        else:
          os.system("clear")
          print("You can't unlock the panel with that. Come back with the right key.")
          print("\n")
          panel()
      elif key1 not in inventory_items or key2 not in inventory_items:
        os.system("clear")
        print("You don't have any keys in your inventory. Come back when you've obtained a key.")
        print("\n")
        game()
    if panel_action == "2":
      game()
    else:
      os.system('clear')
      print("That's not a valid course of action.")
      print("\n")
      panel()
  if note in inventory_items:
    print("There's an empty cobweb inside the panel. This place seems pretty old.")
    print("\n")
    game()
def inventory():
  print("Inventory: ", inventory_items)
  print("Which item would you like to interact with? Please enter the item name as it is written in your inventory. Alternatively, enter R to return to the room. ")
  inventory_action = input("\nEnter your choice here: ")
  if inventory_action == "Silver key" and key1 in inventory_items:
    os.system("clear")
    print("Silver key: A key you found in the potted plant.")
    print("\n")
    inventory()
  elif inventory_action == "Paper slip" and paper in inventory_items:
    os.system("clear")
    print("Paper slip: A piece of paper you found in the locked drawer of the second cubicle. It reads, 'It should've been me.")
    print("\n")
    inventory()
  elif inventory_action == "Bronze key" and key2 in inventory_items:
    os.system("clear")
    print("Bronze key: A key you found in a locked box inside a cabinet in the third cubicle.")
    print("\n")
    inventory()
  elif inventory_action == "Photo" and photo in inventory_items:
    if b not in c:
      os.system("clear")
      print("Photo: A photo you found on the desk in cubicle three. In the photo, an unknown man has his arm around the shoulder of Barry the Chopper. They look like they're good friends.")
      print("\n")
      inventory()
    if b in c:
      os.system("clear")
      print("Photo: A photo you found on the desk in cubicle three. In the photo, Ronald McDonald, one of the Employees of the Year, has his arm around the shoulder of Barry the Chopper. They look like they're good friends.")
      print("\n")
      inventory()
  elif inventory_action == "Sticky note" and note in inventory_items:
    os.system("clear")
    print("Sticky note: A sticky note you found in the hidden panel. It reads, 'They're in the wrong order. Remember, age before beauty.'")
    print("\n")
    inventory()
  elif inventory_action == "R":
    game()
  else: 
    os.system("clear")
    print("That's not an item in your inventory.")
    print("\n")
    inventory()
def game1():  
  os.system('clear')
  print("Enter 1 to interact with the cubicles. Enter 2 to interact with the windows. Enter 3 to interact with the potted plants. Enter 4 to interact with the photos on the wall. Enter 5 to interact with the keypad by the door. Enter 6 to interact with the hidden panel. Enter 7 to access your inventory.")
  choice = input("\nEnter your choice here: ")
  if choice == "1":
    os.system('clear')
    cubicles()
  elif choice == "2":
    os.system('clear')
    window() 
  elif choice == "3":
    os.system('clear')
    plants()
  elif choice == "4":
    os.system('clear')
    photos()
  elif choice == "5":
    os.system('clear')
    keypad()
  elif choice == "6":
    os.system('clear')
    panel()
  elif choice == "7":
    os.system('clear')
    inventory()
  else:
    os.system('clear')
    print("That's not a valid course of action.")
    print("\n")
    print("Enter 1 to interact with the cubicles. Enter 2 to interact with the windows. Enter 3 to interact with the potted plants. Enter 4 to interact with the photos on the wall. Enter 5 to interact with the keypad by the door. Enter 6 to interact with the hidden panel. Enter 7 to access your inventory.")
    choice = input("\nEnter your choice here: ")
def game():
  if start == "1":  
    if newcode in codereplace:
      game1()
    if newcode not in codereplace:
      os.system('clear')
      print("Enter 1 to interact with the cubicles. Enter 2 to interact with the windows. Enter 3 to interact with the potted plants. Enter 4 to interact with the photos on the wall. Enter 5 to interact with the keypad by the door. Enter 6 to access your inventory.")
      choice = input("\nEnter your choice here: ")      
      if choice == "1":
        os.system('clear')
        cubicles()
      elif choice == "2":
        os.system('clear')
        window() 
      elif choice == "3":
        os.system('clear')
        plants()
      elif choice == "4":
        os.system('clear')
        photos()
      elif choice == "5":
        os.system('clear')
        keypad()
      elif choice == "6":
        os.system('clear')
        inventory()
      else:
        print("That's not a valid course of action.")
        print("\nEnter 1 to interact with the cubicles. Enter 2 to interact with the windows. Enter 3 to interact with the potted plants. Enter 4 to interact with the photos on the wall. Enter 5 to interact with the keypad by the door. Enter 6 to access your inventory.")
        choice = input("\nEnter your choice here: ")
  elif start == "2":
    os.system("clear")
    print("What a shame. Maybe Barry the Chopper will greet you some other night...")
  else:
    os.system("clear")
    print("That's not a valid response. Come back when you've made up your mind.")
    
game()

#Write the main part of your program here. Use of the other pages is optional.

#import page1  # uncomment if you're using page1
#import page2  # uncomment if you're using page2
#import page3  # uncomment if you're using page3
#import page4  # uncomment if you're using page4
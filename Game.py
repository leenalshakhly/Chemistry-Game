import sys
import time

#This is the code for the second ingredient of the experiment
def stagetwo():
  while True:
    #introduction to second stage
    print("Stage 2")
    print("Welcome " +name+ " to the second level of this academy!")
    time.sleep(1)
    print("What substances do you want to use for your first experiment?")
    print("You have four choices: Nickel, Iron, and Chromium")
    ingredient2 = input()
    #choices for second ingredient of experiment
    ingredient2list = ["nickel", "iron", "chromium"]
    if ingredient2.lower() in ingredient2list:
      #if user chooses nickel as their second ingredient which is the wrong choice and will kill you
      if ingredient2.lower() == "nickel":
        print("You decide not to use gloves on this experiment...")
        time.sleep(1)
        print("The nickel spills all over your hands! You think its okay and decide to try this experiemnt later!")
        print("Hours go by and your hands are now all puffy and blue...")
        print("You decide to go to the nurse in your academy and she says...")
        time.sleep(2)
        print("We need to cut off both of your hands before the poison spread all over your body!!")
        print("Now you have no hands and eventually die due to the poisoning of the nickel.")
        print("Would you like to start again?")
        #If user wants to replay the game
        replay = input()
        if replay.lower() == "no":
          sys.exit()
        if replay.lower() == "yes":
          continue
      #if user chooses iron as their second ingredient which is the wrong choice and will kill you
      if ingredient2.lower() == "iron":
        print("You brought your food to the lab")
        print("You werent careful, and iron spilled all over the table and...")
        time.sleep(1)
        print("Your food is now contaminated!")
        print("But...you don't know its contaminated..")
        time.sleep(2)
        print("You clean your mess, and take your food outside!")
        print("You take a bite, and get a sense that something is wrong with your food but...")
        time.sleep(1)
        print("You don't care! Hours go by and you start to have abdominal pain")
        print("Do you ask for help or continue your day with an abdominal pain")
        choices = input("")
        #Choices for what to do with iron side effects of whether to ask for help or to just leave it alone
        if choices == 'ask for help':
          print("You ask one of your friends for advice...")
          time.sleep(1)
          print("They tell you to get medical advice!")
          print("You go to the nurse, and inform her on what happened!")
          print("She calls the ambulance and you are now rushed to the hospital!")
          print("You stay there for days, but due to your bad immunity...")
          print("You begin to have organ failure and DIE ALONE!")
          print("Would you like to start again?")
          #If user wants to replay the game
          replay = input()
          if replay.lower() == "no":
            sys.exit()
          if replay.lower() == "yes":
            continue
        if choices.lower() == "continue day":
          print("Your abdominal pain gets worse...")
          time.sleep(1)
          print("You begin to vomit BLOOD!!!")
          time.sleep(1)
          print("As you hit your head to the ground, you begin to find it hard to breathe...")
          time.sleep(1)
          print("You began to internal bleed and before you know it...")
          print("YOU DIED 💀☠️!!!")
      #if user chooses chromium as their second ingredient which is the correct choice to win the game
      if ingredient2.lower() == "chromium":
        print("You perfectly poured the chromium into the beaker...")
        time.sleep(2)
        print("A few seconds goes by..")
        time.sleep(1)
        print("The BEAKER begins to SHAKE!!!!")
        time.sleep(1)
        print("You think an explosion will occur!")
        time.sleep(1)
        print("But, guess what...")
        print("You did the experiment perfectly! Good Job!")
        print("""The magnesium and the chromium mixed perfectly creating 
        a new gooey substance that's red. You're the first person in history
        to create this new substance what would you like to call it?""")
        substance = input()
        print("""You have called it: " +substance + "! Great job young scientist! 
        May this be the start of your scientific journey, so go on and discover!""")
        time.sleep(5)
        print("Thank you for playing the game.")
        sys.exit()


if __name__ == "__main__":
  #The start of the game and the introduction for the whole game
  while True:
    print("Let's start with your name: ")
    name = input()
    print("Welcome " +name+ ",to Tiede Academy!")
    print("Congratulations on being admitted to one of the most prestigious science academies in the world!")
    print("Would you like to start your experiment?")
    experiment = input()
    if experiment == "yes":
       #if user chooses iron as their second ingredient which is the wrong choice and will kill you
       print("What substances do you want to use for your first experiment?")
       print("You have four choices: Zinc, Neon, Cobalt and Magnesium")
       ingredient1 = input()
       ingredient1list = ["zinc", "neon", "cobalt", "magnesium"]
       if ingredient1.lower() in ingredient1list:
       #if user chooses zinc as their first ingredient which is the wrong choice and will kill you
        if ingredient1.lower() == "zinc":
          print("You put the zinc in the beaker and then left the room since your stomach was grumbling. You bought a peanut butter sandwich and smelled a gas. You suppose it isn't yours, but people started whispering that it originated from room 101. You start to worry after some of your classmates pass out, because room 101 was your lab room. You wonder what is causing your peers to pass out. It takes a few moments for you to realize, you've just produced a gas known as CARBON MONOXIDE! The quiet assassin! By the time you reach to ask help, you die.")
          print("Would you like to start again?")
          #If user wants to replay the game
          replay = input()
          if replay.lower() == "no":
            sys.exit()
          if replay.lower() == "yes":
            continue
        #if user chooses neon as their first ingredient which is the wrong choice and will kill you
        if ingredient1.lower() == "neon":
          print("You put neon in the beaker but you're not careful...")
          time.sleep(3)
          print("The neon starts replacing the oxygen in the room. You begin to suffocate, your throat starts to swell! Before you know it, YOU DIED!!")
          print("Would you like to start again?")
          #If user wants to replay the game
          replay = input()
          if replay.lower() == "no":
            sys.exit()
          if replay.lower() == "yes":
            continue
        #if user chooses cobalt as their first ingredient which is the wrong choice and will kill you
        if ingredient1.lower() == "cobalt":
          print("Your not careful with the Cobalt...")
          time.sleep(1)
          print("The Cobalt fell and was shattered into pieces...")
          time.sleep(3)
          print("you start to smell a strange scent in the room as blisters start to appear all over your body. Blood pours from your eyes as you fall to the ground...")
          time.sleep(3)
          print("You start to choke on your blood, as you gasp for air. YOUR BODY STARTS TO CONVULSE as your heart stops and you die.")
          sys.exit()
        if ingredient1.lower() == "magnesium":
          #If the user wanted to choose magnesium,it will run them in a code and wil either get them to past the next step
          print("As you place the magnesium in the beaker CAREFULLY, you get to the ground and cover your head as you prepare for the worst...")
          time.sleep(3)
          print("But nothing happens...Magnesium was the correct ingredient...")
          time.sleep(1)
          print("You can now move to the next stage of the experiment")
          print("press enter")
          stagetwo()
       #if user chooses an ingredient that isn't listed in the list of choices, the code will kill them
       else:
        print("You decided to be adventurous, and decided to throw a random ingredient into the beaker...")
        time.sleep(3)
        print("When you get near the beaker to see what's happening...")
        time.sleep(1)
        print("IT STARTS BUBBLING...")
        time.sleep(1)
        print("The beaker begins to shake and IT EXPLODES INTO A MILLION PIECES AND KILLING YOU!!!")
        print("Do you want to continue?")
        #If user wants to replay the game
        replay = input()
        if replay.lower() == "no":
          sys.exit()
        if replay.lower() == "yes":
          continue
    if experiment.lower() == "no":
      sys.exit()
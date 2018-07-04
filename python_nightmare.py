# Python's Nightmare

# There are 5 room in each house. Use tracker to find out which house is infected
# or not. Use the tracker to avoid Python and to collect all the 8 snakes!

import random, time

chosen = 0
tracker  = random.randint(1, 2)
snakes = 0
h1 = 0
h2 = 0
h3 = 0
h4 = 0
h5 = 0
house1 = random.randint(1, 2)
house2 = random.randint(1, 2)
house3 = random.randint(1, 2)
house4 = random.randint(1, 2)
house5 = random.randint(1, 2)



def winGame():
  global snakes
  time.sleep(2)
  print()
  snakes = str(snakes)
  print("You got "+snakes+"/10 snakes!")
  print()
  time.sleep(2)
  print("CONGRAJULATIONS, YOU WON THE GAME!")
  print()
  time.sleep(1)
  print("Go Brag about it now!")
  time.sleep(1)
  print("      -------        ")
  time.sleep(1)
  print("Creator and Co - Coder: Kaushik")
  time.sleep(1)
  print("Organiser and Logic Giver: Alan")
  time.sleep(1)
  print("Co-Coder: Alex")
  time.sleep(1)
  print("Non-worker: Benjamin (lol)")
  time.sleep(1)
  print()
  print("Thanks for playing!")


def loseGame():
  global house1, house2, house3, house4, house5
  global chosen, tracker, snakes
  global h1, h2, h3, h4, h5
  chosen = 0
  tracker  = 3
  snakes = 0
  h1 = 0
  h2 = 0
  h3 = 0
  h4 = 0
  h5 = 0
  house1 = random.randint(1, 2)
  house2 = random.randint(1, 2)
  house3 = random.randint(1, 2)
  house4 = random.randint(1, 2)
  house5 = random.randint(1, 2)
  time.sleep(1)
  print("YOU LOSE THE GAME BECAUSE THE PYTHON GOT YOU!")
  print("Play Again? (1 = yes, 2 = no)")
  s = input(">>> ")
  if s == "1":
      print()
      startGame()
  else:
      print("Game Closed!")

# This function is not used!
def track():
  global tracker
  if tracker == 0:
    print("You ran out of trackers")
  else:
    if house1 == 2:
      print("House 1 is not safe")
      tracker = tracker - 1
    if house2 == 2:
      print("House 2 is not safe")
      tracker = tracker - 1
    if house3 == 2:
      print("House 3 is not safe")
      tracker = tracker - 1
    if house4 == 2:
      print("House 4 is not safe")
      tracker = tracker - 1
    if house5 == 2:
      print("House 5 is not safe")
      tracker = tracker - 1
  chooseHouse()
# This function is not used!

def chooseHouse():
  global chosen, house1, house2, house3, house4, house5, snakes, tracker
  if snakes >= 10:
      winGame()
  else:
      snakes = str(snakes)
      print("You have "+snakes+"/10 snakes")
      snakes = int(snakes)
      print("Choose house: 1, 2, 3, 4, 5. Type 't' or 'track' to use your tracker to see where the python is.")
      s  = input(">>> ")
      if s == "1":
        chosen = house1
        if h1 >= 1:
          time.sleep(1)
          print("House is now locked")
          chooseHouse()
        else:
          checkHouse()
      elif s == "2":
        chosen = house2
        if h2 >= 1:
            time.sleep(1)
            print("House is now locked")
            chooseHouse()
        else:
          checkHouse()
      elif s == "3":
        chosen = house3
        if h3 >= 1:
          time.sleep(1)
          print("House is now locked")
          chooseHouse()
        else:
          checkHouse()
      elif s == "4":
        chosen = house4
        if h4 >= 1:
          time.sleep(1)
          print("House is now locked")
          chooseHouse()
        else:
          checkHouse()

      elif s == "5":
        chosen = house5
        if h5 >= 1:
          time.sleep(1)
          print("House is now locked")
          chooseHouse()
        else:
          checkHouse()

      elif s == "t" or "track":
          print("Opening Trackers...")
          tracker = tracker - 1
          if tracker == 0:
              print("Your tracker ran out of batteries!")
              chooseHouse()
          else:
              if house1 == 2:
                print("House 1 is not safe")

              if house2 == 2:
                print("House 2 is not safe")
              if house3 == 2:
                print("House 3 is not safe")

              if house4 == 2:
                print("House 4 is not safe")

              if house5 == 2:
                print("House 5 is not safe")

              chooseHouse()

      else:

        startGame()


def searchHouse():
  global chosen, snakes, h1, h2, h3, h4, h5, house1, house2, house3, house4, house5
  bed = random.randint(1, 2)
  bottle = random.randint(1, 2)
  couch = random.randint(1, 2)
  chair = random.randint(1, 2)
  shelf = random.randint(1, 2)
  trash = random.randint(1, 2)
  if chosen == house1:
    h1 = h1 + 1
    print("Type a number to search items:")
    print("1. BED")
    print("2. BOTTLE")
    print("3. COUCH")
    print("4. CHAIR")
    print("5. SHELF")
    print("6. TRASH")
    print("7. LEAVE HOUSE")
    selection = input(">>> ")
    s = selection
    if s == "1":                                        
     print("Checking BED")
     if bed == 1:
        print("You found a snake!")

        searchHouse()
     else:
        print("No Snake Found..")
        snakes = snakes + 1
        searchHouse()

    elif s == "2":
      print("Checking BOTTLE")
      if bottle == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "3":
      print("Checking COUCH")
      if couch == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "4":
      print("Checking CHAIR")
      if chair == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "5":
      print("Checking SHELF")
      if shelf == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "6":
      print("Checking TRASH")
      if trash == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "7":
      print("Exiting House")
      house1 = random.randint(1, 2)
      house2 = random.randint(1, 2)
      house3 = random.randint(1, 2)
      house4 = random.randint(1, 2)
      house5 = random.randint(1, 2)
      chooseHouse()
  elif chosen == house2:
    h2 = h2 + 1
    print("Type a number to search items:")
    print("1. BED")
    print("2. BOTTLE")
    print("3. COUCH")
    print("4. CHAIR")
    print("5. SHELF")
    print("6. TRASH")
    print("7. LEAVE HOUSE")
    selection = input(">>> ")
    s = selection
    if s == "1":
      print("Checking BED")
      if bed == 1:
        print("You found a snake!")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "2":
      print("Checking BOTTLE")
      if bottle == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "3":
      print("Checking COUCH")
      if couch == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "4":
      print("Checking CHAIR")
      if chair == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "5":
      print("Checking SHELF")
      if shelf == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "6":
      print("Checking TRASH")
      if trash == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "7":
      print("Exiting House...")
      house1 = random.randint(1, 2)
      house2 = random.randint(1, 2)
      house3 = random.randint(1, 2)
      house4 = random.randint(1, 2)
      house5 = random.randint(1, 2)
      chooseHouse()

    else:
      chooseHouse()


  elif chosen == house3:
    h3 = h3 +1
    print("Type a number to search items:")
    print("1. BED")
    print("2. BOTTLE")
    print("3. COUCH")
    print("4. CHAIR")
    print("5. SHELF")
    print("6. TRASH")
    print("7. LEAVE HOUSE")
    selection = input(">>> ")
    s = selection
    if s == "1":
      print("Checking BED")
      if bed == 1:
        print("You found a snake!")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "2":
      print("Checking BOTTLE")
      if bottle == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "3":
      print("Checking COUCH")
      if couch == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "4":
      print("Checking CHAIR")
      if chair == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "5":
      print("Checking SHELF")
      if shelf == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "6":
      print("Checking TRASH")
      if trash == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "7":
        print("Exiting House...")
        house1 = random.randint(1, 2)
        house2 = random.randint(1, 2)
        house3 = random.randint(1, 2)
        house4 = random.randint(1, 2)
        house5 = random.randint(1, 2)
        chooseHouse()
    else:
        searchHouse()
  elif chosen == house4:
    h4 = h4 + 1
    print("Type a number to search items:")
    print("1. BED")
    print("2. BOTTLE")
    print("3. COUCH")
    print("4. CHAIR")
    print("5. SHELF")
    print("6. TRASH")
    print("7. LEAVE HOUSE")
    selection = input(">>> ")
    s = selection
    if s == "1":
      print("Checking BED")
      if bed == 1:
        print("You found a snake!")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "2":
      print("Checking BOTTLE")
      if bottle == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "3":
      print("Checking COUCH")
      if couch == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "4":
      print("Checking CHAIR")
      if chair == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "5":
      print("Checking SHELF")
      if shelf == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "6":
      print("Checking TRASH")
      if trash == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        snakes = snakes + 1
        searchHouse()
    elif s == "7":
      print("Exiting House...")
      house1 = random.randint(1, 2)
      house2 = random.randint(1, 2)
      house3 = random.randint(1, 2)
      house4 = random.randint(1, 2)
      house5 = random.randint(1, 2)
      chooseHouse()

    else:
      chooseHouse()

  elif chosen == house5:
    h5 = h5 + 1
    print("Type a number to search items:")
    print("1. BED")
    print("2. BOTTLE")
    print("3. COUCH")
    print("4. CHAIR")
    print("5. SHELF")
    print("6. TRASH")
    print("7. LEAVE HOUSE")
    selection = input(">>> ")
    s = selection
    if s == "1":
      print("Checking BED")
      if bed == 1:
        print("You found a snake!")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "2":
      print("Checking BOTTLE")
      if bottle == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "3":
      print("Checking COUCH")
      if couch == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "4":
      print("Checking CHAIR")
      if chair == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()

    elif s == "5":
      print("Checking SHELF")
      if shelf == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "6":
      print("Checking TRASH")
      if trash == 1:
        print("You found a snake")
        snakes = snakes + 1
        searchHouse()
      else:
        print("No Snake Found..")
        searchHouse()
    elif s == "7":
      print("Exiting House...")
      time.sleep(1)
      house1 = random.randint(1, 2)
      house2 = random.randint(1, 2)
      house3 = random.randint(1, 2)
      house4 = random.randint(1, 2)
      house5 = random.randint(1, 2)
      chooseHouse()
    else:
        chooseHouse()





def checkHouse():
  global chosen, house1, house2, house3, house4, house5
  if chosen == house1:
    print("Entering the door of the House...")
    time.sleep(2)
    print(""""
                             _..-:-.._
                      _..--''    :    ``--.._
               _..--''           :           ``--.._
         _..-''                  :                .'``--.._
  _..--'' `.                     :              .'         |
 |          `.              _.-''|``-._       .'           |
 |            `.       _.-''     |     ``-._.'       _.-.  |
 |   |`-._      `._.-''          |  ;._     |    _.-'   |  |
 |   |    `-._    |     _.-|     |  |  `-.  |   |    _.-'  |
 |_   `-._    |   |    |   |     |  `-._ |  |   |_.-'   _.-'   ..
   `-._   `-._|   |    |.  |  _.-'-._   `'  |       _.-'   ..::::::..
       `-._       |    |  _|-'  *    `-._   |   _.-'   ..::::::::''
           `-._   |   _|-'.::. \\|/  *    `-.|.-'   ..::::::::''
               `-.|.-' *`:::::::.. \\|/  *      ..::::::::''
                      \\|/  *`:::::::.. \\|/ ..::::::::''
                          \\|/  *`:::::::.::::::::''
                              \\|/  *`::::::::''
                                  \\|/  `:''""""")
    time.sleep(1)
    if house1 == 1:
      print("House is safe!")
      time.sleep(0.7)
      searchHouse()

    else:
      print("You: What was that sound?")
      time.sleep(1)
      print("You: What is that?")
      time.sleep(1)
      print(""""       ---_ ......._-_--.
      (|\\ /      / /| \\  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \\          _.-'    / .'*|
   \\______.-'//    .'.' \\*|
    \\|  \\ | //   .'.' _ |*|
     `   \\|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \\*|
      \\`-|\\_/ /    \\ _ _ \\*\\
       `/'\\__/      \\ _ _ \\*\\
      /^|            \\ _ _ \\*
     '  `             \\ _ _ \\      Python...
                       \\_


                                        """)
      time.sleep(2)
      print()
      print("You: AHHHHHH! -- Dead")
      print()
      loseGame()
  elif chosen == house2:
    print("Entering the door of the house...")
    time.sleep(2)
    print(''''     ) )        /\
   =====      /  \\
  _|___|_____/ __ \\____________
 |::::::::::/ |  | \\:::::::::::|
 |:::::::::/  ====  \\::::::::::|
 |::::::::/__________\\:::::::::|
 |_________|  ____  |__________|
  | ______ | / || \ | _______ |
  ||  |   || ====== ||   |   ||
  ||--+---|| |    | ||---+---||
  ||__|___|| |   o| ||___|___||
  |========| |____| |=========|
 (^^-^^^^^-|________|-^^^--^^^)
 (,, , ,, ,/________\\,,,, ,, ,)
','',,,,' /__________\\,,,',',;;
''')

    if house2 == 1:
      print("House is safe!")
      time.sleep(0.7)
      searchHouse()
    else:
      print("You: What was that sound?")
      time.sleep(1)
      print("You: What is that? It Smells...")
      time.sleep(1)
      print(""""       ---_ ......._-_--.
      (|\\ /      / /| \\  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \\          _.-'    / .'*|
   \\______.-'//    .'.' \\*|
    \\|  \\ | //   .'.' _ |*|
     `   \\|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \\*|
      \\`-|\\_/ /    \\ _ _ \\*\\
       `/'\\__/      \\ _ _ \\*\\
      /^|            \\ _ _ \\*
     '  `             \\ _ _ \\      Python...
                       \\_


                                        """)
      time.sleep(2)
      print("You: AHHHHHH! -- Dead")
      print()
      loseGame()
  elif chosen == house3:
    print("Entering the door of the house...")
    time.sleep(2)
    print(''''     ____
                 | =|
               +-"  "-+
               | ==  =|
             +-"  == ="-+
             |=    == = |
           +-" ==   =   "-+
         __| =  ______ ===|__
         | == = |####| ==  =|
       +-"  ==  |====|---. ="-+
       |=== =  =|    | X | == |
    +--" = =  = "----"---"=   "--+
    |==  ==== ==   ==  ===  == ==|
    |= == == _____________ =  == |
    | =  ==  |#####|#####|= ==  =|
    |= = .---|=====|=====|---.=  |
    |== =| X |     |     | X | ==|
    |  =="---"-----+-----"---" = |
    |____________________________|
    |____________________________|
    | ________   _____________   |
    |=|##||##|== |##|##|##|##|  =|
    |=|##||##| ==|##|##|##|##| ==|
    |=|==++==|= =|==+==+==+==|  =|
    |=|,-""-.| = | .^. | .^. | ==|
    |=||    || ==|/   \\|/   \\|  =|
    |=||    ||= _|)___(|)___(|_==|
    |=||o   || "---------------"=|
    |=||    ||==    ===    =   ==|
    |=||    ||  ==   ===   ==== =|
    |_||____||___________________|''''')
    if house3 == 1:
      print("House is safe!")
      time.sleep(0.7)
      searchHouse()
    else:
      print("You: What was that sound?")
      time.sleep(1)
      print("You: What is that? It stinks...")
      time.sleep(1)
      print(""""       ---_ ......._-_--.
      (|\\ /      / /| \\  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \\          _.-'    / .'*|
   \\______.-'//    .'.' \\*|
    \\|  \\ | //   .'.' _ |*|
     `   \\|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \\*|
      \\`-|\\_/ /    \\ _ _ \\*\\
       `/'\\__/      \\ _ _ \\*\\
      /^|            \\ _ _ \\*
     '  `             \\ _ _ \\      Python...
                       \\_


                                        """)
      time.sleep(2)
      print("You: AHHHHHH! -- Dead")
      print()
      loseGame()
  elif chosen == house4:
      print("Entering the door of the house...")
      time.sleep(2)
      print(''''


                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\\        ______    \\    /   /\/\  /\/\
          /  \    //_\\       \\    /\\    \\  /\/\/    \/    \
   /\    / /\/\  //___\\       \\__/  \\    \/
                //_____\\       \\ |[]|     \\
 /\/\/\/       //_______\\       \\|__|      \\
/      \      /XXXXXXXXXX\\                  \\
        \    /_I_II  I__I_\__________________\\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~''''')
      if house4 == 1:
        print("House is safe!")
        time.sleep(0.5)
        searchHouse()
      else:
        print("You: What was that sound?")
        time.sleep(1)
        print("You: What is that? BallSacks...")
        
        time.sleep(1)
        print(""""       ---_ ......._-_--.
      (|\\ /      / /| \\  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \\          _.-'    / .'*|
   \\______.-'//    .'.' \\*|
    \\|  \\ | //   .'.' _ |*|
     `   \\|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \\*|
      \\`-|\\_/ /    \\ _ _ \\*\\
       `/'\\__/      \\ _ _ \\*\\
      /^|            \\ _ _ \\*
     '  `             \\ _ _ \\      Python...
                       \\_


                                        """)
        time.sleep(2)
        print("You: AHHHHHH! -- Dead")
        print()
        loseGame()
  elif chosen == house5:
      print("Entering the door of the house...")
      time.sleep(2)
      print(""""                   ____
                  _           |---||            _
                  ||__________|KKK||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-';`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||;||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    );||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|;-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||;''||   ||:'
    ||||.;  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''-         ''-         ''-         '''  ''''""""")
      if house5 == 1:
        print("House is safe!")
        time.sleep(0.7)
        searchHouse()
      else:
        print("You: What was that sound?")
        time.sleep(1)
        print("You: What is that? A big slitherin' ball?")
        time.sleep(1)
        print(""""       ---_ ......._-_--.
      (|\\ /      / /| \\  \\
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \\          _.-'    / .'*|
   \\______.-'//    .'.' \\*|
    \\|  \\ | //   .'.' _ |*|
     `   \\|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \\*|
      \\`-|\\_/ /    \\ _ _ \\*\\
       `/'\\__/      \\ _ _ \\*\\
      /^|            \\ _ _ \\*
     '  `             \\ _ _ \\      Python...
                       \\_


                                        """)
        time.sleep(2)
        print("You: AHHHHHH! -- Dead")
        print()
        loseGame()
  chosen = 0




def startGame():
  global chosen
  print()
  print("You awake at Snake Wiggles Street...")
  time.sleep(1)
  print("You: Where am I?")
  time.sleep(1)
  print("Voice from somewhere: Find the snakes....")
  time.sleep(1)
  print("You: What...snakes?")
  time.sleep(2)
  print()
  print("Game Begins in: 3")
  time.sleep(1)
  print("Game Begins in: 2")
  time.sleep(1)
  print("Game Begins in: 1")
  time.sleep(1)
  print()
  chooseHouse()

def loadingGame():
  print()
  print("Bad dreams can be terrifying if you are awake in them...")
  time.sleep(1)
  print("     Nightmares are terrifying even when you are not awake in them...")
  time.sleep(2)
  print()
  startGame()

def introGame():
  print(''''       .ed"""" """$$$$be.
     -"           ^""**$$$e.  GAME IMPOSSIBLE
   ."                   '$$$c
  /                      "4$$b
 d  3                      $$$$
 $  *                   .$$$$$$
.$  ^c           $$$$$e$$$$$$$$.
d$L  4.         4$$$$$$$$$$$$$$b
$$$$b ^ceeeee.  4$$ECL.F*$$$$$$$
$$$$P d$$$$F $ $$$$$$$$$- $$$$$$
3$$$F "$$$$b   $"$$$$$$$  $$$$*"
 $$P"  "$$b   .$ $$$$$...e$$         PYTHON'S NIGHTMARE
  *c    ..    $$ 3$$$$$$$$$$eF
    %ce""    $$$  $$$$$$$$$$*
     *$e.    *** d$$$$$"L$$
      $$$      4J$$$$$% $$$
     $"'$=e....$*$$**$cz$$"
     $  *=%4.$ L L$ P3$$$F
     $   "%*ebJLzb$e$$$$$b   By BallSack Studios (c)
      %..      4$$$$$$$$$$
       $$$e   z$$$$$$$$$$
        "*$c  "$$$$$$$P"
          """*$$$$$$$"''''')

  print()
  time.sleep(1)
  s = input("Type something to continue: ")
  if s == "s":
    chooseHouse()
  else:
    ""
    print()
    print("Instructions: ")
    print()
    print("You are on Snake Wiggles Street. You need to collect 10 snakes from the houses. When you get 10 snakes, you win the game.")
    print(" But, you must know that a virus named Python is hunting you. You will have to find the snakes without getting caught by the Python! ")
    print("A tracker will help you guide your path in the game. It will tell which house has the Python in them, however, the tracker works when it wants to work!")
    print("Good Luck")
    print()
    print("Note: When you collect all 10 snakes, leave the house in which you are in to win the game!")
    print()
    time.sleep(1)
    input("Type to play the game: ")
    loadingGame()


# RUN COMMANDS: 
print("V.1.2")
print()
time.sleep(1)
introGame()































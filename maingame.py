# from sys import exit

# import time used to delay when some lines are displayed
import time
# import string used to strip out punctuation
import string

# START GLOBALS

# makes golem room unrepeatable
global golem_already_entered
golem_already_entered = False

# allows the player to unlock the skull door
global skull_key
skull_key = False

# used to track the staring contest
global eye_stare
eye_stare = 0

# used to track insanity from performing non-stare related actions in the eye room
global eye_insanity
eye_insanity = 0

# used to make the pre-search section of the skull room unrepeatable
global skull_door
skull_door = False

# applies protection from the stair ghosts
global glitter_glow
glitter_glow = False

# makes fairy encounter unrepeatable
global fairy
fairy = True

# moves mimic away from the gold door in the mimic room, makes encounter unrepeatable
global mimic_moved
mimic_moved = False

# makes it so the player doesn't need to unlock the skull door every time the room is entered
global skull_lock
skull_lock = False

# dark sign message
global default_death
default_death = "..........\n..........\nYour dark sign flares to life as you are prevented from reaching eternal rest.\n.........."

# END GLOBALS

# START INVENTORY
inventory = ["Dark Sign"]


# currently implemented inventory items: ""Dark Sign", "Skull Key"
# END INVENTORY

# stairs from the start to the great kiln.  requires glitter_glow from fairy's room to traverse.
def ghost_stairs():
    print "Stairs wind down as far as you can see."
    print "Suddenly, everything is illuminated by an ethereal light."

    if glitter_glow == False:
        print "You are swarmed by vengeful ghosts"
        print "They tear you limb from limb."
        dead(default_death)
    elif glitter_glow == True:
        print "Ghosts rush towards you, but are repeled by"
        print "* ~ ~ ~ fairy's Blessing ~ ~ ~*"
        great_kiln()


# final room, ends game
def great_kiln():
    print "You've entered the Kiln of the First Flame."
    print "Will you delay the age of Dark and link the bonfires?"

    punc = raw_input("> ").lower()
    fire_link = punc.translate(string.maketrans("", ""), string.punctuation)
    next = fire_link.split()

    if "yes" in next:
        print "In linking the fires you've condemned yourself to burn eternally..."
        print "but at least the Dark has been prevented."
        exit(0)

    elif "no" in next:
        print "Ascending to become the Dark Lord, you usher in the Age of Dark!"
        print "Good for you I guess?"
        exit(0)

    else:
        print "I don't understand"
        great_kiln()


# mimic room before the mimic is moved
def mimic_room():
    global mimic_moved

    if mimic_moved == True:
        mimic_room_moved()
    elif mimic_moved == False:
        print "There is a treasure chest."
        print "It undoubtedly contains treasure."
        print "The chest is blocking a golden door."
        print "(b)ack"

        punc = raw_input("> ").lower()
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.lower()

        if "mimic" in next and not mimic_moved == True:
            print "The mimic has moved from the door.  You can go through it now."
            mimic_moved = True
            mimic_room_moved()
            return mimic_moved
        elif "i" in next:
            print inventory
            mimic_room()
        elif "inventory" in next:
            print inventory
            mimic_room()
        elif "back" in next:
            start()
        elif "b" in next:
            start()
        elif "treasure" in next:
            print "Upon touching the treasure chest, you discover that it's a mimic."
            print "Before you have a chance to react it devours you whole."
            dead(default_death)
        elif "chest" in next:
            print "Upon touching the treasure chest, you discover that it's a mimic."
            print "Before you have a chance to react it devours you whole."
            dead(default_death)
        elif "door" in next:
            print "Upon touching the treasure chest, you discover that it's a mimic."
            print "Before you have a chance to react it devours you whole."
            dead(default_death)
        else:
            print "I don't understand."
            mimic_room()
    else:
        print "I don't understand."
        mimic_room()


# mimic room after the mimic is moved. allows passage to bone room
def mimic_room_moved():
    print "There is a golden door on the eastern wall"
    print "and mimic hanging out by the wall."
    print "(b)ack, (g)old door"

    punc = raw_input("> ").lower()
    input = punc.translate(string.maketrans("", ""), string.punctuation)
    next = input.split()

    if "i" in next:
        print inventory
        mimic_room_moved()
    elif "inventory" in next:
        print inventory
        mimic_room_moved()
    elif "back" in next:
        start()
    elif "b" in next:
        start()
    elif "door" in next and mimic_moved:
        skull_room()
    elif "d" in next and mimic_moved:
        skull_room()
    elif "gold" in next and mimic_moved:
        skull_room()
    elif "golden" in next and mimic_moved:
        skull_room()
    elif "g" in next and mimic_moved:
        skull_room()
    elif "door" in next and mimic_moved:
        skull_room()
    else:
        print "I don't understand."
        mimic_room_moved()


# initial state of the bone room, needs to be searched
def skull_room():
    # noinspection PyGlobalUndefined
    global skull_lock
    global skull_door
    print "This room has thousands of skulls stacked on dusty shelves and piled on the floor."

    if skull_door == False:
        print "You think you see something shiny out of the corner of your eye."
        print "(b)ack"

        punc = raw_input("> ")
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.lower()

        if "i" in next:
            print inventory
            skull_room()
        elif "inventory" in next:
            print inventory
            skull_room()
        elif "b" in next:
            mimic_room()
        elif "back" in next:
            mimic_room()
        elif "search" in next and skull_door == False:
            print "After some searching you find a lock embedded within a skull."
            skull_door = True
            skull_lock()
        else:
            print "I don't understand."
            skull_room()
    elif skull_door == True and skull_lock == True:
        skull_door_unlocked()
    elif skull_door == True and not skull_lock == True:
        skull_lock()
    else:
        print "program error"
        mimic_room()


# after searching the skull room, this is the provided state.  can unlock the door if skull_key == True
# noinspection PyGlobalUndefined
def skull_lock():
    global skull_lock

    print "You see a lock recessed in an ivory skull."
    print "(b)ack"

    punc = raw_input("> ")
    input = punc.translate(string.maketrans("", ""), string.punctuation)
    next = input.lower()

    if "i" in next:
        print inventory
        skull_lock()
    elif "inventory" in next:
        print inventory
        skull_lock()
    elif "b" in next:
        mimic_room()
    elif "back" in next:
        mimic_room()
    elif "unlock" in next and skull_key == True:
        print "You insert the skull shaped key into the skull lock."
        print "As soon as you turn the key the room begins to shake."
        print "Skulls clatter to the ground revealing a large double door set within a polished bone frame."
        skull_lock = True
        skull_door_unlocked()
    elif "key" in next and skull_key == True:
        print "You insert the skull shaped key into the skull lock."
        print "As soon as you turn the key the room begins to shake."
        print "Skulls clatter to the ground revealing a large double door set within a polished bone frame."
        skull_lock = True
        skull_door_unlocked()
    elif "unlock" in next and skull_key == False:
        print "You need the right key for this lock."
        skull_room()
    elif skull_key == True and next != "unlock":
        print "Do something with the key?"
        skull_lock()
    elif skull_key == False and next != "unlock":
        print "I don't understand."
        skull_lock()
    else:
        "How did you get this error at the skull_lock?"
        skull_room()


# changes the state so the bone door can be used.  allows access to glitter room
def skull_door_unlocked():
    print "There's a bone door amid a pile of skulls."
    print "(b)ack, bone (d)oor"

    punc = raw_input("> ").lower()
    input = punc.translate(string.maketrans("", ""), string.punctuation)
    next = input.split()

    if "door" in next:
        print "Bones crunch under your feet as you enter the bone door."
        glitter_room()
    elif "d" in next:
        print "Bones crunch under your feet as you enter the bone door."
        glitter_room()
    if "i" in next:
        print inventory
        skull_room()
    elif "inventory" in next:
        print inventory
        skull_room()
    elif "back" in next:
        mimic_room()
    elif "b" in next:
        mimic_room()
    else:
        print "I don't understand."
        skull_room()


# initial state of the glitter room.  allows player to get the glitter_glow buff. unrepeatable.
def glitter_room():
    print "You enter a room filled with glowing pink crystals."
    print "Sliver and gold glitter rains continuously from the ceiling."
    global glitter_glow
    global fairy

    if fairy == True:
        print "A glowing fairy floats over head."
        print "As you turn to look at her, she sings out:"
        print "What is movement for the sake of joy?"

        punc = raw_input("> ")
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.upper()
        uppercaseList = [next[0:4]]

        if "I" in uppercaseList:
            print inventory
            glitter_room()
        elif "DANC" in uppercaseList:
            print "The fairy shoots pink glitter from every pore"
            print "She sings, 'You\'re shielded by my protective love.  Good luck!'"
            print "Your vision is clouded with sparkling magic you cannot comprehend."
            glitter_glow = True
            print "******"
            time.sleep(1)
            print "******"
            fairy = False
            start()
        elif uppercaseList != "DANC":
            print "fairy sighs and quietly sings, '...so often disappointed'"
            print "She swoops down and splits your head open with her eye lasers."
            dead(default_death)
    elif fairy == False:
        print "The room is empty"
        print "(b)ack"

        punc = raw_input("> ")
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.lower()

        if "b" in next:
            print "You head back."
            skull_room()
        elif "back" in next:
            print "You head back."
            skull_room()
        else:
            print "I don't understand."
            glitter_room()

    else:
        print "How did you get this error in the fairy's glorious presence?"
        glitter_room()


# has an insanity counter. passes to stare_down.
def eye_room():
    if skull_key == False:
        print "Upon entering the room you see a giant, pulsating eye."
        print "As it turns its gaze upon you, your mind starts to unravel."
        print "(b)ack, (i)nventory?"

        punc = raw_input("> ").lower()
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.split()

        global eye_insanity

        if "i" in next:
            print inventory
            eye_insanity - + 1
            eye_room()
        if "inventory" in next:
            print inventory
            eye_insanity - + 1
            eye_room()
        if "item" in next:
            print inventory
            eye_insanity - + 1
            eye_room()
        elif "flee" in next:
            start()
        elif "back" in next:
            start()
        elif "b" in next:
            start()
        elif "stare" in next:
            stare_down()
        elif eye_insanity >= 3:
            print "The eye's intense gaze completely destabilizes your mind, disabling all body functions."
            print "After what seems like an eternity you suffocate to death."
            dead(default_death)
        else:
            eye_insanity += 1
            eye_room()
    elif skull_key == True:
        print "This room is a dead end, so you head back."
        start()
    else:
        print "How did you get this error entering the eye room?"
        start()


# has insanity counter and a stare counter.  can set skull_key == True and appends it to the player's inventory
def stare_down():
    global eye_stare
    print "You stare back defiantly, refusing to bend your gaze."
    if eye_stare <= 0:
        print "You feel yourself slipping into nothingness..."
        print " "
        time.sleep(3)
        print "Stare or flee?"

        punc = raw_input("> ").lower()
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.split()

        if "stare" in next:
            eye_stare += 1
            stare_down()
        elif "staring" in next:
            eye_stare += 1
            stare_down()
        elif "flee" in next:
            print "You flee back the way you came."
            start()
        elif "b" in next:
            print "You head back the way you came."
        elif "back" in next:
            "You head back the way you came."
            start()
        else:
            "Stare or flee?"
            stare_down()
    elif eye_stare <= 1:
        print "Something twists in your mind..."
        print " "
        time.sleep(3)
        print "Stare or flee?"

        punc = raw_input("> ").lower()
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.split()

        if "stare" in next:
            eye_stare += 1
            stare_down()
        elif "staring" in next:
            eye_stare += 1
            stare_down()
        elif "flee" in next:
            print "You flee back the way you came."
            start()
        elif "b" in next:
            print "You head back the way you came."
        elif "back" in next:
            "You head back the way you came."
            start()
        else:
            "Stare or flee?"
            stare_down()
    elif eye_stare >= 2:
        print "The eye begins spinning rapidly."
        print "eventually the eye spins so fast that it flies from its harness and vanishes into the sky."
        time.sleep(1)
        print "You find a skull shaped key!"
        print "This room is a dead end, so you head back."
        global skull_key
        inventory.append("Skull Key")
        skull_key = True
        start()
    else:
        print "How did you get this error in the eye room at the stare down?"
        start()


# handles player death
def dead(default_death):
    time.sleep(3)
    print default_death
    start()


# causes death on re-entry after riddle completed. passes to riddle
def golem_room():
    print "In this dimly lit room there is a large lake."
    print "A hideous creature approaches you from behind."
    global golem_already_entered
    if golem_already_entered == False:
        print "It screeches at you, 'IT ANSWERS THE RIDDLE OR WE EATS IT!"
        print "What do you do?"

        punc = raw_input("> ").lower()
        input = punc.translate(string.maketrans("", ""), string.punctuation)
        next = input.split()

        if "riddle" in next:
            riddle()
        else:
            print "It chases you down and eats you. You're still alive at the beginning."
            dead(default_death)
    else:
        print "The creature screams, 'WE EATS IT ANYWAY!'"
        print "It chases you down and eats you. You're still alive at the beginning."
        dead(default_death)


# if the riddle is answers gives the password to the mimic room
def riddle():
    print "What has roots as nobody sees..."
    print "...Is taller than trees..."
    print "...Up, up it goes..."
    print "...And yet never grows?"

    punc = raw_input("> ").lower()
    input = punc.translate(string.maketrans("", ""), string.punctuation)
    lowered_riddle_answer = input.split()

    if "mountain" in lowered_riddle_answer:
        print "."
        time.sleep(1)
        print".."
        time.sleep(1)
        print "..."
        time.sleep(2)
        print "The creature sighs and says, '...correct.  We tells it a secret:"
        print "the treasure's password is MIMIC'"
        print "You quickly return the way you came."
        global golem_already_entered
        golem_already_entered = True
        start()

    else:
        print "It screeches, 'Wrong!  NOW WE EATS IT!'"
        print "It chases you down and eats you. You're still alive at the beginning."
        dead(default_death)


# starting area.  links eye, mimic, and golem rooms.  allows access to ghost stairs.  player returns here on death.
def start():
    print "You are in a dark room."
    print "There is are doors to your right, left, and forward, as well as stairs leading down."
    print "(l)eft, (f)orward, (r)ight, (s)tairs, (i)nventory?"

    punc = raw_input("> ").lower()
    input = punc.translate(string.maketrans("", ""), string.punctuation)
    next = input.split()

    if "i" in next:
        print inventory
        start()
    elif "inventory" in next:
        print inventory
        start()
    elif "items" in next:
        print inventory
        start()
    elif "left" in next:
        mimic_room()
    elif "l" in next:
        mimic_room()
    elif "right" in next:
        eye_room()
    elif "r" in next:
        eye_room()
    elif "forward" in next:
        golem_room()
    elif "f" in next:
        golem_room()
    elif "down" in next:
        ghost_stairs()
    elif "s" in next:
        ghost_stairs()
    elif "stairs" in next:
        ghost_stairs()
    elif "climb" in next:
        ghost_stairs()
    else:
        print "I don't understand."
        start()


start()

# import time used to delay when some lines are displayed
import time

inventory = [
    "Dark Sign"]  # currently implemented inventory items: "Dark Sign", "Skull Key", "Fairy Amulet", "Dance Scroll"
status = []  # used to adjust states where adding an item to the inventory doesn't make sense


# stairs from the start to the great kiln.  requires glitter_glow from fairy's room to traverse.
def ghost_stairs():
    print("Stairs wind down as far as you can see.")
    print("Suddenly, everything is illuminated by an ethereal light.")

    if "Fairy Amulet" in inventory:
        print("Ghosts rush towards you, but are repelled by")
        print("* ~ ~ ~ fairy's Blessing ~ ~ ~*")
        great_kiln()

    else:
        print("You are swarmed by vengeful ghosts")
        print("They tear you limb from limb.")
        dead()


# final room, ends game
def great_kiln():
    print("You've entered the Kiln of the First Flame.")
    print("Will you delay the age of Dark and link the bonfires?")

    playerInput = input("> ").lower()

    if "y" in playerInput[0]:
        print("In linking the fires you've condemned yourself to burn eternally...")
        print("but at least the Age of Dark has been prevented.")
        exit(0)

    elif "no" in playerInput[0]:
        print("Ascending to become the Dark Lord, you usher in the Age of Dark!")
        print("Good for you I guess?")
        exit(0)

    else:
        print("I don't understand")
        great_kiln()


# mimic room before the mimic is moved
def mimic_room():
    if "mimic_moved" in status:
        mimic_room_moved()
    elif "mimic_moved" not in status:
        print("There is a treasure chest.")
        print("It undoubtedly contains treasure.")
        print("The chest is blocking a golden door.")
        print("(b)ack")

        playerInput = input("> ").lower()

        if "mimic" in playerInput and "mimic_moved" not in status:
            print("The mimic has moved from the door.  You can go through it now.")
            status.append("mimic_moved")
            mimic_room_moved()
        elif "i" in playerInput[0]:
            print(inventory)
            mimic_room()
        elif "b" in playerInput[0]:
            start()
        elif "treasure" in playerInput:
            print("Upon touching the treasure chest, you discover that it's a mimic.")
            print("Before you have a chance to react it devours you whole.")
            dead()
        elif "chest" in playerInput:
            print("Upon touching the treasure chest, you discover that it's a mimic.")
            print("Before you have a chance to react it devours you whole.")
            dead()
        elif "door" in playerInput:
            print("Upon touching the treasure chest, you discover that it's a mimic.")
            print("Before you have a chance to react it devours you whole.")
            dead()
        else:
            print("I don't understand.")
            mimic_room()
    else:
        print("I don't understand.")
        mimic_room()


# mimic room after the mimic is moved. allows passage to bone room
def mimic_room_moved():
    print("There is a golden door on the eastern wall")
    print("and mimic hanging out by the wall.")
    print("(b)ack, (g)old door")

    playerInput = input("> ").lower()

    if "i" in playerInput[0]:
        print(inventory)
        mimic_room_moved()
    elif "b" in playerInput[0]:
        start()
    elif "d" in playerInput[0] or "g" in playerInput[0] and "Skull Key" in inventory:
        skull_room()
    elif "d" in playerInput[0] or "g" in playerInput[0] and "Skull Key" not in inventory:
        print("This door requires a key\n")
        mimic_room_moved()
    else:
        print("I don't understand.")
        mimic_room_moved()


# changes the state so the bone door can be used.  allows access to glitter room
def skull_door_unlocked():
    print("There's a bone door amid a pile of skulls.")
    print("(b)ack, bone (d)oor")

    playerInput = input("> ").lower()

    if "d" in playerInput[0]:
        print("Bones crunch under your feet as you enter the bone door.")
        glitter_room()
    elif "i" in playerInput[0]:
        print(inventory)
        skull_door_unlocked()
    elif "b" in playerInput[0]:
        mimic_room()
    else:
        print("I don't understand.")
        skull_room()


# initial state of the bone room, needs to be searched
def skull_room():
    print("This room has thousands of skulls stacked on dusty shelves and piled on the floor.")
    if "Dance Scroll" not in inventory:
        print("You think you see something shiny out of the corner of your eye.")
        print("(b)ack, (i)nventory")

        playerInput = input("> ").lower()

        if "i" in playerInput[0]:
            print(inventory)
            skull_room()
        elif "b" in playerInput[0]:
            mimic_room()
        elif "search" in playerInput and "Dance Scroll" not in inventory:
            print("After some searching you find a lock embedded within a skull.")
            print("You find a scroll with a picture of Titania, Queen of the Fairies, and 'DANCE PARTY' written on it.")
            inventory.append("Dance Scroll")
            skull_lock()
        else:
            print("I don't understand.")
            skull_room()
    elif "Dance Scroll" in inventory and "Skull Key" not in inventory:
        skull_lock()
    else:
        print("program error is skull_room")
        mimic_room()


# after searching the skull room, this is the provided state.  can unlock the door if "Skull Key" is in inventory
def skull_lock():
    print("You see a lock recessed in an ivory skull.")
    print("(b)ack, (i)nventory")
    playerInput = input("> ").lower()

    if "i" in playerInput[0]:
        print(inventory)
        skull_lock()
    elif "b" in playerInput[0]:
        mimic_room()
    elif "unlock" in playerInput or "key" in playerInput and "Skull Key" in inventory:
        print("You insert the skull shaped key into the skull lock.")
        print("As soon as you turn the key the room begins to shake.")
        print("Skulls clatter to the ground revealing a large double door set within a polished bone frame.")
        skull_door_unlocked()
    elif "unlock" in playerInput or "key" in playerInput and "Skull Key" not in inventory:
        print("You need the right key for this lock.")
        skull_lock()
    elif "Skull Key" in inventory and playerInput is not "unlock":
        print("Do something with the key?")
        skull_lock()
    else:
        print("How did you get this error at the skull_lock?")
        skull_room()


# initial state of the glitter room.  allows player to get the glitter_glow amulet. unrepeatable.
def glitter_room():
    print("You enter a room filled with glowing pink crystals.")
    print("Sliver and gold glitter rains continuously from the ceiling.")

    if "Fairy Amulet" not in inventory:
        print("A glowing fairy floats over head.")
        print("As you turn to look at her, she sings out:")
        print("What is movement for the sake of joy?")

        playerInput = input("> ").lower()
        # uppercaseList = [playerInput[0:4]]

        if "i" in playerInput:
            print(inventory)
            glitter_room()
        elif "dance" in playerInput:
            print("The fairy shoots pink glitter from every pore")
            print("She sings, 'You\'re shielded by my protective love.  Good luck!'")
            print("You receive a magical amulet!")
            print("Your vision is clouded with sparkling magic you cannot comprehend.")
            inventory.append("Fairy Amulet")
            print("******")
            time.sleep(1)
            print("******")
            start()
        elif "dance" not in playerInput:
            print("fairy sighs and quietly sings, '...so often disappointed'")
            print("She swoops down and splits your head open with her eye lasers.")
            dead()
    elif "Fairy Amulet" in inventory:
        print("The room is empty")
        print("(b)ack")

        playerInput = input("> ").lower()

        if "b" in playerInput[0]:
            print("You head back.")
            skull_room()
        else:
            print("I don't understand.")
            glitter_room()

    else:
        print("How did you get this error in the fairy's glorious presence?")
        glitter_room()


# has an insanity counter. passes to stare_down.
def eye_room():
    if "eye_stare" in status:
        status.remove("eye_stare")
        eye_room()
    elif "Skull Key" not in inventory:
        print("Upon entering the room you see a giant, pulsating eye.")
        print("As it turns its gaze upon you, your mind starts to unravel.")
        print("(b)ack, (i)nventory?")

        playerInput = input("> ").lower()

        if "i" in playerInput[0]:
            print(inventory)
            if "eye_insanity" not in status:
                status.append("eye_insanity")
                eye_room()
            elif "eye_insanity_2" not in status and "eye_insanity" in status:
                status.append("eye_insanity_2")
                eye_room()
            elif "eye_insanity_2" in status:
                print("The eye's intense gaze completely destabilizes your mind, disabling all body functions.")
                print("After what seems like an eternity you suffocate to death.")
                status.remove("eye_insanity")
                status.remove("eye_insanity_2")
                dead()
            else:
                print("How did you get this error in the eye_room?")
                eye_room()
        elif "f" in playerInput[0]:
            start()
        elif "b" in playerInput[0]:
            start()
        elif "stare" in playerInput:
            status.append("eye_stare")
            stare_down()
        elif "eye_insanity_2" in status:
            print("The eye's intense gaze completely destabilizes your mind, disabling all body functions.")
            print("After what seems like an eternity you suffocate to death.")
            status.remove("eye_insanity")
            status.remove("eye_insanity_2")
            dead()
        else:
            if "eye_insanity" not in status:
                status.append("eye_insanity")
                eye_room()
            elif "eye_insanity_2" not in status and "eye_insanity" in status:
                status.append("eye_insanity_2")
                eye_room()
    elif "Skull Key" in inventory:
        print("This room is a dead end, so you head back.")
        start()
    else:
        print("How did you get this error entering the eye room?")
        start()


def stare_down():
    print(status)
    print("You stare back defiantly, refusing to bend your gaze.")
    if "eye_stare_3" in status:
        print("The eye begins spinning rapidly.")
        print("eventually the eye spins so fast that it flies from its harness and vanishes into the sky.")
        time.sleep(1)
        print("You find a skull shaped key!")
        print("This room is a dead end, so you head back.")
        inventory.append("Skull Key")
        start()
    elif "eye_stare_3" not in status and "eye_stare_2" in status:
        print("Something twists in your mind...")
        print(" ")
        time.sleep(3)
        print("Stare or flee?")

        playerInput = input("> ").lower()
        if "stare" in playerInput:
            status.append("eye_stare_3")
            stare_down()
        elif "f" in playerInput[0] or "b" in playerInput[0]:
            print("You flee back the way you came.")
            start()
        else:
            print("Stare or flee?")
            if "eye_insanity_2" not in status:
                status.append("eye_insanity_2")
                stare_down()
            elif "eye_insanity" not in status:
                status.append("eye_insanity")
                stare_down()
            elif "eye_insanity_2" in status:
                print("The eye's intense gaze completely destabilizes your mind, disabling all body functions.")
                print("After what seems like an eternity you suffocate to death.")
                status.remove("eye_insanity")
                status.remove("eye_insanity_2")
                dead()
            stare_down()
    elif "eye_stare_2" not in status:
        print("You feel yourself slipping into nothingness...")
        print(" ")
        time.sleep(3)
        print("Stare or flee?")

        playerInput = input("> ").lower()

        if "stare" in playerInput:
            status.append("eye_stare_2")
            stare_down()
        elif "i" in playerInput[0]:
            print(inventory)
            stare_down()
        elif "f" in playerInput[0] or "b" in playerInput[0]:
            print("You head back the way you came.")
            start()
        else:
            print("Stare or flee?")
            if "eye_insanity_2" not in status:
                status.append("eye_insanity_2")
            elif "eye_insanity" not in status:
                status.append("eye_insanity")
            elif "eye_insanity_2" in status:
                print("The eye's intense gaze completely destabilizes your mind, disabling all body functions.")
                print("After what seems like an eternity you suffocate to death.")
                status.remove("eye_insanity")
                status.remove("eye_insanity_2")
                dead()
            stare_down()


# handles player death
def dead():
    time.sleep(3)
    print(
        "..........\n..........\nYour dark sign flares to life as you are prevented from reaching eternal rest.\n..........")
    start()


# causes death on re-entry after riddle completed. passes to riddle
def golem_room():
    print("In this dimly lit room there is a large lake.")
    print("A hideous creature approaches you from behind.")

    if "golem_already_entered" in status:
        print("It screeches at you, 'IT ANSWERS THE RIDDLE OR WE EATS IT!")
        print("What do you do?")

        playerInput = input("> ").lower()

        if "r" in playerInput[0]:
            riddle()
        else:
            print("It chases you down and eats you. You're still alive at the beginning.")
            dead()
    else:
        print("The creature screams, 'WE EATS IT ANYWAY!'")
        print("It chases you down and eats you. You're still alive at the beginning.")
        dead()


# if the riddle is answered gives the password to the mimic room
def riddle():
    print("What has roots as nobody sees...")
    print("...Is taller than trees...")
    print("...Up, up it goes...")
    print("...And yet never grows?")

    playerInput = input("> ").lower()

    if "mountain" in playerInput:
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(2)
        print("The creature sighs and says, '...correct.  We tells it a secret:")
        print("the treasure's password is MIMIC'")
        print("You quickly return the way you came.")
        status.append("golem_already_entered")
        start()

    else:
        print("It screeches, 'Wrong!  NOW WE EATS IT!'")
        print("It chases you down and eats you. You're still alive at the beginning.")
        dead()


# starting area.  links eye, mimic, and golem rooms.  allows access to ghost stairs.  player returns here on death.
def start():
    print("You are in a dark room.")
    print("There is are doors to your right, left, and forward, as well as stairs leading down.")
    print("(l)eft, (f)orward, (r)ight, (s)tairs, (i)nventory?")

    playerInput = input("> ").lower()

    if "i" in playerInput[0]:
        print(inventory)
        start()
    elif "l" in playerInput[0]:
        mimic_room()
    elif "r" in playerInput[0]:
        eye_room()
    elif "f" in playerInput[0]:
        golem_room()
    elif "d" in playerInput[0]:
        ghost_stairs()
    elif "s" in playerInput[0]:
        ghost_stairs()
    elif "cheat" in playerInput:
        inventory.append("Skull Key")
        start()
    else:
        print("I don't understand.")
        start()


start()

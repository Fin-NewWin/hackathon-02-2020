# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Flip(im, horizontal=True, vertical=False, **properties)
define t = Character("Turt", image="turt")


image black = im.Scale("Solidblack.png", 1280, 720)
image hi happy = im.Scale("hi happy.png", 300, 500)
image bg room = im.Scale("bg room.jpg", 1280, 720)
image turt = im.Scale("turt.png", 300, 400)
image Wall Paper Dark = im.Scale("Wall Paper Dark.jpg", 1280, 720)
image side turt normal = im.Scale("turt.png", 400, 300, yoffset=0, xoffset=5)
image side hi happy = "hi happy.png"
image hi sad = im.Scale("hi sad.png", 300, 500)


define sky = "SkyBottle.mp3"
define feelings = "Feelings.mp3"
define sadstuff = "SadShit.mp3"
define gymnopedia = "Gymnopedia.mp3"
define rain = "rain.mp3"
define panic = "panic.mp3"
define endost = "audio/pain.mp3"
define fire = "fire.mp3"
define h = Character("Yuki")


label start:
    scene black
    play music gymnopedia
    show hi sad:
        zoom 10

    h "Sigh, I have to move once again to a new area."

    h "Oh well, I heard we are close to the beach. I want to go visit it."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hi happy at left:

        # These display lines of dialogue.

    h "Oh wow it looks amazing!"

    h "Sigh, I wonder how we live in such a gorgeous place now."

    h "Maybe I should try exploring this place at night too!"

    scene Wall Paper Dark with fade

    stop music fadeout 1.0

    play music sadstuff
    show hi happy at left:

    h "Hm? What's that over there."

    h "Is that a turtle? Oh no, it looks so hurt!"

    menu:
        "Should I go to it?":
            "Of course I should save that poor guy"

        "Maybe I should leave it.":
            "Not my problem."
            stop music
            jump bad_ending

    show turt at right:
        xzoom - 1
    # with fade

    t normal"You dirty humans!"
    h "You can talk?!?"

    t "Of course I can can't you hear me speaking!"
    h "Uh, sorry this is just a surprise for me. You seem hurt, do you need help?"

    t "I do need help, but not from you humans. Look at the damage you caused me, just imagine the rest of us!"

    scene black with fade

    show hi happy at left:

    h "He's aggresive"

    menu:
        "Maybe I should leave.":
            "He's really mad and I think now isn't the time to bother him"
            jump alternate_path

        "No I have to help him":
            "He needs the treatment for sure! I need to do something about it."

    return
label alternate_path:
    scene Wall Paper Dark with fade

    show hi happy at left:

    show turt at right:

    h "You're right, I can't help you as of right now."

    t "That's right leave me alone."

    h "I'll come by tomorrow to ask again. So wait for me."

label bad_ending:
    stop music
    play audio fire
    play audio panic
    play music endost
    t "the end"
    stop audio
    stop music
    return

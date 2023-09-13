# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amongus")
define s = Character("Superman")
define narrator = Character("")

image space = "images/1328226.png"
image redamongus:
    "images/pngwing.com.png"
    zoom 0.2
image mexigus:
    "images/pngwing.com (1).png"
    zoom 0.3
image amonguns:
    "images/pngwing.com (2).png"
    zoom 0.07
image superman:
    "images/pngwing.com (3).png"
    zoom 0.3


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene space

    play music "audio/music.ogg"

    show superman at truecenter

    s "Its over amongus!"
    
    hide superman

    show redamongus at left

    show mexigus at center

    show amonguns at right

    e "you cant defeat us."

    hide redamongus
    hide mexigus
    hide amonguns

    call prepare_battle

    # This ends the game.

    return


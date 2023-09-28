# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amongus")
define s = Character("Java")
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
image atkamongus:
    "images/amg_atk.png"
    zoom 0.11
image dmgamongus:
    "images/amg_dmg.png"
    zoom 0.11
image java:
    "images/java 15.png"
    zoom 0.75
image java_battle:
    "images/java 1.png"
    zoom 0.65
image java_attack:
    "images/java 2.png"
    zoom 0.65
image java_dmg:
    "images/java 4.png"
    zoom 0.65


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene space

    play music "audio/music.ogg"

    show java at center

    s "Its over amongus!"
    
    hide java

    show redamongus at left

    show mexigus at center

    show amonguns at right

    e "you cant defeat us."

    hide redamongus
    hide mexigus
    hide amonguns

    call prepare_battle

    narrator "Fim de jogo" 

    # This ends the game.

    return


# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Amongus")
define s = Character("Java")
define narrator = Character("")

image space = "images/1328226.png"

image battle_menu_box = "images/screens/2.png"
image battle_change_menu_box = "images/screens/2_2.png"

image player_box = "images/screens/player_box.png"
image enemy_box = "images/screens/enemy_box.png"

image redamongus:
    "images/pngwing.com.png"
    zoom 0.23
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

image java = "images/java 15.png"    
image java_battle = "images/java 1.png"
image java_attack = "images/java 2.png"
image java_dmg = "images/java 4.png"

style battle_button_text:
    color '#000'
    idle_color '#000'
    hover_color '#20558a'

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

    show redamongus at left:
        yalign 0.5

    show mexigus at center:
        yalign 0.5

    show amonguns at right:
        yalign 0.5

    e "You cant defeat us."

    hide redamongus
    hide mexigus
    hide amonguns

    call prepare_battle

    narrator "Fim de jogo" 

    # This ends the game.

    return


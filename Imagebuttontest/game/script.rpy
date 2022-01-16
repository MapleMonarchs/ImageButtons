# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e        = Character("HurDurDings")

image scMain    = "RoomMain.png"

image Gardine   = "RoomGardine.png"

image hDesk     = "RoomDesk_hover.png"
image iDesk     = "RoomDesk_idle.png"
image hDoor     = "RoomDoor_hover.png"
image iDoor     = "RoomDoor_idle.png"
image hWardrobe = "RoomWardrobe_hover.png"
image iWardrobe = "RoomWardrobe_idle.png"
image hWindow   = "RoomWindow_hover.png"
image iWindow   = "RoomWindow_idle.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene scMain 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show iDesk

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

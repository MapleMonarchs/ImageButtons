# choo choo 🥺
#                                                 __   __
#                                                 /'   `\
#                                                Y.     .Y
#                                      _______    \`. .'/
#                       ,-------------'======="--""""-""""---.
#                 ___,=+'-------------------------------------|p
#              .-/___|_]_]  :"/:""""""""""""""""""""""""""""""|'
#           ,-'___________[];/_;_____________________T G V____|
#         ,".../_|____________________________________________|
#        (_>         ,-------.                      ,-------.  |
#         `-.______.'(_)`='(_)\_7___7___7___7__7_.'(_)`='(_)\_/

define e        = Character("Test")

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

screen room:

    imagebutton:
        idle "iWindow"
        hover "hWindow"

    imagebutton:
        idle "iDoor"
        hover "hDoor" 
        
    imagebutton:
        idle "iDesk"
        hover "hDesk"

    imagebutton:
        idle "iWardrobe"
        hover "hWardrobe"

screen door_notif:
    text "TÜR":
        at transform:
            align (0.5, 0.5) alpha 0.0
            linear 0.5 alpha 1.0
            pause 2
            linear 0.5 alpha 0.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene scMain 
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    call screen room

    show iDesk

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

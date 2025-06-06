import pygame as pg
from pygame import mixer
from bob import Bob
from bobby import Bobby
from button import Button

# set up pygame modules
pg.init()
clock = pg.time.Clock()
fps = 60
pg.font.init()

# set up variables for the display
height= 1300
width = 800
size = (height, width)
screen = pg.display.set_mode(size)

font = pg.font.Font('fonts/handwritten.ttf', 70)
pg.display.set_caption("tOCltPalcap")

#images
welcome= pg.image.load("images/bg1.jpg")
welcome_image = pg.transform.scale(welcome, (size))

bg = pg.image.load("images/bg.jpg")
bg_image = pg.transform.scale(bg, (size))


textbox = pg.image.load("images/textbox.png")
textbox_image = pg.transform.scale(textbox, (1500, 1050))
textboxRect = textbox_image.get_rect()
textboxRect.centerx = screen.get_rect().centerx
textboxRect.centery = height / 12 * 7.2

#sounds
talking_Sound = pg.mixer.Sound('sounds/text.wav')
bgm = pg.mixer.Sound('sounds/bgm.wav')
title = pg.mixer.Sound('sounds/title.wav')
play_bgm = False
play_title = False
bgm.set_volume(.4)

#message
#messages = ['here are your daily cat facts-----', '1.)Cats can jump 5 times their height', '2.) A house cat is genetically 95.6% tiger.', '3.) Cat whiskers are the same width as their body', '4.)Cats’ noses is unique, like human fingerprints.', '5.) Grimalkin is the name of a older, female cat', '6.)Cats have an extra organ lets them taste scents', 'i ran out of cat facts', 'please exit out', 'i beg of you', 'i really dont have any cat facts', 'rfbiuoaknjafadiuoaknjafadgifjdnkgifjdasgretqtdnka', 'rrqhiuoaknjafadgifaefasffjdnkowijgeaafa', 'uriwhkafeiuoakngwyijgdewjafadgifjdnkjdma0','horiajgeiuoakguoiwkejfnjafadgifjdnkkw0rrit','9uwrioiuoruiewjkbvm,waknjafadgifjdnkvetep9wkma']
#messages = ['What does a storm cloud wear under his raincoat?', 'Thunderwer' ,'What do kids play when they have nothing to do?' , 'Bored games.','What do you call an ant who fights crime?' , 'A vigilANTe!' , 'Why are snails slow?' , 'Because theyre carrying a house on their back' , 'Whats the smartest insect?' , ' A spelling bee!' , 'What is fast, loud and crunchy?' , 'A rocket chip.' , 'How does the ocean say hi?' , 'It waves!']
with open('text/encouraging_messages.txt', 'r') as file:
    messages = [line.strip() for line in file]

snip = font.render('', True, 'black')
counter = 0
speed = 3
active_message = 0
message = messages[active_message]
done = False

#objects
b = Bob(50, 90)
bb = Bobby(450, 350)

button1_enabled = True
new_press = True

intro_screen = True
game_screen = False
dialogue = False

talking = False

while intro_screen:
    screen.blit(welcome_image, (0, 0))
    clock.tick(fps)
    if not play_title:
        title.play(-1)
        play_title = True

            
    # --- event loop
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If user clicked close
            intro_screen = False
        if event.type == pg.MOUSEBUTTONDOWN:
            intro_screen = False
            game_screen = True
    pg.display.update()

while game_screen:
    screen.blit(bg_image, (0,0))
    screen.blit(b.image, b.rect)
    screen.blit(bb.image, bb.rect)
    clock.tick(fps)
    talking_Sound.stop()
    title.fadeout(1500)

    play_title = False
    talking = False

    if  not play_bgm:
        bgm.play(-1)
        play_bgm = True

    #interact--talk button

    if bb.rect.colliderect(b.rect):
        talk_bob = Button('Talk?', bb.x + 200 , bb.y + 100, 120, 60, True)
        if talk_bob.check_click():
            dialogue = True

    # --- event loop
    for event in pg.event.get():  # User did something
        if event.type == pg.QUIT:  # If user clicked close
            game_screen = False

    keys = pg.key.get_pressed()  # checking pressed keys
    if keys[pg.K_d]:
        bb.move_direction("right")
    if keys[pg.K_a]:
        bb.move_direction("left")
    if keys[pg.K_w]:
    
        bb.move_direction("up")
    if keys[pg.K_s]:
        bb.move_direction("down")

    pg.display.flip()

#dialogue!!!
    while dialogue == True:
        clock.tick(fps)
        screen.blit(textbox_image, textboxRect)
        exit_button = Button('X', textboxRect.centerx + 450, textboxRect.y + 200 , 50, 50, True)
        
        if not talking:
            talking_Sound.play(-1)
            talking = True
            

        # message speed + finished
        if counter < speed * len(message):
            counter += 1
        else:
            if not done:
                talking_Sound.stop()  # Stop typewriter sound once message is fully typed
                done = True
            


        # --- event loop
        for event in pg.event.get():  # User did something
            if event.type == pg.QUIT:  # If user clicked close
                dialogue = False
                
            if exit_button.check_click():
                dialogue = False


            #typewrite
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN or done and (active_message < len(messages) - 1):
                    active_message += 1
                    done = False
                    message = messages[active_message]
                    counter = 0
                    talking = False
        snip = font.render(message[0:counter // speed], True, 'orange')
        screen.blit(snip, (100, 490))

        pg.display.flip()
    pg.quit









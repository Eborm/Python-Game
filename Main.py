import Display
import GameGraphics
import pygame
from Variables import Screen_Starts as Screen

pygame.init()

# Load images for game window
Start_screen = GameGraphics.Draw_image(0, 0, 'Start_screen.png', 1)
Map = GameGraphics.Draw_image(0, 0, 'Map.png', 1)
Start_Button = GameGraphics.Button(610, 328, 'Button.png', 1)
Stop_Button = GameGraphics.Button(610, 613, 'Button.png', 1)
Stop_Button2 = GameGraphics.Button(960, 540, 'Button.png', 0.75) #Temporary Will make a button and menu screen
Temp_Menu_Box =  GameGraphics.Rectangle(960, 540, 620, 900, (0, 0, 0), 2)

#Test_Circle = GameGraphics.Cricle(100, 100, 50, (25, 25, 25), 25)
#Test_Box = GameGraphics.Rectangle(100, 100, 500, 100, (0, 255, 255), 2)
#Test_Text = GameGraphics.Text(100, 100, 'Test', (0, 255, 0), 140, None)
#State variables
run = True
while Screen.Game_Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = Screen.Game_Run
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                Screen.Game_Run = False
            if event.key == pygame.K_ESCAPE:
                if Screen.In_Game_Menu == True:
                    Screen.In_Game_Menu = False
                elif Screen.In_Game_Menu == False:
                    Screen.In_Game_Menu = True
                
    if not Screen.Game_Started:
        Start_screen.draw()
        # Use the draw method of the Button class to handle events
        if Start_Button.EventDetection():
            Screen.Game_Started = True
        if Stop_Button.EventDetection():
            Screen.Game_Run = False

    if Screen.Game_Started:
        Map.draw()
        if Screen.In_Game_Menu == True:
            Temp_Menu_Box.Draw(None)
            Stop_Button2.draw()
            if Stop_Button2.EventDetection():
                Screen.Game_Run = False
    Display.Update()

pygame.quit()
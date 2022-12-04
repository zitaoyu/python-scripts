import pyautogui
from PIL import  ImageGrab

# bottom obstacle coordnates:
obstacle_x = 940
obstacle_y = 660
# top object coordnates:
top_object_y = 386

purple_candy_color = (228, 93, 191)
cup_green_color = (1, 114, 73)

i = 0
while(True):
    while(True):
        # grab pixel
        color = ImageGrab.grab((obstacle_x, obstacle_y, obstacle_x + 1, obstacle_y + 1)).load()[0, 0]

        # jump if detect candy obstacle
        if color == purple_candy_color:
            pyautogui.press('space')
            obstacle_x += 1
            break
        
        r: int = color[0]
        b: int = color[1]
        g: int = color[2]
        # since holly has multiple colors, we have to check the range of the color, jump if detected
        if (230 < r < 240 and 60 < b < 70 and 80 < g < 90) or (0 < r < 12 and 110 < b < 122 and 65 < g < 77):
            pyautogui.press('space')
            obstacle_x += 1
            break

        # grab top pixel
        color_2 = ImageGrab.grab((obstacle_x, top_object_y, obstacle_x + 1, top_object_y + 1)).load()[0, 0]
        # jump if detect starbucks cup
        if color_2 == cup_green_color:
            pyautogui.press('space')
            obstacle_x += 1
# Sterling Spencer j656k347
# Program:: prj.py
# This program makes use of the pygame library to draw a simple tree fractal and allows the user
# to edit some of the variables that go into producing the tree fractal. Such variables include
# the angle of tree branches, the number of iterations, width of the lines that produce the branches
# and the angle of the tree. The user can also choose to auto cycle through the angles which animates
# the tree at different angles.
#
# Psuedo Code
#
# Algorithm MAIN
#   Runs loop that will call various functions to get data to print to the screen.
# Pre - None
# Post - Prints out screen data, quits program
#
#    set font to courier size 16
#    angle = 20, iterations = 8, changeLW = 0, reverse = 0
#    offOn = 0, mPosition = (0,0), orentation = -90
#    while TRUE:
#       ev = event that is searched for
#       if ev.type == pygame.QUIT:
#          break
#       sideMenuWidth = 250
#       fill main_surface sky blue
#       drawTree((mainSurfaceWidth-sideMenuWidth)/2,mainSurfaceHeight - 10, orientation, iterations, angle, changeLW)
#       iterations, angle, changeLW, orientation, reverse, offOn = sideMenu(sideMenuWidth, iterations, angle, changeLW, orientation, reverse, offOn, mPosition, ev)
#       line1 = text info on some variables
#       line2 = text info on line width
#       push line1 and line2 to main_surface
#       flip main_surface to display
#       delay program
#    quit pygame
# End MAIN
#
# Algorithm DRAWTREE
#   Generates sets of x,y coordinates and uses them to draw lines onto main_surface
# Pre - takes in x1, y1, orientation, iterations, angle, changeLW as variables
# Post - draws line on main_surface
#
#   if iterations:
#       x2 = x1 + int(math.cos(math.radians(orientation)) * iterations * 10.0)
#       y2 = y1 + int(math.sin(math.radians(orientation)) * iterations * 10.0)
#       if iterations < 3:
#           red = 34
#           green = 139
#           blue = 34
#       else:
#           red = 160
#           green = 82
#           blue = 45
#       lineWidth = iteration + changeLW
#       draw line on main_surface
#       call DRAWTREE(x2, y2, orientation - angle, iterations - 1, angle, changeLW)
#       call DRAWTREE(x2, y2, orientation + angle, iterations - 1, angle, changeLW)
# End DRAWTREE
#
# Algorithm SIDEMENU
#   Draws multiple rectangles that will act as buttons, handles the mouse
#   hovering over them, and being clicked. It also puts text over the
#   the rectangles to decribe the buttons
# Pre - takes in sideMenuWidth, iterations, angle, changeLW, orientation, reverse, offOn, mPosition, ev
# Post - returns iterations, angle, changeLW, orientation, reverse, offOn
#
#   bSpacing = 20
#   buttonSpacing = [0,0,0,0,0,0,0,0,0]
#   for x in range(9):
#       buttonSpacing[x] = bSpacing
#       bSpacing += 40
#   fills right side of main_surface gray
#   Next luster of lines fills in rectagnles spaced appart via buttonSpacing,
#   changes button apperance if mouse is over them or have been clicked.
#   If any of them are clicked, it increments or decrements the needed var
#   calls AUTOANGLE which will automatically change the angle if the button for it has been pressed
#   Next cluster of lines places text over rectangles
#   return iterations, angle, changeLW, orientation, reverse, offOn
# End SIDEMENU
#
# Algorithm AUTOANGLE
#   Cycles through the angle and bounce back and forth between 0 and 360
# Pre - take offOn, reverse, and angle as input
# Post - returns angle and reverse
#
#   if offOn == 1:
#       if angle > 359 and reverse == 0:
#           reverse = 1
#       elif angle < 1 and reverse == 1:
#           reverse = 0
#       if reverse == 0:
#           angle += 1
#       elif reverse == 1:
#           angle -= 1
#   return angle, reverse 
# End AUTOANGLE

import pygame, time, math
from pygame.locals import *

# Sets surface ratio
mainSurfaceWidth = 1200
mainSurfaceHeight = 675

pygame.init()    # Prepare the PyGame module for use
main_surface = pygame.display.set_mode((mainSurfaceWidth, mainSurfaceHeight))
pygame.display.set_caption("Fractal Tree") # Title the window
font = pygame.font.SysFont("Courier", 16) # set font

def drawTree(x1, y1, orientation, iterations, angle, changeLW):
    if iterations:

        # Creates second (x,y) point to draw line
        x2 = x1 + int(math.cos(math.radians(orientation)) * iterations * 10.0)
        y2 = y1 + int(math.sin(math.radians(orientation)) * iterations * 10.0)

        # Color is greenish if iterations < 3, and is brown otherwise. Makes tree look like it has green leaves
        if iterations < 3:
            red = 34
            green = 139
            blue = 34
        else:
            red = 160
            green = 82
            blue = 45

        # Sets line width based on changeLW
        lineWidth = iterations + changeLW
        pygame.draw.line(main_surface, (red,green,blue), (x1, y1), (x2, y2), lineWidth)

        # Calls drawTree twice to draw both branches for the next iterations 
        drawTree(x2, y2, orientation - angle, iterations - 1, angle, changeLW)
        drawTree(x2, y2, orientation + angle, iterations - 1, angle, changeLW)

def autoAngle(offOn, reverse, angle):
    # Cycles from 0 to 360 if offOn == 1
    if offOn == 1:
        if angle > 359 and reverse == 0:
            reverse = 1
        elif angle < 1 and reverse == 1:
            reverse = 0

        if reverse == 0:
            angle += 1
        elif reverse == 1:
            angle -= 1

    return angle, reverse

def sideMenu(sideMenuWidth, iterations, angle, changeLW, orientation, reverse, offOn, mPosition, ev):
    # Gives spacing for the rectangles that will be used as buttons
    bSpacing = 20
    buttonSpacing = [0,0,0,0,0,0,0,0,0]
    for x in range(9):
        buttonSpacing[x] = bSpacing
        bSpacing += 40
        
    # Gray rectangle for side menu
    main_surface.fill((190,190,190), (mainSurfaceWidth - sideMenuWidth, 0, sideMenuWidth, mainSurfaceHeight))

    # Creates rectangles that will be used as buttons and colors them according to how they are being used
    buttonAngleUp = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[0], sideMenuWidth - 20, 20))
    buttonAngleDown = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[1], sideMenuWidth - 20, 20))
    if iterations < 11:
        buttonItrUp = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[2], sideMenuWidth - 20, 20))
    else:
        buttonItrUp = main_surface.fill((255,99,71), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[2], sideMenuWidth - 20, 20))
    if iterations > 0:
        buttonItrDown = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[3], sideMenuWidth - 20, 20))
    else:
        buttonItrDown = main_surface.fill((255,99,71), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[3], sideMenuWidth - 20, 20))

    buttonLineWidthUp = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[4], sideMenuWidth - 20, 20))
    buttonLineWidthDown = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[5], sideMenuWidth - 20, 20))

    buttonOrUp = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[6], sideMenuWidth - 20, 20))
    buttonOrDown = main_surface.fill((255,255,255), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[7], sideMenuWidth - 20, 20))

    if offOn == 1:
        buttonOffOn = main_surface.fill((255,200,200), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[8], sideMenuWidth - 20, 20))
    else:
        buttonOffOn = main_surface.fill((200,255,200), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[8], sideMenuWidth - 20, 20))

    # Changes buttons' apperance if mouse is over them
    if pygame.Rect(buttonAngleUp).collidepoint(pygame.mouse.get_pos()):
        buttonAngleUp = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[0], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonAngleDown).collidepoint(pygame.mouse.get_pos()):
        buttonAngleDown = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[1], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonItrUp).collidepoint(pygame.mouse.get_pos()):
        if iterations < 11:
            buttonItrUp = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[2], sideMenuWidth - 20, 20))
        else:
            buttonItrUp = main_surface.fill((255,99,71), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[2], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonItrDown).collidepoint(pygame.mouse.get_pos()):
        if iterations > 0:
            buttonItrDown = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[3], sideMenuWidth - 20, 20))
        else:
            buttonItrDown = main_surface.fill((255,99,71), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[3], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonLineWidthUp).collidepoint(pygame.mouse.get_pos()):
        buttonLineWidthUp = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[4], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonLineWidthDown).collidepoint(pygame.mouse.get_pos()):
        buttonLineWidthDown = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[5], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonOrUp).collidepoint(pygame.mouse.get_pos()):
        buttonOrUp = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[6], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonOrDown).collidepoint(pygame.mouse.get_pos()):
        buttonOrDown = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[7], sideMenuWidth - 20, 20))
    elif pygame.Rect(buttonOffOn).collidepoint(pygame.mouse.get_pos()):
        buttonOffOn = main_surface.fill((230,230,230), (mainSurfaceWidth - sideMenuWidth + 10, buttonSpacing[8], sideMenuWidth - 20, 20))

    # Checks if event == mousebuttondown
    if ev.type == MOUSEBUTTONDOWN:
        mPosition = ev.dict["pos"]    # Get the coordinates.
    else:
        mPosition = 0,0

    # Increments variables based on button that is pressed
    if pygame.Rect(buttonAngleUp).collidepoint(mPosition):
        angle += 1
    elif pygame.Rect(buttonAngleDown).collidepoint(mPosition):
        angle -= 1
    elif pygame.Rect(buttonItrUp).collidepoint(mPosition) and iterations < 11:
        iterations += 1
    elif pygame.Rect(buttonItrDown).collidepoint(mPosition) and iterations > 0:
        iterations -= 1
    elif pygame.Rect(buttonLineWidthUp).collidepoint(mPosition):
        changeLW += 1
    elif pygame.Rect(buttonLineWidthDown).collidepoint(mPosition):
        changeLW -= 1
    elif pygame.Rect(buttonOrUp).collidepoint(mPosition):
        orientation -= 1
    elif pygame.Rect(buttonOrDown).collidepoint(mPosition):
        orientation += 1
    elif pygame.Rect(buttonOffOn).collidepoint(mPosition):
        if offOn == 0:
            offOn = 1
        else:
            offOn = 0

    angle, reverse = autoAngle(offOn, reverse, angle)

    # Draws text over each button rectangle to decribe what that button does
    buttonAU = font.render("Branch Angle +", False, (0,0,0))
    main_surface.blit(buttonAU, (buttonAngleUp))
    buttonAD = font.render("Branch Angle -", False, (0,0,0))
    main_surface.blit(buttonAD, (buttonAngleDown))
    buttonIU = font.render("Iterations +", False, (0,0,0))
    main_surface.blit(buttonIU, (buttonItrUp))
    buttonID = font.render("Iterations -", False, (0,0,0))
    main_surface.blit(buttonID, (buttonItrDown))
    buttonLWU = font.render("Line Width +", False, (0,0,0))
    main_surface.blit(buttonLWU, (buttonLineWidthUp))
    buttonLWD = font.render("Line Width -", False, (0,0,0))
    main_surface.blit(buttonLWD, (buttonLineWidthDown))
    buttonOU = font.render("Tree Orientation +", False, (0,0,0))
    main_surface.blit(buttonOU, (buttonOrUp))
    buttonOD = font.render("Tree Orientation -", False, (0,0,0))
    main_surface.blit(buttonOD, (buttonOrDown))
    if offOn == 0:
        buttonFN = font.render("Auto Cycle Angles: OFF", False, (0,0,0))
        main_surface.blit(buttonFN, (buttonOffOn))
    else:
        buttonFN = font.render("Auto Cycle Angles: ON", False, (0,0,0))
        main_surface.blit(buttonFN, (buttonOffOn))        

    return iterations, angle, changeLW, orientation, reverse, offOn

def main():

    # Create a font for rendering text
    font = pygame.font.SysFont("Courier", 16)

    angle = 20
    iterations = 8
    changeLW = 0
    reverse = 0
    offOn = 0
    mPosition = 0,0
    orientation = -90

    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop

        # sets side menu size
        sideMenuWidth = 250

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Draws the tree fractal
        drawTree((mainSurfaceWidth - sideMenuWidth) / 2, mainSurfaceHeight - 10, orientation, iterations, angle, changeLW)

        # Runs the sideMenu()
        iterations, angle, changeLW, orientation, reverse, offOn= sideMenu(sideMenuWidth, iterations, angle, changeLW, orientation, reverse, offOn, mPosition, ev)

        # Copy the text surface to the main surface
        line1 = font.render("Iterations: " + str(iterations) + " Angle: " + str(angle) + " Orientation: " + str(-orientation), False, (0,0,0))
        line2 = font.render("Lind Width Incrementer: " + str(changeLW), False, (0,0,0))
        main_surface.blit(line1, (10, 10))
        main_surface.blit(line2, (10, 30))

        # Puts everything on display now that it has all been drawn
        pygame.display.flip()

        # Delays the program, makes the output from the autoAngle function look better, otherwise it's too fast
        pygame.time.delay(30)

    pygame.quit()


main()

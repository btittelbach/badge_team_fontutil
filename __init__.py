#!/usr/bin/python3
import badge
import display
import buttons
import system
import virtualtimers

known_fonts_ = [
    "org18",                  #Legacy font name
    "org01_8",                #
    "fairlight8",             #
    "fairlight12",            #
    "dejavusans20",           #SHA2017
    "permanentmarker22",      #SHA2017
    "permanentmarker36",      #SHA2017
    "roboto_black22",         #SHA2017
    "roboto_blackitalic24",   #SHA2017
    "roboto_regular12",       #SHA2017
    "roboto_regular18",       #SHA2017 
    "roboto_regular22",       #SHA2017
    "weather42",              #SHA2017
    "pixelade13",             #SHA2017
    "7x5",                    #CAMPZONE2019
    "ocra16",                 #CYBER
    "ocra22",                 #CYBER
    "exo2_regular22",         #TROOPERS
    "exo2_thin22",            #TROOPERS
    "exo2_bold22",            #TROOPERS
    "exo2_regular18",         #TROOPERS
    "exo2_thin18",            #TROOPERS
    "exo2_bold18",            #TROOPERS
    "exo2_regular12",         #TROOPERS
    "exo2_thin12",            #TROOPERS
    "exo2_bold12"]            #TROOPERS

current_font_ = 0

def clearDisplay():
    for x in range(0,2):
        display.drawRect(0, 0, display.width(), display.height(), True, 0xffffff) ## clear display
        display.flush()

def drawChars(font):
    x = 0
    y = 0
    maxh_this_row = 0
    for c in range(0,127):
        char = "%c" % (c)
        print(c,char)
        tw = display.getTextWidth(char, font)
        th = display.getTextHeight(char, font)
        maxh_this_row = max(th, maxh_this_row)
        if tw > 0 and th > 0:
            if tw + x >= display.width():
                y += maxh_this_row
                maxh_this_row = 0
                x = 0
            display.drawText(x,y, char, 0, font)
            x += tw

def drawFont():
    global current_font_
    print("========")
    print(known_fonts_[current_font_])
    clearDisplay()
    drawChars(known_fonts_[current_font_])
    print(known_fonts_[current_font_])
    print("========")
    display.flush()

def nextFont(pressed):
    global current_font_
    if pressed:
        return
    current_font_ += 1
    current_font_ %= len(known_fonts_)
    drawFont()

def prevFont(pressed):
    global current_font_
    if pressed:
        return
    current_font_ -= 1
    current_font_ %= len(known_fonts_)
    drawFont()

def buttonExitApp(pressed):
    system.home()


buttons.attach(buttons.BTN_A, nextFont)
buttons.attach(buttons.BTN_B, prevFont)
buttons.attach(buttons.BTN_START, buttonExitApp)

drawFont()
from microbit import *
from random import randint
x = randint(1,3)
y = randint(1,3)
sensX = 1
sensY = 1
planchex = 1

while True:
  display.set_pixel(x,y,9)
  for i in range(0,10):         #boucle de test de boutons
    if button_a.is_pressed():
      display.set_pixel(planchex,4,0)   
      display.set_pixel(planchex+1,4,0)
      if planchex < 3:                  #si la planche est en dessous de 
        planchex += 1                   # 3 alors ajoute 1
      display.set_pixel(planchex,4,9)
      display.set_pixel(planchex+1,4,9)
    elif button_b.is_pressed():
      display.set_pixel(planchex,4,0)
      display.set_pixel(planchex+1,4,0)
      if planchex > 0: 
         planchex -= 1
      display.set_pixel(planchex,4,9)
      display.set_pixel(planchex+1,4,9)
    sleep(100)

  display.set_pixel(x,y,0)
  #affiche planche
  display.set_pixel(planchex,4,9)
  display.set_pixel(planchex+1,4,9)
  if x == 4:
    sensX = -1
  elif x == 0:
    sensX = 1
  if y == 4:
    display.scroll("Game over")
    #game over
  elif y == 0:
    sensY = 1
  if (x == planchex or x == planchex+1) and(y == 3):
    sensY = -1
  x += sensX
  y += sensY

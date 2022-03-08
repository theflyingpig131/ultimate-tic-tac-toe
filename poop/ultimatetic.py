import pygame
import math
pygame.display.set_caption('Ultimate Tic-Tac-Toe')
global turn, used, save, ow, xw, poophi
poophi = 0
turn = 0
xw = []
ow = []
used = []
save = []
check = 0
next = 5
def getcoord(mango):
  if mango == 1:
    coord = [0, 0]
  elif mango == 2:
    coord = [200, 0]

  elif mango == 3:
    coord = [400, 0]
  elif mango == 4:
    coord = [0, 200]
  elif mango == 5:
    coord = [200, 200]
  elif mango == 6:
    coord = [400, 200]
  elif mango == 7:
    coord = [0, 400]
  elif mango == 8:
    coord = [200, 400]
  elif mango == 9:
    coord = [400, 400]
  return coord
def setup():
  global screen, w, h, save, ow, next, xw
  w = 600
  
  h = 600
  screen = pygame.display.set_mode((w, h))
  screen.fill((255,255,255))
  coord = getcoord(next)


  if next != 0:

    pygame.draw.rect(screen, (100, 200, 100), pygame.Rect(coord[0], coord[1], 200, 200))
  if next == 0:
    pygame.draw.rect(screen, (100, 200, 100), pygame.Rect(coord[0], coord[1], 600, 600))
  pygame.draw.line(screen, (0, 0, 0), (w / 3, 0), (w / 3, h), 7)  
  pygame.draw.line(screen, (0, 0, 0), (w / 3 * 2, 0), (w / 3 * 2, h), 7)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 3), (w, h / 3), 7)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 3 * 2), (w, h / 3 * 2), 7)

  pygame.draw.line(screen, (0, 0, 0), (w / 9, 0), (w / 9, h), 3)
  pygame.draw.line(screen, (0, 0, 0), (w / 9 * 2, 0), (w / 9 * 2, h), 3)
  pygame.draw.line(screen, (0, 0, 0), (w / 9 * 4, 0), (w / 9 * 4, h), 3)
  pygame.draw.line(screen, (0, 0, 0), (w / 9 * 5, 0), (w / 9 * 5, h), 3)
  pygame.draw.line(screen, (0, 0, 0), (w / 9 * 7, 0), (w / 9 * 7, h), 3)
  pygame.draw.line(screen, (0, 0, 0), (w / 9 * 8, 0), (w / 9 * 8, h), 3)

  pygame.draw.line(screen, (0, 0, 0), (0, h / 9), (w, h / 9), 3)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 9 * 2), (w, h / 9 * 2), 3)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 9 * 4), (w, h / 9 * 4), 3)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 9 * 5), (w, h / 9 * 5), 3)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 9 * 7), (w, h / 9 * 7), 3)
  pygame.draw.line(screen, (0, 0, 0), (0, h / 9 * 8), (w, h / 9 * 8), 3)
  for x in save:
    if x[2] == "x":
      image = pygame.image.load('x.png'). convert_alpha()
      image = pygame.transform.scale(image, (60, 60))       
      screen.blit(image, (x[0], x[1]))
    elif x[2] == "o":
      image = pygame.image.load('o.png'). convert_alpha()
      image = pygame.transform.scale(image, (60, 90))       
      screen.blit(image, (x[0], x[1]))
  for lol in ow:
    coord = getcoord(lol)
    image = pygame.image.load('o.png'). convert_alpha()
    image = pygame.transform.scale(image, (200, 300))       
    screen.blit(image, (coord[0], coord[1] - 50))
  for poo in xw:
    coord = getcoord(poo)
    image = pygame.image.load('x.png'). convert_alpha()
    image = pygame.transform.scale(image, (200, 200))       
    screen.blit(image, (coord[0], coord[1]))
  pygame.display.flip()
  winchecks()
  choose()

def x(row, col, next, side, top):
  global screen, used, save
  image = pygame.image.load('x.png'). convert_alpha()
  image = pygame.transform.scale(image, (60, 90)) 
  for x in used:
    if int(x[0]) == row and int(x[1]) == col:
      choose()
  for p in range(1, 3):
    if p == 1:
      
      if row == 1:
        y = 0
      for l in range(2, 9):
          if row == l:
            y = 70 + (l - 2) * 68  
    elif p == 2:
      if col == 1:
        x = 0
      for l in range(2, 9):
          if col == l:
            x = 70 + (l - 2) * 68  
  used += [(row, col, "x", next, side, top)]
  save += [(x, y, "x")]
  screen.blit(image, (x, y))


def o(row, col, next, side, top):
  global screen, used, save
  image = pygame.image.load('o.png'). convert_alpha()
  image = pygame.transform.scale(image, (60, 90)) 
  for x in used:
    
    if x[0] == row and x[1] == col:
      choose()
  for p in range(1, 3):
    if p == 1:
      
      if row == 1:
        y = 0
      for l in range(2, 9):
          if row == l:
            y = 70 + (l - 2) * 67  
    elif p == 2:
      if col == 1:
        x = 0
      for l in range(2, 9):
          if col == l:
            x = 70 + (l - 2) * 66 
  if row == 0:
    choose()
  for p in range(1, 3):
    if p == 1:
      
      if row == 1:
        y = -15
      for l in range(2, 9):
          if row == l:
            y = 65 + (l - 2) * 65
    elif p == 2:
      if col == 1:
        x = 0
      for l in range(2, 9):
          if col == l:
            x = 70 + (l - 2) * 67 

  used += [(row, col, "o", next, side, top)]
  save += [(x, y, "o")]

  screen.blit(image, (x, y))
def winchecks():
  global used, h, w, xw, ow
  s1 = []

  xs = []
  os = []
  for x in used:
    
    if x[4] == 1 and x[5] == 1:
      num = 1
    elif x[4] == 2 and x[5] == 1:
      num = 2
    elif x[4] == 3 and x[5] == 1:
      num = 3
    elif x[4] == 1 and x[5] == 2:
      num = 4
    elif x[4] == 2 and x[5] == 2:
      num = 5
    elif x[4] == 3 and x[5] == 2:
      num = 6
    elif x[4] == 1 and x[5] == 3:
      num = 7
    elif x[4] == 2 and x[5] == 3:
      num = 8
    elif x[4] == 3 and x[5] == 3:
      num = 9
    #Check what it is
    bs = int(x[3])
    if x[2] == "x":
      
      xs += [(num, bs)]
      scheck = []
      for l in xs:
        xo = 0
        if l[1] == bs:
          scheck += l
          scheck.remove(l[1])
        scheck.sort()
    elif x[2] == "o":
      os += [(num, bs)]
      scheck = []
      for l in os:
        xo = 1
        if l[1] == bs:
          scheck += l
          scheck.remove(l[1])
        scheck.sort()
    win = bwc(scheck)
    if win == 1:
      coord = getcoord(bs)
      meow = 0
      if xo == 0:
        for m in ow:
          if m == bs:
            meow = 1
        if meow != 1:
          image = pygame.image.load('x.png'). convert_alpha()
          image = pygame.transform.scale(image, (200, 200))       
          screen.blit(image, (coord[0], coord[1]))
        lol = 0
        for m in xw:
            if m == bs:
              lol = 1
        if lol == 0:
            xw += [bs]
        pygame.display.update()
        poophi = 0
        bigwinc()
      if xo == 1:
        lol = 0
        meow = 0
        for m in ow:
          if m == bs:
            meow = 1
        if meow == 0:
          ow += [bs]
    
          image = pygame.image.load('o.png'). convert_alpha()
          image = pygame.transform.scale(image, (200, 300))       
          screen.blit(image, (coord[0], coord[1] - 50))
          pygame.display.update()
          poophi = 1
        bigwinc()



    

      
    
def choose():
  global turn, next
  running = True
  plop = 0
  for n in used:
  
    if n[3] == next:
      plop += 1
  if plop == 9:
    next = 0
    
    setup()
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        number = 1
        stop = False
        row = 0
        col = 0
        for l in range(1, 10):

          if stop == False:

              if pos[0] < w / 9 * number:
                col = number
                stop = True
          number += 1

        number = 1
        stop = False
        for l in range(1, 10):

          if stop == False:
            if pos[1] < h / 9 * number:
              row = number

              stop = True
          number += 1
  
        if next != 0:
          if (col < 4) and (row < 4) and (next != 1):
            choose()
          elif (col > 3 and col < 7) and (row < 4) and (next != 2):
            choose()
          elif (col > 6) and (row < 4) and (next != 3):
            choose()
          elif (col < 4) and (row > 3 and row < 7) and (next != 4):
            choose()
          elif (col > 3 and col < 7) and (row > 3 and row < 7) and (next != 5):
            choose()
          elif (col > 6) and (row > 3 and row < 7) and (next != 6):
            choose()
          elif (col < 4) and (row > 6) and (next != 7):
            choose()
          elif (col > 3 and col < 7) and (row > 6) and (next != 8):
            choose()
          elif (col > 6) and (row > 6) and (next != 9):
            choose()


        if col == 1 or col == 4 or col == 7:
          side = 1
        elif col == 2 or col == 5 or col == 8:
          side = 2
        elif col == 3 or col == 6 or col == 9:
          side = 3
        if row == 1 or row == 4 or row == 7:
          top = 1
        elif row == 2 or row == 5 or row == 8:
          top = 2
        elif row == 3 or row == 6 or row == 9:
          top = 3
        
        tnext = next
        if side == 1 and top == 1:
          next = 1
        elif side == 2 and top == 1:
          next = 2
        elif side == 3 and top == 1:
          next = 3
        elif side == 1 and top == 2:
          next = 4
        elif side == 1 and top == 3:
          next = 7
        elif side == 2 and top == 2:
          next = 5
        elif side == 2 and top == 3:
          next = 8
        elif side == 3 and top == 2:
          next = 6
        elif side == 3 and top == 3:
          next = 9
        plop = 0


        if turn == 0:
          turn = 1
          x(row, col, tnext, side, top)
          setup()

          pygame.display.update()
        elif turn == 1:
          turn = 0
          o(row, col, tnext, side, top)
          setup()

          pygame.display.update()
  

def freeze():
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

def bigwinc():
  global xw, ow, poophi
  xw.sort()
  ow.sort()
  if poophi == 0:
    thing = xw
  elif poophi == 1:
    thing = ow
  win = bwc(thing)
  if win == 1:
    freeze()
  poophi += 1
  if poophi != 2:
    bigwinc()
  else:
    poophi = 0
def bwc(thing):
  global poophi
  win = 0
    #Win = true if {1, 2, 3}{1, 4, 7}{1, 5, 9}{2, 5, 8}{3, 6, 9}{3, 5, 7}{4, 5, 6}{7, 8, 9}
  try:
    if (thing[0] == 3 or thing[1] == 3 or thing[2] == 3) and (thing[1] == 6  or thing[2] == 6 or thing[3] == 6 or thing[4] == 6 or thing[5] == 6) and (thing[2] == 9 or thing[3] == 9 or thing[4] == 9 or thing[5] == 9 or thing[6] == 9 or thing[7] == 9 or thing[8] == 9):
        win = 1
  except IndexError:
    pass 
  try:  
    if (thing[0] == 1) and (thing[1] == 2) and (thing[2] == 3):
      win = 1
  except IndexError:
    pass
  try:

    if (thing[0] == 1) and (thing[1] == 4 or thing[2] == 4 or thing[3] == 4) and (thing[2] == 7 or thing[3] == 7 or thing[4] == 7 or thing[5] == 7 or thing[6] == 7):
      win = 1
  except IndexError:
    pass
  try:
    if (thing[0] == 1) and (thing[1] == 5 or thing[2] == 5 or thing[3] == 5 or thing[4] == 5) and (thing[2] == 9 or thing[3] == 9 or thing[4] == 9 or thing[5] == 9 or thing[6] == 9 or thing[7] == 9 or thing[8] == 9):
      win = 1
  except IndexError:
    pass
  try:
    if (thing[0] == 2 or thing[1] == 2) and (thing[1] == 5 or thing[2] == 5 or thing[3] == 5 or thing[4] == 5) and (thing[2] == 8 or thing[3] == 8 or thing[4] == 8 or thing[5] == 8 or thing[6] == 7 or thing[7] == 8):
      win = 1
  except IndexError:
    pass
  try:
    if (thing[0] == 3 or thing[1] == 3 or thing[2] == 3) and (thing[1] == 5 or thing[2] == 5 or thing[3] == 5 or thing[4] == 5) and (thing[2] == 7 or thing[3] == 7 or thing[4] == 7 or thing[5] == 7 or thing[6] == 7):
      win = 1
  except IndexError:
    pass
  try:
      if (thing[0] == 4 or thing[1] == 4 or thing[2] == 4 or thing[3] == 4) and (thing[1] == 5 or thing[2] == 5 or thing[3] == 5 or thing[4] == 5) and (thing[2] == 6 or thing[3] == 6 or thing[4] == 6 or thing[5] == 6):
        win = 1
  except IndexError:
    pass
  try:
    if (thing[1] == 7 or thing[0] == 7 or thing[2] == 7 or thing[3] == 7 or thing[4] == 7 or thing[5] == 7 or thing[6] == 7) and (thing[0] == 8 or thing[1] == 8 or thing[2] == 8 or thing[3] == 8 or thing[4] == 8 or thing[5] == 8 or thing[6] == 7 or thing[7] == 8) and (thing[0] == 9 or thing[1] == 9 or thing[2] == 9 or thing[3] == 9 or thing[4] == 9 or thing[5] == 9 or thing[6] == 9 or thing[7] == 9 or thing[8] == 9):
      win = 1
  except IndexError:
    pass
  return win

if __name__ == "__main__":
  setup()

#Python Source Code

#Library Imports
import pygame
from random import randint as ri
pygame.init()
import time
import cv2 as cv
import math


#GAME Parameters
screen = pygame.display.set_mode([600, 750])
GAME_x = 20
GAME_y = 40
GAME_width = 440
GAME_height = 400
GAME_border = 3
WHITE=(255,255,255)
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
custom_color_1=(10,145,80)
screen.fill(BLACK)
INT_MAX = 100000000000000
#Class Definitions
class Button:
    def __init__ (self, colour, x, y, width, height):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def create(self,screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y,self.width ,self.height])


#Function Definition : Point inside Game ?
def point_inside_game(x,y):
    if x>GAME_x+GAME_border and x<GAME_x + GAME_width - GAME_border:
                if y>GAME_y+GAME_border and y < GAME_y + GAME_height - GAME_border:
                    return(True)
    return(False)


#Function Definition : Random Point Generator inside Game
def random_point():
    x_random = ri(GAME_x+GAME_border , GAME_x + GAME_width - GAME_border - 1)
    y_random = ri(GAME_y+GAME_border , GAME_y + GAME_height - GAME_border - 1 )
    return((x_random, y_random))


#Function Definition : Point inside given Rectangle ?
def point_inside_rec(xr,yr,wr,hr,x,y):
    if x> xr and x < xr + wr:
                if y > yr and y < yr + hr:
                    return(True)
    return(False)


#Function Definition : Point to Point Distance
def p2p_dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return (((x1-x2)**2 + (y1-y2)**2 )**0.5)


#Function Definition : Text on Button
def ClickText():
    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render('CLICK HERE', True, BLACK)
    textRect = text.get_rect()
    textRect.center = (75, 495)
    screen.blit(text, textRect)


#Function Definition : Description Text
def DesText(s,x=315,y=485):
    pygame.draw.rect(screen,BLACK,(125,470,500,30))
    font = pygame.font.SysFont('segoeuisemilight', 15)
    text = font.render('%s'%(s), True, WHITE)
    textRect = text.get_rect()
    #textRect.center = (255, 460)
    textRect.center = (x, y)
    screen.blit(text, textRect)


#Function Definition :RRT Algorithm
def RRT(x,y,parent):
    if (x,y) not in parent and screen.get_at((x,y)) == (0,0,0,255):
        x_m,y_m=-1,-1
        cur_min=INT_MAX
        for v in parent:
            if p2p_dist(v,(x,y))<cur_min:
                x_m,y_m=v
                cur_min =  p2p_dist(v,(x,y))

        good = True
        ans=[]
        if abs(x_m - x)<abs(y_m-y):
            if y_m<y:
                for u in range(y_m+1, y+1):
                    x_cur = int (((x_m - x)/(y_m - y))*( u - y) + x)
                    y_cur = u
                    if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
                        good=False
                        break
                if good:
                    ans=[int (((x_m - x)/(y_m - y))*( y_m+Step - y) + x),y_m+Step]
            else:
                for u in range(y, y_m):
                    x_cur = int(((x_m - x)/(y_m - y))*( u - y) + x)
                    y_cur = u
                    if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
                        good=False
                        break
                if good:
                    ans=[int (((x_m - x)/(y_m - y))*( y_m-Step - y) + x),y_m-Step]

        else:
            if x_m<x:
                for u in range(x_m + 1, x+1):
                    x_cur = u
                    y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
                    if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
                        good=False
                        break
                if good:
                    ans=[x_m+Step,int( ((y_m-y)/(x_m-x))*(x_m+Step-x) + y ) ]
            else:
                for u in range(x , x_m):
                    x_cur = u
                    y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
                    if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
                        good=False
                        break
                if good:
                    ans=[x_m-Step,int( ((y_m-y)/(x_m-x))*(x_m-Step-x) + y ) ]
        return(good,x_m,y_m,ans)
    return(False,-1,-1,[])

def canny(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (13,13), cv.BORDER_DEFAULT)
    canny = cv.Canny(blur, 125, 175)
    return canny

def c(e):
  coords=[]
  l1=e.tolist()

  for i in range(e.shape[0]):
    for j in range(e.shape[1]):
      if l1[i][j]==255:
        coords.append((i,j))
  return coords


def a(coords):
  coord_dict = {}
  #
  for x, y in coords:
      if x not in coord_dict:
          coord_dict[x] = []
      coord_dict[x].append(y)

  result=[]

  for key in list(coord_dict.keys()):
      for i in range(len(coord_dict[key])-1):
          diff=coord_dict[key][i+1]-coord_dict[key][i]
          if 6<=diff<=12:
              mean=math.floor((diff/2)+coord_dict[key][i])
              result.append([key,mean])

  return result

def b(coords):

  coord_dict1 = {}
  #
  for x, y in coords:
      if y not in coord_dict1:
        coord_dict1[y]=[]
      coord_dict1[y].append(x)

  result1=[]

  for key in list(coord_dict1.keys()):
      for i in range(len(coord_dict1[key])-1):
          diff=coord_dict1[key][i+1]-coord_dict1[key][i]
          if 6<=diff<=12:
              mean=math.floor((diff/2)+coord_dict1[key][i])
              result1.append([key,mean])
  return result1
running = True

#Button for Game
#pygame.draw.rect(screen,WHITE,(GAME_x,GAME_y,GAME_width,GAME_height),GAME_border)

image = pygame.image.load("world1.jpg")
img_width = image.get_width()
img_height = image.get_height()

# Position to draw image 
img_x = GAME_x 
img_y = GAME_y

# # Draw image onto screen
screen.blit(image, (img_x, img_y))  
B1 = Button(WHITE, 25, 470, 100, 50)
B1.create(screen)
OBS=dict()

#Number of forward Steps towards random sampled point
Step = 10
#Start stores a single point [Starting point- RED Point]
Start=[]

#End stores a set of destination point [Destination point- Green Point]
#Multiple points allowed to make the point appear bigger, and fast discovery,
#due to huge number of pixels in this game
End=set()


#parent stores the graph
parent=dict()
level=1
ClickText()
DesText("Instruction :",y=460)
DesText("Draw the Path, then CLICK White Button")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if running==False:
            break
        m = pygame.mouse.get_pressed()
        x,y = pygame.mouse.get_pos()

        if m[0]==1:
            if point_inside_rec(B1.x,B1.y, B1.width, B1.height,x,y):
                    #print("BUTTON", level)
                    if level==1 and Start==[]:
                        level+=1
                        B1.colour=RED
                        DesText("Draw the Starting point, then CLICK RED Button")
                    elif level==2 and Start:
                        level+=1
                        B1.colour=GREEN
                        DesText("Draw the Destination point, then CLICK GREEN Button")
                    elif level==3 and End!=set():
                        level+=1
                        B1.colour=BLUE
                        DesText("Path is being explored using RRT Algorithm")
                    B1.create(screen)
                    ClickText()
                    continue
            elif level==1:
                if point_inside_game(x,y):
                    #print("OBSTABLE ",x,y)
                    OBS[(x,y)]=1
                    pygame.draw.circle(screen, BLACK, (x, y), 3)
            elif level == 2 and Start==[]:
                if point_inside_game(x,y):
                    #print("START ",x,y)
                    Start=(x,y)
                    pygame.draw.circle(screen, RED, (x, y), 3)
            elif level == 3:
                if point_inside_game(x,y):
                    #print("END ",x,y)
                    End.add((x,y))
                    pygame.draw.circle(screen, GREEN, (x, y), 3)

        if level>=4:
            running = False
            break
    pygame.display.update()

running = True
parent[Start]=(-1,-1)
Trace=[]
Timer =  time.time()
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    x,y =random_point()
    if (time.time() - Timer) > 5:
        Step=5
    good,x_m,y_m,ans=RRT(x,y,parent)

    if good and ans:
        x_cur = ans[0]
        y_cur = ans[1]
        if screen.get_at((x_cur,y_cur)) != (255,255,255,255) and (x_cur,y_cur) not in parent:
            parent[(x_cur,y_cur)]=(x_m,y_m)
            if screen.get_at((x_cur,y_cur)) == (0, 255, 0, 255):
                Trace=(x_cur,y_cur)
                #print("End", x_cur, y_cur)
                running = False
            pygame.draw.line(screen, BLUE, (x_cur,y_cur), (x_m,y_m), 2)
    pygame.display.update()

running = True
#This loop gets the route back to Start point
path=[]


cv.waitKey(0)
#print(Trace)

while(Trace and running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    while(Trace!=Start):
        x,y = parent[Trace]
        path.append([x,y])
        pygame.draw.line(screen, GREEN, (x,y), Trace, 2)
        Trace=(x,y)
        #print("Trace",x,y)
    DesText("Green Colored Path is the Required Path")
    pygame.display.update()
print( "the path travarse output are: ", path)
#Quit the Game
pygame.quit()

# img = cv.imread('New folder/path2.jpg')
# img1 = np.copy(img)
# canny1 = canny(img1)
# cv.imwrite('New folder/ canny123.jpg',canny1)
# # print(type (cropped_image))

# coords1=c(canny1)
# output = a(coords1)
# output1 = b(coords1)
# print(cropped_image)
# print(coords1)
# print(output)
# print((output1))


# x,y = zip(*coords1)
# plt.figure(figsize=(6, 6))
# plt.scatter(x,y,s=1)


# x,y =zip(*output)
# plt.figure(figsize=(6, 6))
# plt.scatter(x,y,s=1)


# image = np.zeros((img1.shape[0], img1.shape[1], 3), dtype=np.uint8)
# x1,y1 =zip(*output1)
# plt.figure(figsize=(6, 6))
# plt.scatter(x1,y1,s=1)
# image1 = np.zeros((img1.shape[0], img1.shape[1], 3), dtype=np.uint8)


# for x, y in output:
#     # Draw a 5px radius red circle at coords
#     cv.circle(image, (y,x), 2, (0, 0, 255), -1)

# for x1, y1 in output1:
#     cv.circle(image1, (x1,y1), 2, (0,0,255),-1)



# bitwise_and = cv.bitwise_and(image, image1)

# cv.imshow('Bitwise AND', image1)
# cv.imwrite('New folder/verticleimage.jpg', image)
# cv.imwrite('New folder/horizontalimage.png', image1)

# cv.imshow('canny_result', image)
# cv.imwrite('New folder/output_image2.png', image)

#---------------------------------------------------------------
# img = cv.imread('New folder/output_image.png')
# rgba = np.zeros((image1.shape[0], image1.shape[1], 4))

# # Copy RGB values to RGBA channels
# rgba[:,:,0] = image1[:,:,0]   # Red channel  
# rgba[:,:,1] = image1[:,:,1]   # Green channel
# rgba[:,:,2] = image1[:,:,2]   # Blue channel

# # Set alpha channel to full opacity 
# rgba[:,:,3] = 255
# for y in range(rgba.shape[1]):
#     for x in range(rgba.shape[0]):
#         if np.all(rgba[x, y] == (0, 0, 0, 255)):
#             rgba[x, y] = (0, 0, 0, 0)

# cv.imwrite('New folder/transperant2.png', rgba)
# #----------------------Blending--------------------------------------------
# background = cv.imread('New folder/output_image2.png')

# # Load the PNG image with an alpha channel (foreground)
# foreground = cv.imread('New folder/transperant2.png')

# blended = cv.add(foreground, background)
# Save or display the result

# cv.imshow('Blended_Image.jpg', blended)
# cv.imwrite('New folder/Blended_Image.jpg', blended)
# cv.imshow('Superimposed Image', blended)

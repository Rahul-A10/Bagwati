##########################################################
import rospy
from geometry_msgs.msg import Twist, Point, Pose, Quaternion, Vector3
from nav_msgs.msg import Odometry as odom
from tf.transformations import euler_from_quaternion
from math import atan2


# #Library Imports
# import pygame
# from random import randint as ri
# pygame.init()
# import time
# import cv2 as cv
# import numpy as np
# import math
# from PIL import Image
# import matplotlib.pyplot as plt

# #############################################################


# #GAME Parameters
# screen = pygame.display.set_mode([600, 750])
# GAME_x = 20
# GAME_y = 40
# GAME_width = 440
# GAME_height = 400
# GAME_border = 3
# WHITE=(255,255,255)
# BLUE=(0,0,255)
# BLACK=(0,0,0)
# RED=(255,0,0)
# GREEN=(0,255,0)
# custom_color_1=(10,145,80)
# screen.fill(BLACK)
# INT_MAX = 100000000000000
# #Class Definitions
# class Button:
#     def __init__ (self, colour, x, y, width, height):
#         self.colour = colour
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#     def create(self,screen):
#         pygame.draw.rect(screen, self.colour, [self.x, self.y,self.width ,self.height])


# #Function Definition : Point inside Game ?
# def point_inside_game(x,y):
#     if x>GAME_x+GAME_border and x<GAME_x + GAME_width - GAME_border:
#                 if y>GAME_y+GAME_border and y < GAME_y + GAME_height - GAME_border:
#                     return(True)
#     return(False)


# #Function Definition : Random Point Generator inside Game
# def random_point():
#     x_random = ri(GAME_x+GAME_border , GAME_x + GAME_width - GAME_border - 1)
#     y_random = ri(GAME_y+GAME_border , GAME_y + GAME_height - GAME_border - 1 )
#     return((x_random, y_random))


# #Function Definition : Point inside given Rectangle ?
# def point_inside_rec(xr,yr,wr,hr,x,y):
#     if x> xr and x < xr + wr:
#                 if y > yr and y < yr + hr:
#                     return(True)
#     return(False)


# #Function Definition : Point to Point Distance
# def p2p_dist(p1,p2):
#     x1,y1=p1
#     x2,y2=p2
#     return (((x1-x2)**2 + (y1-y2)**2 )**0.5)


# #Function Definition : Text on Button
# def ClickText():
#     font = pygame.font.Font('freesansbold.ttf', 12)
#     text = font.render('CLICK HERE', True, BLACK)
#     textRect = text.get_rect()
#     textRect.center = (75, 495)
#     screen.blit(text, textRect)


# #Function Definition : Description Text
# def DesText(s,x=315,y=485):
#     pygame.draw.rect(screen,BLACK,(125,470,500,30))
#     font = pygame.font.SysFont('segoeuisemilight', 15)
#     text = font.render('%s'%(s), True, WHITE)
#     textRect = text.get_rect()
#     #textRect.center = (255, 460)
#     textRect.center = (x, y)
#     screen.blit(text, textRect)


# #Function Definition :RRT Algorithm
# def RRT(x,y,parent):
#     if (x,y) not in parent and screen.get_at((x,y)) == (0,0,0,255):
#         x_m,y_m=-1,-1
#         cur_min=INT_MAX
#         for v in parent:
#             if p2p_dist(v,(x,y))<cur_min:
#                 x_m,y_m=v
#                 cur_min =  p2p_dist(v,(x,y))

#         good = True
#         ans=[]
#         if abs(x_m - x)<abs(y_m-y):
#             if y_m<y:
#                 for u in range(y_m+1, y+1):
#                     x_cur = int (((x_m - x)/(y_m - y))*( u - y) + x)
#                     y_cur = u
#                     if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
#                         good=False
#                         break
#                 if good:
#                     ans=[int (((x_m - x)/(y_m - y))*( y_m+Step - y) + x),y_m+Step]
#             else:
#                 for u in range(y, y_m):
#                     x_cur = int(((x_m - x)/(y_m - y))*( u - y) + x)
#                     y_cur = u
#                     if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
#                         good=False
#                         break
#                 if good:
#                     ans=[int (((x_m - x)/(y_m - y))*( y_m-Step - y) + x),y_m-Step]

#         else:
#             if x_m<x:
#                 for u in range(x_m + 1, x+1):
#                     x_cur = u
#                     y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
#                     if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
#                         good=False
#                         break
#                 if good:
#                     ans=[x_m+Step,int( ((y_m-y)/(x_m-x))*(x_m+Step-x) + y ) ]
#             else:
#                 for u in range(x , x_m):
#                     x_cur = u
#                     y_cur = int( ((y_m-y)/(x_m-x))*(u-x) + y )
#                     if screen.get_at((x_cur,y_cur)) == (255,255,255,255):
#                         good=False
#                         break
#                 if good:
#                     ans=[x_m-Step,int( ((y_m-y)/(x_m-x))*(x_m-Step-x) + y ) ]
#         return(good,x_m,y_m,ans)
#     return(False,-1,-1,[])

# def canny(img):
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#     blur = cv.GaussianBlur(gray, (13,13), cv.BORDER_DEFAULT)
#     canny = cv.Canny(blur, 125, 175)
#     return canny

# def c(e): # function to generate coordinates from image
#   coords=[]
#   l1=e.tolist()

#   for i in range(e.shape[0]):
#     for j in range(e.shape[1]):
#       if l1[i][j]==255:
#         coords.append((i,j))
#   return coords


# def a(coords): # function to generate mean point frmo rows (x axis)
#   coord_dict = {}
#   #
#   for x, y in coords:
#       if x not in coord_dict:
#           coord_dict[x] = []
#       coord_dict[x].append(y)

#   result=[]

#   for key in list(coord_dict.keys()):
#       for i in range(len(coord_dict[key])-1):
#           diff=coord_dict[key][i+1]-coord_dict[key][i]
#           if 6<=diff<=12:
#               mean=math.floor((diff/2)+coord_dict[key][i])
#               result.append([key,mean])

#   return result

# def b(coords): # functino to generate mean from columns (y axis)
#   coord_dict1 = {}
#   #
#   for x, y in coords:
#       if y not in coord_dict1:
#         coord_dict1[y]=[]
#       coord_dict1[y].append(x)

#   result1=[]

#   for key in list(coord_dict1.keys()):
#       for i in range(len(coord_dict1[key])-1):
#           diff=coord_dict1[key][i+1]-coord_dict1[key][i]
#           if 6<=diff<=12:
#               mean=math.floor((diff/2)+coord_dict1[key][i])
#               result1.append([key,mean])
#   return result1

# ############################################################

def newOdom(data):
    global x
    global y
    global theta

    x=data.pose.pose.position.x
    y=data.pose.pose.position.y
    rotq=data.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rotq.x,rotq.y,rotq.z,rotq.w])

def returnhome():
    home=odom()
    home.pose.pose=Pose(Point(0,0,0),0)
    home.twist.twist=Twist(Vector3(0,0,0),Vector3(0,0,0))
    pub1.publish(home)

# #############################################################


# running = True
# #Button for Game
# #pygame.draw.rect(screen,WHITE,(GAME_x,GAME_y,GAME_width,GAME_height),GAME_border)
# im = cv.imread('New folder/final_layout.png')
# grayImage = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

# (thresh, blackAndWhiteImage) = cv.threshold(grayImage, 200, 255, cv.THRESH_BINARY)
# blackAndWhiteImage3 = cv.cvtColor(blackAndWhiteImage, cv.COLOR_GRAY2BGR)
# blackAndWhiteImage3[blackAndWhiteImage==0] = (0,0,255)
# path_dirrect = 'New folder/path3.jpg'
# cv.imwrite(path_dirrect, blackAndWhiteImage3)
# image = pygame.image.load("New folder/path3.jpg")
# img_width = image.get_width()
# img_height = image.get_height()

# # Position to draw image 
# img_x = GAME_x 
# img_y = GAME_y

# # # Draw image onto screen
# screen.blit(image, (img_x, img_y))  
# B1 = Button(WHITE, 25, 470, 100, 50)
# B1.create(screen)
# OBS=dict()

# #Number of forward Steps towards random sampled point
# Step = 10
# #Start stores a single point [Starting point- RED Point]
# Start=[]

# #End stores a set of destination point [Destination point- Green Point]
# #Multiple points allowed to make the point appear bigger, and fast discovery,
# #due to huge number of pixels in this game
# End=set()


# #parent stores the graph
# parent=dict()
# level=1
# ClickText()
# DesText("Instruction :",y=460)
# DesText("Draw the Path, then CLICK White Button")
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             break
#         if running==False:
#             break
#         m = pygame.mouse.get_pressed()
#         x,y = pygame.mouse.get_pos()

#         if m[0]==1:
#             if point_inside_rec(B1.x,B1.y, B1.width, B1.height,x,y):
#                     #print("BUTTON", level)
#                     if level==1 and Start==[]:
#                         level+=1
#                         B1.colour=RED
#                         DesText("Draw the Starting point, then CLICK RED Button")
#                     elif level==2 and Start:
#                         level+=1
#                         B1.colour=GREEN
#                         DesText("Draw the Destination point, then CLICK GREEN Button")
#                     elif level==3 and End!=set():
#                         level+=1
#                         B1.colour=BLUE
#                         DesText("Path is being explored using RRT Algorithm")
#                     B1.create(screen)
#                     ClickText()
#                     continue
#             elif level==1:
#                 if point_inside_game(x,y):
#                     #print("OBSTABLE ",x,y)
#                     OBS[(x,y)]=1
#                     pygame.draw.circle(screen, BLACK, (x, y), 3)
#             elif level == 2 and Start==[]:
#                 if point_inside_game(x,y):
#                     #print("START ",x,y)
#                     Start=(x,y)
#                     pygame.draw.circle(screen, RED, (x, y), 3)
#             elif level == 3:
#                 if point_inside_game(x,y):
#                     #print("END ",x,y)
#                     End.add((x,y))
#                     pygame.draw.circle(screen, GREEN, (x, y), 3)

#         if level>=4:
#             running = False
#             break
#     pygame.display.update()

# running = True
# parent[Start]=(-1,-1)
# Trace=[]
# Timer =  time.time()
# while(running):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             break
#     x,y =random_point()
#     if (time.time() - Timer) > 5:
#         Step=5
#     good,x_m,y_m,ans=RRT(x,y,parent)

#     if good and ans:
#         x_cur = ans[0]
#         y_cur = ans[1]
#         if screen.get_at((x_cur,y_cur)) != (255,255,255,255) and (x_cur,y_cur) not in parent:
#             parent[(x_cur,y_cur)]=(x_m,y_m)
#             if screen.get_at((x_cur,y_cur)) == (0, 255, 0, 255):
#                 Trace=(x_cur,y_cur)
#                 #print("End", x_cur, y_cur)
#                 running = False
#             pygame.draw.line(screen, BLUE, (x_cur,y_cur), (x_m,y_m), 2)
#     pygame.display.update()

# running = True
# #This loop gets the route back to Start point
# path=[]

# img = cv.imread('New folder/path2.jpg')
# img1 = np.copy(img)
# canny1 = canny(img1)
# cv.imwrite('New folder/ canny123.jpg',canny1)
# # print(type (cropped_image))

# coords1=c(canny1)
# output = a(coords1)
# output1 = b(coords1)
# # print(cropped_image)
# # print(coords1)
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



# # bitwise_and = cv.bitwise_and(image, image1)

# # cv.imshow('Bitwise AND', image1)
# # cv.imwrite('New folder/verticleimage.jpg', image)
# # cv.imwrite('New folder/horizontalimage.png', image1)

# # cv.imshow('canny_result', image)
# # cv.imwrite('New folder/output_image2.png', image)

# #---------------------------------------------------------------
# img = cv.imread('New folder/output.jpg')
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
# # Save or display the result

# # cv.imshow('Blended_Image.jpg', blended)
# # cv.imwrite('New folder/Blended_Image.jpg', blended)
# # cv.imshow('Superimposed Image', blended)
# cv.waitKey(0)
# #print(Trace)
# while(Trace and running):
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#             break
#     while(Trace!=Start):
#         x,y = parent[Trace]
#         path.append([x,y])
#         pygame.draw.line(screen, GREEN, (x,y), Trace, 2)
#         Trace=(x,y)
#         #print("Trace",x,y)
#     DesText("Green Colored Path is the Required Path")
#     pygame.display.update()
# print( "the path travarse output are: ", path)
# #Quit the Game
# pygame.quit()

############################################################


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

image = pygame.image.load("New folder/final_layout.png")
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


#############################################################

x=0.0
y=0.0
theta=0.0

rospy.init_node('turtlebot_node',anonymous=True)

pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
sub=rospy.Subscriber('/odom',odom, newOdom)
pub1=rospy.Publisher('/odom',odom, queue_size=10)

speed=Twist()

r=rospy.Rate(10)
# path=[[300, 190], [290, 199], [280, 209], [270, 218], [261, 228], [251, 237], [241, 243], [231, 251], [221, 261], [211, 270], [201, 279], [191, 289], [181, 298], [171, 308], [162, 318], [152, 326], [142, 336], [132, 346], [122, 356], [112, 366], [102, 373], [92, 382], [82, 390], [72, 394], [62, 400]]
# path = [[96, 86], [96, 91], [96, 96], [95, 101], [96, 106], [96, 111], [96, 116], [96, 121], [97, 126], [96, 131], [97, 136], [96, 141], [97, 146], [97, 151], [97, 156], [92, 161], [92, 166], [92, 171], [92, 176], [92, 181], [92, 186], [92, 191], [92, 196], [92, 201], [92, 206], [92, 211], [92, 216], [92, 221], [92, 226], [92, 231], [92, 236], [92, 241], [92, 246], [90, 251], [90, 256], [90, 261], [90, 266], [90, 271], [90, 276], [90, 281], [90, 286], [90, 291], [90, 296], [91, 301], [92, 306], [92, 311], [97, 316], [102, 316], [107, 316], [112, 318], [117, 316], [122, 316], [132, 316], [142, 317], [152, 317], [162, 318], [172, 318], [182, 319], [192, 318], [202, 317], [212, 318], [222, 315], [232, 314], [242, 314], [252, 314], [262, 316], [272, 317], [282, 317], [292, 325], [297, 335], [297, 345], [297, 355], [297, 365], [297, 375], [296, 385], [296, 395], [296, 405]]
path = [[181, 70], [180, 75], [175, 77], [172, 82], [167, 85], [162, 84], [157, 85], [152, 85], [147, 84], [142, 85], [137, 84], [132, 84], [127, 84], [122, 84], [117, 83], [112, 83], [107, 83], [102, 83], [97, 88], [92, 90], [87, 95], [89, 100], [85, 105], [84, 110], [82, 115], [87, 117], [89, 122], [89, 127], [90, 132], [91, 137], [96, 140], [99, 145], [104, 146], [109, 146], [114, 147], [119, 149], [124, 150], [129, 152], [134, 154], [139, 156], [144, 160], [149, 162], [154, 165], [155, 170], [160, 173], [165, 176], [168, 181], [167, 186], [172, 190], [169, 195], [170, 200], [170, 205], [171, 210], [170, 215], [169, 220], [170, 225], [170, 230], [171, 235], [171, 240], [171, 245], [170, 250], [170, 255], [170, 260], [175, 265], [176, 270], [181, 275], [182, 280], [187, 280], [192, 281], [197, 284], [202, 286], [207, 286], [212, 285], [217, 287], [227, 286], [237, 285], [247, 283], [246, 293], [255, 303], [264, 313], [260, 323], [260, 333], [254, 343], [252, 353], [252, 363], [251, 373], [261, 383], [271, 385], [276, 395], [286, 400]]
path=list(reversed(path))
print('\n final path\n')
temp=path[0]
print(path)

for i in path:
    # origin align
    i[0]=abs(i[0]-336)
    i[1]=abs(i[1]-448)
    # scale down
    i[0]/=32
    i[1]/=32
print('\n path scaled down\n')
print(path)

goal= Point()
goal.x=path[0][0]
goal.y=path[0][1]
i=0

while not rospy.is_shutdown():
    # print("current odom values are {x},{y}".format(x=x,y=y))
    inc_x = goal.x - x
    inc_y = goal.y - y
    angle_to_theta = atan2(inc_y,inc_x)

    if(i>len(path)):
        break
    # assign orientation pose.pose.orientation.w = angle_to_theta
    # print(abs(angle_to_theta - theta))
    if abs(angle_to_theta - theta) > 0.2:
        speed.linear.x= 0
        speed.angular.z =.5
        r.sleep()
    else:
        # print("\n\nrobot is brought to a stop\n\n")
        speed.linear.x=0
        speed.angular.z=0
        pub.publish(speed)
        r.sleep()
        # print("\n\nentered\n\n")
        speed.linear.x=.5
        speed.angular.z=0
    
    if (inc_x<0.2) and (inc_y<0.2):
        #returnhome()
        print('reached destination, collecting next')
        i+=1
        speed.linear.x=0
        speed.angular.z=0
        pub.publish(speed)
        r.sleep()
        goal.x=path[i][1] # the image u is the path y axes (in gazebo)
        goal.y=path[i][0] # the image v is the path x axes (in gazebo)
    pub.publish(speed)

    r.sleep()
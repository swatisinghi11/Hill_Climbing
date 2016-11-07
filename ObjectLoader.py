import pygame
import math


class Object:

	displayScreen = 0

	def __init__(self,loadImage,imagePathorImage,x,y):
		if(loadImage):
			self.image = pygame.image.load(imagePathorImage).convert_alpha()
		else:
			self.image = imagePathorImage
		self.screenX = x
		self.globalX = x
		self.globalY = y

	def rot_center(self,image, angle):
		orig_rect = image.get_rect()
		rot_image = pygame.transform.rotate(image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		return rot_image

	def scale(self,height,width):
		self.image = pygame.transform.scale(self.image, (height, width))

	def display(self):
		Object.displayScreen.blit(self.image,[self.screenX , self.globalY])

	def rotateAndDisplay(self,rotation_angle):
		rotated_image = self.rot_center(self.image,rotation_angle)
		# Object.displayScreen.blit(self.image,[self.screenX , self.globalY])
		Object.displayScreen.blit(rotated_image,[self.screenX , self.globalY])

	def displayImage(self,image):
		Object.displayScreen.blit(image,[self.screenX , self.globalY])

	def horizontalShift(self,x):
		self.screenX -= x

	def verticalShift(self,y):
		self.globalY += y

	def setXCoordinates(self,screenX,globalX):
		self.screenX = screenX
		self.globalX = globalX

	def setYCoordinate(self,y):
		self.globalY = y

	def setAllCoordinates(self,screenX,globalX,y):
		self.screenX = screenX
		self.globalX = globalX
		self.globalY = y

	def printCoordinates(self):
		print "screenX = "+ str(self.screenX)
		print "globalX = "+ str(self.globalX)
		print "globalY = "+ str(self.globalY)

	def displayCircle(self):
		pygame.draw.circle(Object.displayScreen, [255,255,255] , [int(self.screenX),int(self.globalY)], 5)

	def get_global_Xpos(self):
		return self.globalX
	def get_global_Ypos(self):
		return self.globalY
	
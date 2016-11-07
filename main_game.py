from ObjectLoader import Object
from Stages import Stages
import pygame
from pygame import *
import math

SCORE = 0
FUEL = 100
TIME_OVER = 100
fuelDelta = 0.4
GAME_OVER = False
GAME_OVER

fuel_offset = 60
fuel_height = 50
fuel_width = 50

screen_height = 768
screen_width = 1366
offset = 300
screen_front = -630
camera_width = 1370
rectangle_number = (camera_width - screen_front)/2 +50
wheel_offset = 100
rectangle_width = 10
rectangle_height = 600

wheel_height = 50
wheel_width = 50

rider_height = 90
rider_width = 90

handle_height = 70
handle_width = 100

roadTop_height = 10 
roadTop_width = 10
wheel_rotation_angle = 0;
frameCounter = 0;
wheel_vx=0
wheel_vy=0
wheel_Y_pos=0

omega=0
acceleration=2
angular_acceleration = 2
left_key=False
right_key=False
gravity=0.4
gravity_multiplication_factor = 5;
friction=0.1
EEE=1
E=50
e=20

stage = Stages(3,screen_height)


def angles(x_pos):
	
	theta=float(math.atan((stage.getYPosition(x_pos+2,False)-stage.getYPosition(x_pos,False))/2))
	return theta

def keyEffects1():
	global  acceleration, angular_acceleration,omega,wheel_vy,wheel_vx
	sinTheta = math.sin(angles(frameCounter+wheel_offset))
	cosTheta = math.cos(angles(frameCounter+wheel_offset))
	if(FUEL <= 0):
		if wheel_vx < 0:
			wheel_vx +=  friction*cosTheta -gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx 
		else:
			wheel_vx +=  - friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx 
		return
	if right_key == True and left_key == False:
		if(wheel_vx <= 30 and wheel_vx >= 0):    
		    wheel_vx = wheel_vx + acceleration*cosTheta-friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
		    omega = wheel_vx
		elif (wheel_vx < 0):
			wheel_vx = wheel_vx + acceleration*cosTheta  + friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx
		else:
			wheel_vx = 30
			omega = 30
		    
	if right_key==False and left_key==False:
		if wheel_vx < 0:
			wheel_vx +=  friction*cosTheta -gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx 
		else:
			wheel_vx +=  - friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx 
			

	if left_key == True and right_key==False:
		if(wheel_vx > -10 and wheel_vx< 0):    
		    wheel_vx = wheel_vx - acceleration*cosTheta + friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
		    omega = wheel_vx 
		elif(wheel_vx >= 0):    
			wheel_vx = wheel_vx - acceleration*cosTheta  - friction*cosTheta - gravity_multiplication_factor*gravity*sinTheta
			omega = wheel_vx  
		else:
			wheel_vx = -10
			omega = -10
	    
def game_init():
	pygame.init()
	pygame.font.init()
	SIZE = [screen_width,screen_height]
	screen = display.set_mode((0,0),FULLSCREEN)
	# pygame.display.set_caption("Climb The Hill By Swati and Veerendra")
	Object.displayScreen = screen
	

def run():
	global TIME_OVER,GAME_OVER,FUEL,SCORE, wheel_rotation_angle, frameCounter, left_key,right_key,wheel_vx,wheel_vy,wheel_Y_pos,E
	game_init()
	clock = pygame.time.Clock()

	background = Object(True,"back5.jpg",0,0)
	background.scale(screen_width,screen_height)

	road = Object(True,"123.jpg",0,0)
	road.scale(rectangle_width,rectangle_height)

	roadTop = Object(True,"grass.jpg",0,0)
	roadTop.scale(roadTop_height,roadTop_width)

	road_Rectangles = []
	x_pos = screen_front
	for i in range(rectangle_number):
		road_bottom = Object(False,road.image,x_pos,0)
		road_top = Object(False,roadTop.image,x_pos,0)
		road_Rectangles.append([road_bottom,road_top])
		x_pos = x_pos + 2

	fuel_objects = []
	for i in range(len(Stages.fuel_array)):
		fuel_y = stage.getYPosition(Stages.fuel_array[i],True) + fuel_offset
		fuel = Object(True,"fuel.png",Stages.fuel_array[i],fuel_y)
		fuel.scale(fuel_height,fuel_width)	
		fuel_objects.append(fuel)



	wheel = Object(True,"wheel.png",0,0)
	wheel.scale(wheel_width,wheel_height)

	rider = Object(True,"obj.png",0,0)
	rider.scale(rider_width,rider_height)

	handle = Object(True,"handle.png",0,0)
	handle.scale(handle_width,handle_height)

	menu_background = Object(True,'menu_background.jpg',0,0)
	menu_background.scale(screen_width,screen_height)

	mixer.music.load("toystory.mp3")
	mixer.music.play()

	done = False
	show_menu = True
	while not done:
		for event in pygame.event.get():   # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True  
			
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					left_key = True
					right_key = False

				elif event.key == pygame.K_RIGHT:
					right_key = True
					left_key = False

				elif event.key == K_ESCAPE:
					done = True

				elif event.key == K_RETURN:
					show_menu = not show_menu  

			elif event.type == pygame.KEYUP:
				right_key = False
				left_key = False

		if(show_menu):
			menu_background.display()
			menu_font = pygame.font.Font(None,80)
			menuText = menu_font.render("PRESS ENTER TO START THE GAME",1,(255,0,0))
			Object.displayScreen.blit(menuText,(200,150))
			pygame.display.flip()
			clock.tick(200)
			continue

		road_y = stage.getYPosition(frameCounter+wheel_offset,False)	
			
		if(wheel_Y_pos - road_y<EEE):
			wheel_vy = 0
			wheel_Y_pos=road_y
			keyEffects1()
		else:
			wheel_vy=wheel_vy - gravity	

		wheel_rotation_angle -= omega
		frameCounter += wheel_vx
		wheel_Y_pos += wheel_vy
		count = 0
		for i in range(0,len(road_Rectangles)):
			road_Rectangles[i][0].horizontalShift(wheel_vx);
			road_Rectangles[i][1].horizontalShift(wheel_vx);
			if(road_Rectangles[i][0].screenX < screen_front): 
				road_Rectangles[i][0].screenX = camera_width - wheel_vx + count*2
				road_Rectangles[i][1].screenX = camera_width - wheel_vx + count*2
				road_Rectangles[i][0].globalX = camera_width + frameCounter - wheel_vx + count*2
				road_Rectangles[i][1].globalX = camera_width + frameCounter - wheel_vx + count*2
				count += 1

		wheel_screen_position = wheel_offset - wheel_width/2;
		wheel_global_y = screen_height- wheel_Y_pos - wheel_height
		wheel.setAllCoordinates(wheel_screen_position,wheel_screen_position+frameCounter,wheel_global_y)

		handle.setAllCoordinates(wheel.screenX-10,wheel.globalX,wheel.globalY-40)
		rider.setAllCoordinates(wheel.screenX-25,wheel.globalX,wheel.globalY-80)
		background.rotateAndDisplay(0)
		rider.display()
		rider.display()
		handle.rotateAndDisplay(249)
		wheel.rotateAndDisplay(wheel_rotation_angle)

		for fuelBox in fuel_objects:
			if( abs(fuelBox.globalX - wheel.globalX) < E and abs(fuelBox.globalY - wheel.globalY) < E ):
				FUEL = 100
				TIME_OVER = 100
				fuel_objects.remove(fuelBox)
		
		for i in range(len(fuel_objects)):
			fuel_Xpos=fuel_objects[i].screenX - wheel_vx
			fuel_Ypos= stage.getYPosition(fuel_objects[i].globalX,True)-fuel_offset
			fuel_objects[i].setAllCoordinates(fuel_Xpos,fuel_objects[i].globalX,fuel_Ypos)
			fuel_objects[i].display()

		fuel_bar_background = pygame.draw.rect(Object.displayScreen, [255,255,255], (400,5,200,20))
		fuel_bar = pygame.draw.rect(Object.displayScreen, [255,0,0], (400,5,FUEL*2,20))

		for road_Rectangle in road_Rectangles:
			yPos = int(stage.getYPosition(road_Rectangle[0].globalX,True))
			road_Rectangle[0].setYCoordinate(yPos)
			road_Rectangle[1].setYCoordinate(yPos)
			road_Rectangle[0].display()
			road_Rectangle[1].display()
		if(FUEL > 0):
			FUEL -= fuelDelta
		
		TIME_OVER -= fuelDelta
		if(TIME_OVER < -fuelDelta*100):
			GAME_OVER = True

		if(wheel_vx >0):
			SCORE += wheel_vx/50
		display_font = pygame.font.Font(None,40)
		scoreText = display_font.render("SCORE : "+str(int(SCORE)),1,(0,0,0))
		Object.displayScreen.blit(scoreText,(5,5))

		fuelText = display_font.render("FUEL : "+str(int(FUEL)) + "%",1,(0,0,0))
		Object.displayScreen.blit(fuelText,(200,5))
		
		escape_font = pygame.font.Font(None,40)
		escapeText = escape_font.render("PRESS ESCAPE TO END THE GAME",1,(255,0,0))
		Object.displayScreen.blit(escapeText,(800,10))
		enterText = escape_font.render("PRESS ENTER TO PAUSE THE GAME",1,(0,0,255))
		Object.displayScreen.blit(enterText,(800,50))

		if(GAME_OVER):
			game_over_font = pygame.font.Font(None,100)
			gameOverText = game_over_font.render("GAME OVER!!!",1,(0,0,0))
			Object.displayScreen.blit(gameOverText,(400,400))
			finalScoreText = game_over_font.render("Your SCORE : "+str(int(SCORE)),1,(0,0,0))
			Object.displayScreen.blit(finalScoreText,(380,500))

		pygame.display.flip()
		clock.tick(200)

	pygame.quit()

run()		
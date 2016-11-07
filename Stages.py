import math


class Stages:
	stageIndex = 0
	screen_height = 0
	fuel_array=[1300,4000,7000,10000,14000,18000]
	def __init__(self,stageNum,screen_height):
		Stages.stageIndex = stageNum
		Stages.screen_height = screen_height

	def getYPosition(self,x,forRender):
		if(Stages.stageIndex == 1):
			return self.stage_1(x,forRender)
		elif(Stages.stageIndex == 2):
			return self.stage_2(x,forRender)
		elif(Stages.stageIndex == 3):
			return self.stage_3(x,forRender)

	def stage_1(self,x,forRender):
		y_val = 0
		offset = 300
		if(x == 0):
		    y_val = offset
		elif(x > 0 and x < 600):
		    y_val = offset
		elif(x>2400 and x<4200):
		    y_val = float(math.tanh(2*3.14*x/1200)*75) + offset-75
		else:
		    y_val = float(math.sin(2*3.14*x/1200)*75) + offset
		if(forRender):
			return float(Stages.screen_height) - y_val
		else:
			return y_val

	def stage_2(self,x,forRender):
		y_val = 0
		offset = 300
		y_val = offset
		if(forRender):
			return float(Stages.screen_height) - y_val
		else:
			return y_val

	def stage_3(self,x,forRender):
		y_val = 0
		offset = 300
		if(x > - 1000 and x < 800):
			y_val = offset
		elif(x >= 800 and x < 1200):
			y_val = offset+0.25*(x-800)
		elif(x >= 1200 and x < 1600):
			y_val = offset+100
		elif(x>=1600 and x <= 2500):
			y_val = offset-100+(x-2000)*(x-2000)/800.0
		elif(x>= 2500 and x <2700):
			y_val = float(math.sin(2*3.14*(x-2500)/400)*75) + offset-100+2500.0/8.0
		elif(x>=2700 and x < 3400):
			y_val = offset-100+(x-3200)*(x-3200)/800.0
		elif(x >= 3400 and x < 3600):
			y_val = float(math.sin(2*3.14*(x-3400)/400)*75) + offset-100+50
		elif(x>=3600 and x < 6000):
			y_val = offset-100+(x-4500)*(x-4500)/(900.0*18.0)
		elif(x>=6000 and x < 7000):
			y_val = offset-100+(15*1500/162.0)
		elif(x >= 7000 and x < 8200):
			y_val = float(math.sin(2*3.14*(x-7000)/400)*75) + offset-100+(15*1500/162.0)
		elif(x>=8200 and x < 12000):
			y_val = offset+(x-10000)*(x-10000)/(1800*1800.0/((15*1500/162.0)-100))
		elif(x>=12000 and x <24000):
			return self.stage_3(x-12000,forRender)
		elif(x >= 24000 and x < 30000):
			return self.stage_1(x-24000,forRender)
		elif(x >= 30000 and x < 40000):
			return self.stage_2(x-30000,forRender)
		elif(x >= 40000 and x < 50000):
			return self.stage_3(x-40000,forRender)
		elif(x >= 50000 and x < 55000):
			return self.stage_1(x-50000,forRender)
		elif(x >= 55000 and x < 65000):
			return self.stage_1(x-55000,forRender)
		elif(x >= 65000 and x < 85000):
			return self.stage_3(x-65000,forRender)
		elif(x >= 85000 and x < 90000):
			return self.stage_2(x-85000,forRender)
		elif(x >= 90000 and x < 120000):
			return self.stage_1(x-90000,forRender)


		if(forRender):
			return float(Stages.screen_height) - y_val
		else:
			return y_val

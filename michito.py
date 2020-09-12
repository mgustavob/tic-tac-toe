

import random, time, pygame, sys
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
pynk = (255, 213, 213)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

x_pos = 0
y_pos = 0
player = 1
number = 0
valid = 0
random_pos = 0
count = 0
position = ''
location = ''
all_x = {}
all_o = {}
semicolon = []
free_pos = []

all_sounds = ['beeparca.wav', 'beepspri.wav', 'applause3.wav', 'beeplaug.wav']
all_pos = {'a1':'100;150', 'a2':'200;150', 'a3':'300;150', 'b1':'100;250', 'b2':'200;250', 'b3':'300;250', 'c1':'100;350', 'c2':'200;350', 'c3':'300;350'}
all_free_pos = all_pos
all_solutions = [['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'], ['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'], ['a1','b2','c3'], ['a3','b2','c1']]
all_solut_pos = [[100,200,400,200],[100,300,400,300],[100,400,400,400],[150,150,150,450],[250,150,250,450],[350,150,350,450],[100,150,400,450],[100,450,400,150]]
all_results = ['The Machine Won', 'You Won', 'Nobody Won']


# start exit function
def exit(number):
	pygame.display.flip()
	if number == 0:
		pygame.quit()
		sys.exit(0)
	if number == 1:
		pygame.mixer.music.load(all_sounds[3])
		pygame.mixer.music.play()
	if number == 2:
		pygame.mixer.music.load(all_sounds[2])
		pygame.mixer.music.play()
	time.sleep(4)
	pygame.quit()
	sys.exit(0)

# start main function
def main():
	pygame.init()
	pygame.mixer.init()
	sysfont = pygame.font.get_default_font()
	size = width, height = 500, 500
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption('My first Tic Tac Toe')
	player = 1

	# start main loop
	while True:

		time.sleep(1)

		# draw screen and an empty tic tac toe
		screen.fill(pynk)
		pygame.draw.line(screen, black, (100, 250), (400, 250), 10)
		pygame.draw.line(screen, black, (100, 350), (400, 350), 10)
		pygame.draw.line(screen, black, (200, 150), (200, 450), 10)
		pygame.draw.line(screen, black, (300, 150), (300, 450), 10)
	
		# draw all the x's	
		px = ''
		for p, u in all_x.items():
			semicolon = u.split(';')
			x_pos = int(semicolon[0])
			y_pos = int(semicolon[1])
			pygame.draw.line(screen, black, (x_pos+25, y_pos+15), (x_pos+75, y_pos+85), 15)
			pygame.draw.line(screen, black, (x_pos+25, y_pos+85), (x_pos+75, y_pos+15), 15)
			px = px + p
		
		# draw all the o's
		po = ''
		for p, u in all_o.items():
			semicolon = u.split(';')
			x_pos = int(semicolon[0])
			y_pos = int(semicolon[1])
			pygame.draw.circle(screen, black, (x_pos+50, y_pos+50), 38, 12)
			po = po + p
		
		# change buffers
		pygame.display.flip()

		count = 0
		for ix in all_solutions:
			if (ix[0] in px) and (ix[1] in px) and (ix[2] in px):
				pygame.draw.line(screen, red, (all_solut_pos[count][0], all_solut_pos[count][1]), (all_solut_pos[count][2], all_solut_pos[count][3]), 15)
				screen.blit(pygame.font.SysFont(sysfont, 25).render(all_results[0], True, blue), (20, 470))
				exit(1)
			count += 1

		count = 0
		for io in all_solutions:
			if (io[0] in po) and (io[1] in po) and (io[2] in po):
				pygame.draw.line(screen, red, (all_solut_pos[count][0], all_solut_pos[count][1]), (all_solut_pos[count][2], all_solut_pos[count][3]), 15)
				screen.blit(pygame.font.SysFont(sysfont, 25).render(all_results[1], True, blue), (20, 470))
				exit(2)
			count += 1

		# no alternatives left
		if all_free_pos == {}:
			screen.blit(pygame.font.SysFont(sysfont, 30).render(all_results[2], True, blue), (20, 470))
			exit(3)

		if player == 1:
			# player 1's turn
			free_pos = []
			location = ''
			for p, u in all_free_pos.items():
				free_pos.append(p)
			random_pos = random.choice(free_pos)
			location = all_free_pos.pop(random_pos)
			semicolon = location.split(';')
			x_pos = int(semicolon[0])
			y_pos = int(semicolon[1])
			pygame.draw.line(screen, red, (x_pos+25, y_pos+15), (x_pos+75, y_pos+85), 15)
			pygame.draw.line(screen, red, (x_pos+25, y_pos+85), (x_pos+75, y_pos+15), 15)
			all_x[random_pos] = location
			player = 2
		elif player == 2:
			# player 2's turn
			valid = 0
			while valid == 0:
				for event in pygame.event.get():
					
					# when press the mouse button
					if event.type == pygame.MOUSEBUTTONDOWN:
						mouse_pos = pygame.mouse.get_pos()

						# left mouse button
						if event.button == 1:
							position = ''
							for p,u in all_free_pos.items():
								semicolon = u.split(';')
								x_pos = int(semicolon[0])
								y_pos = int(semicolon[1])
								if mouse_pos[0] in list(range(x_pos, x_pos+100)) and mouse_pos[1] in list(range(y_pos, y_pos+100)):
									pygame.draw.circle(screen, red, (x_pos+50, y_pos+50), 38, 12)
									all_o[p] = u
									position = p
									player = 1
									valid = 1
							if valid == 1:
								all_free_pos.pop(position)
								pygame.mixer.music.load(all_sounds[0])
								pygame.mixer.music.play()
							else:
								pygame.mixer.music.load(all_sounds[1])
								pygame.mixer.music.play()

						# right mouse button
						if event.button == 3:
							salida(0)

					# window's exit symbol
					if event.type == QUIT:
						exit(0)
					
					# esc key
					if event.type == KEYDOWN:
						if event.key == K_ESCAPE:
							exit(0)
						else:
							pygame.mixer.music.load(all_sounds[1])
							pygame.mixer.music.play()

		# change buffers
		pygame.display.flip()
	
if __name__ == '__main__':
   main()

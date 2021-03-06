import time
import pygame
import sys
import os
import random
from picamera import PiCamera
from PIL import Image

pics = '/home/pi/PokedexV2/pics/'
pokePics = '/home/pi/PokedexV2/pics/pokemons/'
black = (0,0,0)
white = (255,255,255)
pygame.init()
screen = pygame.display.set_mode((800,480), pygame.FULLSCREEN)
cam = PiCamera()

def startScreen():
	screen.fill(black)
	startScreen = pics+'start-screen.png'
	startScreenPNG = pygame.image.load(startScreen).convert_alpha()
	screen.blit(startScreenPNG, (0,0))
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				mainMenu()
def WIP():
        myfont = pygame.font.SysFont("monospace", 45)
        WIP = myfont.render("WORK IN PROGRESS", 1, black)
        screen.blit(WIP, (400, 210))
        pygame.display.update()

def mainMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	start = pics+'start.png'
	startPNG = pygame.image.load(start).convert_alpha()
	credit = pics+'credits.png'
	creditPNG = pygame.image.load(credit).convert_alpha()
	exit = pics+'exit.png'
	exitPNG = pygame.image.load(exit).convert_alpha()
	#Rect some stuff
	startPos = pygame.Rect(60, 125, 268, 71)
	creditPos = pygame.Rect(60, 246, 268, 71)
	exitPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(startPNG, startPos)
	screen.blit(creditPNG, creditPos)	#image size 268x71 so add 121
	screen.blit(exitPNG, exitPos)
	#display
	pygame.display.update()
	#move Rects
	startPos = startPNG.get_rect()
	startPos = startPos.move(60, 125)
	creditPos = creditPNG.get_rect()
	creditPos = creditPos.move(60, 246)
	exitPos = exitPNG.get_rect()
	exitPos = exitPos.move (60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				#print mouse_pos
				if startPos.collidepoint(mouse_pos):
					startMenu()
				if creditPos.collidepoint(mouse_pos):
					credits()
				if exitPos.collidepoint(mouse_pos):
					exitMenu()

def startMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	pokedex = pics+'Pokedex.png'
	pokedexPNG = pygame.image.load(pokedex).convert_alpha()
	camera = pics+'camera.png'
	cameraPNG = pygame.image.load(camera).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	pokedexPos = pygame.Rect(60, 125, 268, 71)
	cameraPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(pokedexPNG, pokedexPos)
	screen.blit(cameraPNG, cameraPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	pokedexPos = pokedexPNG.get_rect()
	pokedexPos = pokedexPos.move(60, 125)
	cameraPos = cameraPNG.get_rect()
	cameraPos = cameraPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				if pokedexPos.collidepoint(mouse_pos):
					pokedexMenu()
				if cameraPos.collidepoint(mouse_pos):
					cameraMenu()
				if backPos.collidepoint(mouse_pos):
					mainMenu()

def exitMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background)
	exit = pics+'exit.png'
	exitPNG = pygame.image.load(exit).convert_alpha()
	shutdown = pics+'shutdown.png'
	shutdownPNG = pygame.image.load(shutdown).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	exitPos = pygame.Rect(60, 125, 268, 71)
        shutdownPos = pygame.Rect(60, 246, 268, 71)
        backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(exitPNG, exitPos)
	screen.blit(shutdownPNG, shutdownPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	exitPos = exitPNG.get_rect()
	exitPos = exitPos.move(60, 125)
	shutdownPos = shutdownPNG.get_rect()
	shutdownPos = shutdownPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
				if exitPos.collidepoint(mouse_pos):
					sys.exit()
				if shutdownPos.collidepoint(mouse_pos):
					os.system('shutdown now')
				if backPos.collidepoint(mouse_pos):
					mainMenu()
					
def pokedexMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	database = pics+'database.png'
	databasePNG = pygame.image.load(database).convert_alpha()
	search = pics+'search.png'
	searchPNG = pygame.image.load(search).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	databasePos = pygame.Rect(60, 125, 268, 71)
	searchPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG, (0,0))
	screen.blit(databasePNG, databasePos)
	screen.blit(searchPNG, searchPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	databasePos = databasePNG.get_rect()
	databasePos = databasePos.move(60, 125)
	searchPos = searchPNG.get_rect()
	searchPos = searchPos.move(60, 246)
	backPos = backPNG.get_rect()
	backPos = backPos.move(60, 367)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = event.pos
				if databasePos.collidepoint(mouse_pos):
					databaseMenu()
				if searchPos.collidepoint(mouse_pos):
					searchMenu()
				if backPos.collidepoint(mouse_pos):
					startMenu()

def databaseMenu():
	screen.fill(black)
	#define pics
	background = pics+'background.png'
	backgroundPNG = pygame.image.load(background).convert_alpha()
	up = pics+'next.png'
	upPNG = pygame.image.load(up).convert_alpha()
	down = pics+'previous.png'
	downPNG = pygame.image.load(down).convert_alpha()
	back = pics+'back.png'
	backPNG = pygame.image.load(back).convert_alpha()
	#Rect some stuff
	upPos = pygame.Rect(60, 125, 268, 71)
	downPos = pygame.Rect(60, 246, 268, 71)
	backPos = pygame.Rect(60, 367, 268, 71)
	#blit images
	screen.blit(backgroundPNG,(0,0))
	screen.blit(upPNG, upPos)
	screen.blit(downPNG, downPos)
	screen.blit(backPNG, backPos)
	#display
	pygame.display.update()
	#move Rects
	upPos = upPNG.get_rect()
        upPos = upPos.move(60, 125)
        downPos = downPNG.get_rect()
        downPos = downPos.move(60, 246)
        backPos = backPNG.get_rect()
        backPos = backPos.move (60, 367)
	pokeNum = 1
	pokeMax = 251	#Maximum pokemon number
	pokePos = (420,115)
	#pokemon no.1
	pokemon = pokePics+'001.png'
	pokemonPNG = pygame.image.load(pokemon).convert_alpha()
	pokemonPNG = pygame.transform.scale(pokemonPNG, (380,380))
	#display number
	pygame.font.init()
	myfont = pygame.font.SysFont("monospace", 45)
	pokeName = myfont.render("bulbasaur", 1, black)
	pokeID = myfont.render("001", 1, black)
	#blit stuff
	screen.blit(pokemonPNG, pokePos)
	screen.blit(pokeName, (400, 75))
	screen.blit(pokeID, (400, 420))
	pygame.display.update()
	while True:
		pygame.draw.rect(screen,white,(400, 75, 800, 480))
		#pygame.display.update()
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
				#-----------------------------------
                                if upPos.collidepoint(mouse_pos):
					pokeNum = pokeNum+1
					if pokeNum > pokeMax:
						pokeNum = 1
					pokeStr = str(pokeNum)
					pokeLength = len(pokeStr)
					if pokeLength == 1:
						pokeStr = "00" + pokeStr
					if pokeLength == 2:
						pokeStr = "0" + pokeStr
					print pokeStr
					#print pokeNum
					pokeFile = open('/home/pi/PokedexV2/code/pokemon.csv','r')
					pokeName = pokeFile.readlines()[pokeNum]
					id,name = pokeName.split(",")
					name = name[:-2]
					#define pics
					pokemon = pokePics+pokeStr+'.png'
        				pokemonPNG = pygame.image.load(pokemon).convert_alpha()
        				pokemonPNG = pygame.transform.scale(pokemonPNG, (380,380))
        				#display number
        				pygame.font.init()
        				myfont = pygame.font.SysFont("monospace", 45)
        				pokeID = myfont.render(pokeStr, 1, black)
					pokeName = myfont.render(name, 1, black)
        				#blit stuff
					screen.blit(pokemonPNG, pokePos)
        				screen.blit(pokeID, (400, 420))
					screen.blit(pokeName, (400, 75))
        				pygame.display.update()
					pokeFile.close()
				#-------------------------------------
                                if downPos.collidepoint(mouse_pos):
                                        pokeNum = pokeNum-1
					if pokeNum ==0:
						pokeNum = pokeMax
					pokeStr = str(pokeNum)
                                        pokeLength = len(pokeStr)
                                        if pokeLength == 1:
                                                pokeStr = "00" + pokeStr
                                        if pokeLength == 2:
                                                pokeStr = "0" + pokeStr
                                        print pokeStr
					#print pokeNum
					pokeFile = open('/home/pi/PokedexV2/code/pokemon.csv')
                                        pokeName = pokeFile.readlines()[pokeNum]
                                        id,name = pokeName.split(",")
                                        name = name[:-2]
                                        #define pics
                                        pokemon = pokePics+pokeStr+'.png'
                                        pokemonPNG = pygame.image.load(pokemon).convert_alpha()
                                        pokemonPNG = pygame.transform.scale(pokemonPNG, (380, 380))
                                        #display number
                                        pygame.font.init()
                                        myfont = pygame.font.SysFont("monospace", 45)
                                        pokeID = myfont.render(pokeStr, 1, black)
                                        pokeName = myfont.render(name, 1, black)
                                        #blit stuff
					screen.blit(pokemonPNG, pokePos)
                                        screen.blit(pokeID, (400, 420))
                                        screen.blit(pokeName, (400, 75))
                                        pygame.display.update()
                                        pokeFile.close()
				#----------------------------------------
                                if backPos.collidepoint(mouse_pos):
                                        pokedexMenu()

def searchMenu():
	WIP()

def credits():
	WIP()

def cameraMenu():
	screen.fill(black)
        #define pics
        background = pics+'background.png'
        backgroundPNG = pygame.image.load(background).convert_alpha()
        capture = pics+'capture.png'
        capturePNG = pygame.image.load(capture).convert_alpha()
        test = pics+'test.png'
        testPNG = pygame.image.load(test).convert_alpha()
        back = pics+'back.png'
        backPNG = pygame.image.load(back).convert_alpha()
        #Rect some stuff
        capturePos = pygame.Rect(60, 125, 268, 71)
        testPos = pygame.Rect(60, 246, 268, 71)
        backPos = pygame.Rect(60, 367, 268, 71)
        #blit images
        screen.blit(backgroundPNG, (0,0))
        screen.blit(capturePNG, capturePos)
        screen.blit(testPNG, testPos)
        screen.blit(backPNG, backPos)
        #display
        pygame.display.update()
        #move Rects
        capturePos = capturePNG.get_rect()
        capturePos = capturePos.move(60, 125)
        testPos = testPNG.get_rect()
        testPos = testPos.move(60, 246)
        backPos = backPNG.get_rect()
        backPos = backPos.move(60, 367)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if capturePos.collidepoint(mouse_pos):
                                        cameraCapture()
                                if testPos.collidepoint(mouse_pos):
                                        cameraTest()
                                if backPos.collidepoint(mouse_pos):
                                        startMenu()

def cameraCapture():
	cam.resolution = (800, 480)
	cam.start_preview()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				cam.capture('/home/pi/PokedexV2/pics/camera/background.png')
				cam.stop_preview()
				cameraMenu2()

def cameraMenu2():
        screen.fill(black)
        #define pics
        background = pics+'background.png'
        backgroundPNG = pygame.image.load(background).convert_alpha()
        cont = pics+'continue.png'
        contPNG = pygame.image.load(cont).convert_alpha()
        preview = pics+'preview.png'
        previewPNG = pygame.image.load(preview).convert_alpha()
        discard = pics+'discard.png'
        discardPNG = pygame.image.load(discard).convert_alpha()
        #Rect some stuff
        contPos = pygame.Rect(60, 125, 268, 71)
        previewPos = pygame.Rect(60, 246, 268, 71)
        discardPos = pygame.Rect(60, 367, 268, 71)
        #blit images
        screen.blit(backgroundPNG, (0,0))
        screen.blit(contPNG, contPos)
        screen.blit(previewPNG, previewPos)
        screen.blit(discardPNG, discardPos)
        #display
        pygame.display.update()
        #move Rects
        contPos = contPNG.get_rect()
        contPos = contPos.move(60, 125)
        previewPos = previewPNG.get_rect()
        previewPos = previewPos.move(60, 246)
        discardPos = discardPNG.get_rect()
        discardPos = discardPos.move(60, 367)
        while True:
                for event in pygame.event.get():
			if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if contPos.collidepoint(mouse_pos):
                                        cameraMenu3simple()
                                if previewPos.collidepoint(mouse_pos):
                                        screen.fill(black)
					picture = '/home/pi/PokedexV2/pics/camera/background.png'
					picturePNG = pygame.image.load(picture).convert_alpha()
					screen.blit(picturePNG, (0,0))
					pygame.display.update()
					while True:
						for event in pygame.event.get():
							if event.type == pygame.MOUSEBUTTONDOWN:
								cameraMenu2()
                                if discardPos.collidepoint(mouse_pos):
					os.remove('/home/pi/PokedexV2/pics/camera/background.png')
					#print('deleted')
					cameraMenu()

def cameraMenu3simple():
	screen.fill(black)
        #define pics
        background = pics+'background.png'
        backgroundPNG = pygame.image.load(background).convert_alpha()
        poke1 = pics+'pokemon1.png'
        poke1PNG = pygame.image.load(poke1).convert_alpha()
        poke2 = pics+'pokemon2.png'
        poke2PNG = pygame.image.load(poke2).convert_alpha()
        poke3 = pics+'pokemon3.png'
        poke3PNG = pygame.image.load(poke3).convert_alpha()
        #Rect some stuff
        poke1Pos = pygame.Rect(60, 125, 268, 71)
        poke2Pos = pygame.Rect(60, 246, 268, 71)
        poke3Pos = pygame.Rect(60, 367, 268, 71)
        #blit images
        screen.blit(backgroundPNG, (0,0))
        screen.blit(poke1PNG, poke1Pos)
        screen.blit(poke2PNG, poke2Pos)
        screen.blit(poke3PNG, poke3Pos)
        #display
        pygame.display.update()
        #move Rects
        poke1Pos = poke1PNG.get_rect()
        poke1Pos = poke1Pos.move(60, 125)
        poke2Pos = poke2PNG.get_rect()
        poke2Pos = poke2Pos.move(60, 246)
        poke3Pos = poke3PNG.get_rect()
        poke3Pos = poke3Pos.move(60, 367)
	while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if poke1Pos.collidepoint(mouse_pos):
					screen.fill(black)
					myfont = pygame.font.SysFont("monospace", 150)
					loading = myfont.render("Loading...", 1, white)
					screen.blit(loading, (0, 190))
					pygame.display.update()
					#---------------------------
                                        imbg = Image.open('/home/pi/PokedexV2/pics/camera/background.png')
					imfg = Image.open('/home/pi/PokedexV2/pics/pokemons/025.png')
					imfg = imfg.resize((200, 200))
					new_im = Image.new('RGBA', (800,480))
					new_im.paste(imfg,(400,240))
					imbg.paste(new_im, None, new_im)
					imbg.save('/home/pi/PokedexV2/pics/camera/final.png', 'png')
					#---------------------------
					cameraMenu4()
                                if poke2Pos.collidepoint(mouse_pos):
                                        screen.fill(black)
                                        myfont = pygame.font.SysFont("monospace", 150)
                                        loading = myfont.render("Loading...", 1, white)
                                        screen.blit(loading, (0, 190))
                                        pygame.display.update()
                                        #---------------------------
                                        imbg = Image.open('/home/pi/PokedexV2/pics/camera/background.png')
                                        imfg = Image.open('/home/pi/PokedexV2/pics/pokemons/054.png')
                                        imfg = imfg.resize((200, 200))
                                        new_im = Image.new('RGBA', (800,480))
                                        new_im.paste(imfg,(400,240))
                                        imbg.paste(new_im, None, new_im)
                                        imbg.save('/home/pi/PokedexV2/pics/camera/final.png', 'png')
                                        #---------------------------
                                        cameraMenu4()
                                if poke3Pos.collidepoint(mouse_pos):
                                        screen.fill(black)
                                        myfont = pygame.font.SysFont("monospace", 150)
                                        loading = myfont.render("Loading...", 1, white)
                                        screen.blit(loading, (0, 190))
                                        pygame.display.update()
                                        #---------------------------
					pokePath = '/home/pi/PokedexV2/pics/pokemons/' + str(random.randint(001,251)) + '.png'
                                        imbg = Image.open('/home/pi/PokedexV2/pics/camera/background.png')
                                        imfg = Image.open(pokePath)
                                        imfg = imfg.resize((200, 200))
                                        new_im = Image.new('RGBA', (800,480))
                                        new_im.paste(imfg,(400,240))
                                        imbg.paste(new_im, None, new_im)
                                        imbg.save('/home/pi/PokedexV2/pics/camera/final.png', 'png')
                                        #---------------------------
                                        cameraMenu4()

def cameraMenu4():
	screen.fill(black)
        #define pics
        background = pics+'background.png'
        backgroundPNG = pygame.image.load(background).convert_alpha()
        preview = pics+'preview.png'
        previewPNG = pygame.image.load(preview).convert_alpha()
        share = pics+'share.png'
        sharePNG = pygame.image.load(share).convert_alpha()
        discard = pics+'discard.png'
        discardPNG = pygame.image.load(discard).convert_alpha()
        #Rect some stuff
        previewPos = pygame.Rect(60, 125, 268, 71)
        sharePos = pygame.Rect(60, 246, 268, 71)
        discardPos = pygame.Rect(60, 367, 268, 71)
        #blit images
        screen.blit(backgroundPNG, (0,0))
        screen.blit(previewPNG, previewPos)
        screen.blit(sharePNG, sharePos)
        screen.blit(discardPNG, discardPos)
        #display
        pygame.display.update()
	#move Rects
        previewPos = previewPNG.get_rect()
        previewPos = previewPos.move(60, 125)
        sharePos = sharePNG.get_rect()
        sharePos = sharePos.move(60, 246)
        discardPos = discardPNG.get_rect()
        discardPos = discardPos.move(60, 367)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse_pos = event.pos
                                if previewPos.collidepoint(mouse_pos):
                                        screen.fill(black)
                                        picture = '/home/pi/PokedexV2/pics/camera/final.png'
                                        picturePNG = pygame.image.load(picture).convert_alpha()
                                        screen.blit(picturePNG, (0,0))
                                        pygame.display.update()
                                        while True:
						for event in pygame.event.get():
							if event.type == pygame.MOUSEBUTTONDOWN:
								cameraMenu4()
                                if sharePos.collidepoint(mouse_pos):
                                        WIP()
                                if discardPos.collidepoint(mouse_pos):
                                        os.remove('/home/pi/PokedexV2/pics/camera/background.png')
					os.remove('/home/pi/PokedexV2/pics/camera/final.png')
					cameraMenu()

def cameraTest():
	cam.resolution = (800, 480)
	cam.start_preview()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				cam.stop_preview()
				cameraMenu()

startScreen()

'''
import pygame
from pygame.locals import *
from pygame import mixer
'''
import subprocess

p = subprocess.call(["afplay", "TitleScreen.mp3"])
p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)

p.terminate()

p = subprocess.call(["afplay", "Bsttle.mp3"])

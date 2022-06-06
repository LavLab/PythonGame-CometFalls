import pygame

from cls_Level import cls_Level
from random import randint
import os

class cls_Enemy(pygame.sprite.Sprite):
    def __init__(self, pGame, pLevel):
        super().__init__()
        self.Game = pGame
        self.Level = pLevel
        
        self.LoadStatistics()
        self.LoadImages()
        self.Spawn()
        
    def LoadStatistics(self):
        self.c_Name = self.Level.c_Enemies["NAME"]
        self.c_Speed = self.Level.c_Enemies["STATS"]["SPEED"]
        self.c_Max_Health = self.Level.c_Enemies["STATS"]["MAX_HEALTH"]
        
    def Spawn(self):        
        self.image = self.images["IDLE"][0]
        self.rect = self.image.get_rect()
        
        # Point de Spawn
        self.rect.x = randint(self.Level.c_Map["SPAWNS"]["ENEMIES"]["X"][0],self.Level.c_Map["SPAWNS"]["ENEMIES"]["X"][1])
        self.rect.y = randint(self.Level.c_Map["SPAWNS"]["ENEMIES"]["Y"][0],self.Level.c_Map["SPAWNS"]["ENEMIES"]["Y"][1])
                
        self.c_Health = self.c_Max_Health
        
    def LoadImages(self):
        self.images={}
        self.images["IDLE"]=[]
        for file in os.listdir("assets\\ENEMIES\\"+self.c_Name+"\\IDLE"):
            if file.endswith(".png"):
                self.images["IDLE"].append(pygame.image.load("assets\\ENEMIES\\"+self.c_Name+"\\IDLE\\"+file)) 
                    
        self.images["WALK"]=[]
        for file in os.listdir("assets\\ENEMIES\\"+self.c_Name+"\\WALK"):
            if file.endswith(".png"):
                self.images["WALK"].append(pygame.image.load("assets\\ENEMIES\\"+self.c_Name+"\\WALK\\"+file))
                        
        self.images["ATTACK"]=[]       
        for file in os.listdir("assets\\ENEMIES\\"+self.c_Name+"\\ATTACK"):
            if file.endswith(".png"):
                self.images["ATTACK"].append(pygame.image.load("assets\\ENEMIES\\"+self.c_Name+"\\ATTACK\\"+file))
                
    # Deplacement vers GAUCHE 
    def Move(self):
        if self.rect.x > self.Level.c_Map["LIMITS"]["X"][0]:
            self.rect.x -= self.c_Speed
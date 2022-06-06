import pygame

from cls_Level import cls_Level
from random import randint
import os

class cls_Player(pygame.sprite.Sprite):
    def __init__(self, pGame, pLevel):
        super().__init__()
        self.Game = pGame
        self.Level = pLevel
        
        self.LoadStatistics()
        self.LoadImages()
        self.Spawn()
        
    def LoadStatistics(self):
        self.c_Name = self.Level.c_Players["NAME"]
        self.c_Speed = self.Level.c_Players["STATS"]["SPEED"]
        self.c_Max_Health = self.Level.c_Players["STATS"]["MAX_HEALTH"]
        self.c_Max_Energy = self.Level.c_Players["STATS"]["MAX_ENERGY"]
        
    def LoadImages(self):
        self.images={}
        self.images["IDLE"]=[]
        for file in os.listdir("assets\\PLAYERS\\"+self.c_Name+"\\IDLE"):
            if file.endswith(".png"):
                self.images["IDLE"].append(pygame.image.load("assets\\PLAYERS\\"+self.c_Name+"\\IDLE\\"+file)) 
                    
        self.images["WALK"]=[]
        for file in os.listdir("assets\\PLAYERS\\"+self.c_Name+"\\WALK"):
            if file.endswith(".png"):
                self.images["WALK"].append(pygame.image.load("assets\\PLAYERS\\"+self.c_Name+"\\WALK\\"+file))
                        
        self.images["ATTACK"]=[]       
        for file in os.listdir("assets\\PLAYERS\\"+self.c_Name+"\\ATTACK"):
            if file.endswith(".png"):
                self.images["ATTACK"].append(pygame.image.load("assets\\PLAYERS\\"+self.c_Name+"\\ATTACK\\"+file))
        
    def Spawn(self):        
        self.image = self.images["IDLE"][0]
        self.rect = self.image.get_rect()
        
        # Point de Spawn
        self.rect.x = randint(self.Level.c_Map["SPAWNS"]["PLAYERS"]["X"][0],self.Level.c_Map["SPAWNS"]["PLAYERS"]["X"][1])
        self.rect.y = randint(self.Level.c_Map["SPAWNS"]["PLAYERS"]["Y"][0],self.Level.c_Map["SPAWNS"]["PLAYERS"]["Y"][1])
                
        self.c_Health = self.c_Max_Health
        self.c_Energy = self.c_Max_Energy
            
        
        # Deplacement vers DROITE 
    def Move_Right(self):
        if self.rect.x + self.rect.width < self.Level.c_Map["LIMITS"]["X"][1]:
            self.rect.x += self.c_Speed 
        
        # Deplacement vers GAUCHE 
    def Move_Left(self):
        if self.rect.x > self.Level.c_Map["LIMITS"]["X"][0]:
            self.rect.x -= self.c_Speed
        
        # Deplacement vers HAUT 
    def Move_Top(self):
        if  self.rect.y > self.Level.c_Map["LIMITS"]["Y"][0]:
            self.rect.y -= self.c_Speed
        
        # Deplacement vers BAS 
    def Move_Bot(self):
        if self.rect.y + self.rect.height < self.Level.c_Map["LIMITS"]["Y"][1]:
            self.rect.y += self.c_Speed
import pygame

from cls_Level import cls_Level
from random import randint
import os

class cls_Capacity(pygame.sprite.Sprite):
    def __init__(self, pGame, pLevel):
        super().__init__()
        self.Game = pGame
        self.Level = pLevel
        
        self.LoadStatistics()
        self.LoadImages()
        self.Spawn()
        
    def LoadStatistics(self):
        self.c_Name = self.Level.c_Capacities["NAME"]
        self.c_Speed = self.Level.c_Capacities["STATS"]["SPEED"]
        self.c_Max_Health = self.Level.c_Capacities["STATS"]["MAX_HEALTH"]
        self.c_Max_Energy = self.Level.c_Capacities["STATS"]["MAX_ENERGY"]
        
    def LoadImages(self):
        self.images=[]
        self.images.append(pygame.image.load("assets\\CAPACITIES\\"+self.c_Name+"\\capa.png"))
        
    def Spawn(self):        
        self.image = self.images[0]
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
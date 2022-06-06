import pygame
import json

class cls_Level(pygame.sprite.Sprite):
    def __init__(self, pGame, pGameLevel):
        super().__init__()
        self.Game = pGame
        self.c_Level = pGameLevel        
        self.LoadJSON()          
            
    def LoadJSON(self):
        self.JSON={}
        with open('tresor.json') as json_file:
            JSON = json.load(json_file)
            LEVEL = JSON["LEVELS_EDIT"][self.c_Level]
            
            self.c_Map = JSON["MAPS"][LEVEL["MAP"]]
            
            self.c_Players={}
            self.c_Players["NAME"] = JSON["PLAYERS"][LEVEL["PLAYER"]]["NAME"]
            self.c_Players["STATS"] = JSON["PLAYERS"][LEVEL["PLAYER"]]["LEVELS"][self.c_Level]
                
            self.c_Capacities={}
            for Capacity in LEVEL["CAPACITIES"]:
                self.c_Capacities["NAME"] = JSON["CAPACITIES"][Capacity]["NAME"]
                self.c_Capacities["STATS"] = JSON["CAPACITIES"][Capacity]["LEVELS"][self.c_Level]
            
            self.c_Enemies={}        
            for Enemy in LEVEL["ENEMIES"]:
                self.c_Enemies["COUNT"] = LEVEL["ENEMIES_COUNT"]
                self.c_Enemies["NAME"] = JSON["ENEMIES"][Enemy]["NAME"]
                self.c_Enemies["STATS"] = JSON["ENEMIES"][Enemy]["LEVELS"][self.c_Level]
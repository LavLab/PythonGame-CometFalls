from cls_Enemy import cls_Enemy
import pygame

from cls_Level import cls_Level
from cls_Player import cls_Player

class cls_Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.c_StateRunning = True
        self.c_StateBreak = False
        self.c_StateLose = False
          
        self.c_ScreenLayer = []
        self.c_PressedKeys={}
        self.GameLevel = 0
        
        self.LoadScreenLayer()      
        self.LoadLevel()                     
        self.LoadPlayers()
        self.LoadEnemies()
        
    def LoadScreenLayer(self):        
        # Ordre des Calques (NOM, VISIBILITE EN PAUSE, VISIBILITE EN PERDU)
        self.c_ScreenLayer.append(("BACKGROUND",True,True))
        self.c_ScreenLayer.append(("PLAYERS",True,True))
        self.c_ScreenLayer.append(("ENEMIES",True,True))

    def ScreenLayer(self, pGameScreen):
        self.ScreenArea = pGameScreen.get_rect()
        # Les Calques
        for Layer in self.c_ScreenLayer:
            # Si le calques visible en pause et perdu
            if Layer[1] == self.c_StateBreak or Layer[1] :
                if Layer[2] == self.c_StateLose or Layer[2]:
                    if Layer[0] == 'BACKGROUND':
                        Background = pygame.image.load("assets\MAPS\\"+self.c_Level.c_Map["NAME"]+"\\Background.png")
                        Background = pygame.transform.smoothscale(Background, pygame.display.get_surface().get_size())
                        pGameScreen.blit(Background, (0,0))
                    if Layer[0] == 'PLAYERS':
                        self.all_Players.draw(pGameScreen)
                    if Layer[0] == 'ENEMIES':
                        self.all_Enemies.draw(pGameScreen)
         
    # Ecran perdu 
    def GameLose(self, pGameScreen):
        if self.c_StateLose:
            # Surface
            Surface = pygame.Surface((pGameScreen.get_width(),pGameScreen.get_height()))
            Surface.set_alpha(128)
            Surface.fill((0,0,0))
            pGameScreen.blit(Surface, (0,0))
            # Texte
            myfont = pygame.font.SysFont(None, 40, 15)
            label = myfont.render("- PERDU -", 1, (255,255,255))
            text_rect = label.get_rect(center=(pGameScreen.get_width()/2, pGameScreen.get_height()/2 - 200))
            pGameScreen.blit(label, text_rect)
    
    # Ecran pause  
    def GamePause(self, pGameScreen):
        if self.c_StateBreak:
            # Surface
            Surface = pygame.Surface((pGameScreen.get_width(),pGameScreen.get_height()))
            Surface.set_alpha(128)
            Surface.fill((0,0,0))
            pGameScreen.blit(Surface, (0,0))
            # Texte
            myfont = pygame.font.SysFont(None, 40, 15)
            label = myfont.render("- PAUSE -", 1, (255,255,255))
            text_rect = label.get_rect(center=(pGameScreen.get_width()/2, pGameScreen.get_height()/2 - 200))
            pGameScreen.blit(label, text_rect)
        
    # -- LEVEL --
    def LoadLevel(self):
        self.c_Level = cls_Level(self,self.GameLevel)
        
    # -- PLAYER --
    def LoadPlayers(self):
        self.all_Players = pygame.sprite.Group()
        self.SpawnPlayer()
        
    def SpawnPlayer(self):
        aPlayer = cls_Player(self,self.c_Level)
        self.all_Players.add(aPlayer)
        
    # -- ENEMY --
    def LoadEnemies(self):
        self.all_Enemies = pygame.sprite.Group()
        for i in range(0,self.c_Level.c_Enemies["COUNT"]):
            timer=0
            while timer < self.c_Level.c_Enemies["STATS"]["ENEMIES_SPAWN_TIME"] :
                self.SpawnEnemy()
                break
        
    def SpawnEnemy(self):
        aEnemy = cls_Enemy(self,self.c_Level)
        self.all_Enemies.add(aEnemy)
        
    # COLISION
    def Check_Colision(self, pSprite, pGroup):
        return pygame.sprite.pygame.sprite.spritecollide(pSprite, pGroup, False, pygame.sprite.collide_mask)
    
    # DOMMAGE
    def Damage_Distribution(self,pTabOBJECT):
        # pTabOBJECT[0] : Object attaquant
        # pTabOBJECT[1] : Object cible
        
        # Si la VIE - les Dommages >= 0
        if pTabOBJECT[1].c_Health - pTabOBJECT[0].c_Damage >= 0:
            # Soustraction des dommages
            pTabOBJECT[1].c_Health -= pTabOBJECT[0].c_Damage
            print(pTabOBJECT[1].c_Health)
        else:            
            # Si Entity Tué et Perdu
            if type(pTabOBJECT[1]) is cls_Entity:
                self.c_StateLose = True
                
            # Si Entity Tué
            if type(pTabOBJECT[1]) is cls_Entity:
                pTabOBJECT[1].Spawn()
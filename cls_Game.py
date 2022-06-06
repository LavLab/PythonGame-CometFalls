import pygame

from cls_Entity import cls_Entity

class cls_Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.c_StateRunning = True
        self.c_StateBreak = False
        self.c_StateLose = False
          
        self.c_ScreenLayer = []
        self.c_PressedKeys={}
        
        self.ScreenLayerLoad()
        
        self.Generate_Entity()
        
    def ScreenLayerLoad(self):        
        # Ordre des Calques (NOM, VISIBILITE EN PAUSE, VISIBILITE EN PERDU)
        self.c_ScreenLayer.append(("BACKGROUND",True,True))
        self.c_ScreenLayer.append(("ENTITY",True,True))

    def ScreenLayer(self, GameScreen):
        self.ScreenArea = GameScreen.get_rect()
        # Les Calques
        for Layer in self.c_ScreenLayer:
            # Si le calques visible en pause et perdu
            if Layer[1] == self.c_StateBreak or Layer[1] :
                if Layer[2] == self.c_StateLose or Layer[2]:
                    if Layer[0] == 'BACKGROUND':
                        Background = pygame.image.load('assets/Backgrounds\Black.png')
                        Background = pygame.transform.smoothscale(Background, pygame.display.get_surface().get_size())
                        GameScreen.blit(Background, (0,0))
                    if Layer[0] == 'ENTITY':
                        self.all_players.draw(GameScreen)
         
    # Ecran perdu 
    def GameLose(self, GameScreen):
        if self.c_StateLose:
            # Surface
            Surface = pygame.Surface((GameScreen.get_width(),GameScreen.get_height()))
            Surface.set_alpha(128)
            Surface.fill((0,0,0))
            GameScreen.blit(Surface, (0,0))
            # Texte
            myfont = pygame.font.SysFont(None, 40, 15)
            label = myfont.render("- PERDU -", 1, (255,255,255))
            text_rect = label.get_rect(center=(GameScreen.get_width()/2, GameScreen.get_height()/2 - 200))
            GameScreen.blit(label, text_rect)
    
    # Ecran pause  
    def GamePause(self, GameScreen):
        if self.c_StateBreak:
            # Surface
            Surface = pygame.Surface((GameScreen.get_width(),GameScreen.get_height()))
            Surface.set_alpha(128)
            Surface.fill((0,0,0))
            GameScreen.blit(Surface, (0,0))
            # Texte
            myfont = pygame.font.SysFont(None, 40, 15)
            label = myfont.render("- PAUSE -", 1, (255,255,255))
            text_rect = label.get_rect(center=(GameScreen.get_width()/2, GameScreen.get_height()/2 - 200))
            GameScreen.blit(label, text_rect)

    # -- ENTITIES --
    def Generate_Entity(self):
        self.all_Entities = pygame.sprite.Group()
        self.Spawn_Entity()
        
    def Spawn_Entity(self):
        Entity = cls_Entity(self)
        self.all_Entities.add(Entity)
        
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
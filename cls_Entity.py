import pygame

class cls_Entity(pygame.sprite.Sprite):
    def __init__(self, pGame):
        super().__init__()
        self.Game = pGame
        
        self.Statistics()
        self.LoadImages()
        self.Spawn()
        
    def Statistics(self):
        self.c_Damage = 5
        self.c_Speed = 5
        self.c_Level = 1
        
        self.c_Length = (350 / 100)
        self.c_Health_Max = self.c_Length * 100
        self.c_Health = 0
        self.c_Energy_Max = self.c_Length * 100
        self.c_Energy = 0
        
    def Spawn(self):        
        self.image = self.images[self.c_Level-1]
        self.rect = self.image.get_rect()
        
        # Point de Spawn : 
        # X :: Position Horizontale -> Hauteur(ecran.hauteur/2) - Largeur(image.largeur/2)
        # Y :: Position Verticale
        self.rect.x = (512/2)-(self.rect.width/2)
        self.rect.y = 600
                
        self.c_Health = self.c_Health_Max
        self.c_Energy = self.c_Energy_Max
        
    def LoadImages(self):
        self.images=[]
        self.images.append(pygame.image.load("assets\Entities\Player\0.png"))        
        self.image = self.images[self.c_Level-1]
        self.rect = self.image.get_rect()
            
        
        # Deplacement vers DROITE 
    def Move_Right(self):
        # POSITION + TAILLE inferrieur TAILLE ECRAN - 10 (bordure)
        if self.rect.x + self.rect.width < self.Game.ScreenArea.width - 10:
            self.rect.x += self.c_Speed 
        
        # Deplacement vers GAUCHE 
    def Move_Left(self):
        # POSITION supperieur TAILLE ECRAN + 10 (bordure)
        if self.rect.x > 0 + 10:
            self.rect.x -= self.c_Speed
        
        # Deplacement vers HAUT 
    def Move_Top(self):
        # POSITION supperieur TAILLE ECRAN + 100 (bordure)
        if  self.rect.y > 0 + 100:
            self.rect.y -= self.c_Speed
        
        # Deplacement vers BAS 
    def Move_Bot(self):
        # POSITION + TAILLE inferrieur TAILLE ECRAN - 100 (bordure)
        if self.rect.y + self.rect.height < self.Game.ScreenArea.height - 100:
            self.rect.y += self.c_Speed
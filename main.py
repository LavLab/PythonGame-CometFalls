import pygame

from cls_Game import cls_Game

# Initialisation pygame
pygame.init()
Clock = pygame.time.Clock()

# Charger GAME
Game = cls_Game()

# # Titre de la fenetre
pygame.display.set_caption("LavLab's PyGame - TEMPLATE")

# Definition de l'ecran (X,Y)
GameScreen = pygame.display.set_mode((512,900))

# Souris invisible
pygame.mouse.set_visible(0)

while Game.c_StateRunning:
    
    # Positionnement des Calques
    Game.ScreenLayer(GameScreen)
    
    # Jeu en Pause
    Game.GamePause(GameScreen)
    
    # Jeu en Perdu
    Game.GameLose(GameScreen)
 
    if not Game.c_StateBreak and not Game.c_StateLose:
        
        # Entity
        for entity in Game.all_entities:
                        
            # Déplacement DROITE
            if Game.c_PressedKeys.get(pygame.K_RIGHT):
                entity.Move_Right()
            
            # Déplacement GAUCHE
            if Game.c_PressedKeys.get(pygame.K_LEFT):
                entity.Move_Left()
                
            # Déplacement HAUT
            if Game.c_PressedKeys.get(pygame.K_UP):
                entity.Move_Top()
                
            # Déplacement BAS
            if Game.c_PressedKeys.get(pygame.K_DOWN):
                entity.Move_Bot()
            
    
    # MAJ de l'ecran
    pygame.display.flip()
            
    # Evenement de la fenetre
    for event in pygame.event.get():
            
        # Touches pressées
        if event.type == pygame.KEYDOWN:
            Game.c_PressedKeys[event.key] = True
                    
            # Touche [ECHAP] pressé
            if Game.c_PressedKeys.get(pygame.K_ESCAPE):
                if Game.c_StateBreak:
                    Game.c_StateBreak = False
                else:
                    Game.c_StateBreak = True
                    
            # Touche [P] pressé
            if Game.c_PressedKeys.get(pygame.K_p):
                if Game.c_StateLose:
                    Game.c_StateLose = False
                else:
                    Game.c_StateLose = True
    
        # Touches lachées  
        if event.type == pygame.KEYUP:
            Game.c_PressedKeys[event.key] = False                  
                
        # Fin de session
        if event.type == pygame.QUIT:
            Game.c_StateRunning = False
            pygame.quit()
    
    # Clock, 75 images par secondes
    Clock.tick(75)
import pygame
from framework.utils.vector2 import Vector2


class Entity:
    '''
    Entity is the base class for all game objects.
    position: Vector2 - the position of the entity
    hitbox: Vector2 - the size of the entity and the hitbox
    '''
    def __init__(self, hitbox: Vector2 = None, position: Vector2 = None, size: Vector2 = None, offset: Vector2 = Vector2(0, 0)):
        if(self.__class__.__name__ == 'Entity'):
            raise Exception("Entity cannot be instantiated")
        if(position == None):
            raise Exception("Entity must have a position")
        if(hitbox == None):
            raise Exception("Entity must have a hitbox")
        if(not hitbox.is_positive()):
            raise Exception("Hitbox must be positive")
        if(size == None):
            raise Exception("Entity cannot have size")
        if(not size.is_positive()):
            raise Exception("Position must be positive")
        self.position = position
        self.hitbox = hitbox
        self.size = size
        self.isActive = True
        self.fliped = False
        self.animation_manager = None
        self.texture = None
        self.offset = offset
        self.show_hitbox = False
        self.rect = pygame.Rect((position + offset).to_tuple(), hitbox.to_tuple())
    
    
    def __render__(self, display):
        if(self.animation_manager == None and self.texture == None):
            raise Exception("Entity must have either animation_manager or texture")
        if(self.animation_manager != None and self.texture != None):
            raise Exception("Entity cannot have both animation_manager and texture")
        if(self.isActive == False):
            return
        if(self.animation_manager != None):
            self.animation_manager.__render__(display)
        elif(self.texture != None):
            self.texture.__render__(display)
        else:
            raise Exception("Entity must have either animation_manager or texture")
        
        if(self.show_hitbox):
            pygame.draw.rect(display, (255, 0, 0), self.rect, 1)

    def __update__(self, event):
        if(self.isActive == False):
            return
        if(self.animation_manager != None):
            return
        elif(self.texture != None):
            return
        else:
            raise Exception("Entity must have either animation_manager or texture")
        
    def __on_collision__(self, others):
        pass        

    def set_position(self, position: Vector2):
        self.position = position
        self.rect = pygame.Rect((self.position + self.offset).to_tuple(), self.hitbox.to_tuple())

        # self.position = position
        # self.rect = pygame.Rect((self.position + self.offset).to_tuple(), self.hitbox.to_tuple())

    def is_colliding(self, other):
        return self.rect.colliderect(other.rect)


        
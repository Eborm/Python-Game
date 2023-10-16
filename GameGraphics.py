import Display
import pygame
import pygame.freetype

#Rendering en Detection Engine


class Button:
    def __init__(self, x, y, filename, scale):
        image = pygame.image.load('Textures/' + filename)
        width, height = image.get_width(), image.get_height()
        self.x, self.y = x, y
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def EventDetection(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        
        return action
    
    def draw(self):
        Display.display.blit(self.image, (self.rect.x, self.rect.y))

class Draw_image:
    def __init__(self, x, y, filename, scale):
        image = pygame.image.load('Textures/' + filename)
        width, height = image.get_width(), image.get_height()
        self.x, self.y = x, y
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        Display.display.blit(self.image, (self.rect.x, self.rect.y))
        
class Text:
    def __init__(self, x, y, text, text_color, font_size, font=None):
        self.clicked = False
        self.x, self.y = x, y
        if font is None:
            font_render = pygame.freetype.Font(None, font_size)
        else:
            font_render = pygame.freetype.Font(font, font_size)   
        
        self.Text_render, self.rect = font_render.render(text, text_color)
        
        
    def EventDetection(self):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True
        
        return action
            
    def Draw(self):
        Display.display.blit(self.Text_render, (self.x, self.y))
        
class Rectangle:
    def __init__(self, xc, yc, width, height, color, Border_width):
        x, y = xc-(width/2), yc-(height/2)
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.Border_width = Border_width
        
    def Draw(self, Fill):
        if Fill:
            pygame.draw.rect(Display.display, self.color, self.rect, self.Border_width)
        else:
            pygame.draw.rect(Display.display, self.color, self.rect)
            
class Cricle:
    def __init__(self, x, y, Radius, color, Border_width):
        self.x, self.y = x, y
        self.color = color
        self.Radius = Radius
        self.rect = (self.x, self.y)
        self.Border_width = Border_width
        
    def Draw(self, Fill):
        if not Fill:
            pygame.draw.circle(Display.display, self.color, self.rect, self.Radius)
        if Fill:
            pygame.draw.circle(Display.display, self.color, self.rect, self.Radius, self.Border_width)

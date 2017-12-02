# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:58:12 2017

@author: aluno
"""
import pygame 

#myfont = pygame.font.SysFont("monospace", 30)
#label1 = myfont.render("angulo do cutuvelo direito:", 1, (255,255,0))
class button(object):
    def __init__(self,screen,button_points, color,text):
        self.screen = screen
        self.button_points = button_points
        self.color = color        
        self.visible = True
        self.text = text
        #state 0: inicializado
        #state 1: pressionado pela primeira vez
        #state 2: o botão continua pressionado
        #state 3: o botão foi pressionado e foi largado #senne ponto retornar o true
        self.state = 0
        self.on_off = False
        
        #color1, mao em cima do botão
        self.color1=(round(color[0]*3/4),round(color[1]*3/4),round(color[2]*3/4))
        #color2 mao pressionando o botão
        self.color2 = (round(self.color1[0]*3/4),round(self.color1[1]*3/4),round(self.color1[2]*3/4))
    
    def draw(self,hand_points,hand_state):
        if self.visible:
            if ( (hand_points[0]>=self.button_points[0]) and (hand_points[0]<=(self.button_points[0]+self.button_points[2])) 
                and (hand_points[1]>=self.button_points[1]) and (hand_points[1]<=(self.button_points[1]+self.button_points[3])) ): 
                if (hand_state == 3) :        
                    pygame.draw.rect(self.screen,self.color2,self.button_points)
                    #self.screen.blit(self.label, (button.button_points[0]+2, button.button_points[1]+2))
                    if (self.state==0):
                        self.state = 1
                        return False
                    if (self.state==1):
                        self.state = 2
                        return False

                else:
                    pygame.draw.rect(self.screen,self.color1,self.button_points)                    
                    if (self.state==2):
                        self.state = 3
                        self.on_off = not self.on_off
                        return True
                    else:
                        self.state = 0
                        return False
            else:
                self.state = 0
                pygame.draw.rect(self.screen,self.color,self.button_points)
                #self.screen.blit(self.label, (button.button_points[0]+2, button.button_points[1]+2))
                return False
        else:
            return False
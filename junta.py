# -*- coding: utf-8 -*-
"""
joints ids
SpineBase = 0
SpineMid = 1
Neck = 2
Head = 3
ShoulderLeft = 4
ElbowLeft = 5
WristLeft = 6
HandLeft = 7
ShoulderRight = 8
ElbowRight = 9
WristRight = 10
HandRight = 11
HipLeft = 12
KneeLeft = 13
AnkleLeft = 14
FootLeft = 15
HipRight = 16
KneeRight = 17
AnkleRight = 18
FootRight = 19
SpineShoulder = 20
HandTipLeft = 21
ThumbLeft = 22
HandTipRight = 23
ThumbRight = 24

@author: Lucas
definir uma junta
"""
import numpy #as np
class Junta(object):
    def __init__(self, x=None, y=None, z=None, n=None, nPai=None,nome=""):
        self.x=x
        self.y=y
        self.z=z
        self.n=n
        self.nPai=None
        self.nome=nome
        
    def getPosicao(self):
        return [self.x,self.y,self.z]    
    def getNome(self):
        return [self.nome]
    def getNoNumero(self):
        return [self.n]
    def getNoPai(self):
        return [self.nPai]
    
    def setPosicao(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z        
    def setNome(self,nome):
        self.nome=nome
    def setNoNumero(self):
        return [self.n]
    def setNoPai(self):
        return [self.n]
    
   
    def getJointMemberAngle(self, outraJunta):
        """
        usar cordenada esférica: angulo alfa e angulo beta, com o raio r
        alfa(x,y)
        beta(z,y)
        
        """
        
        #calcula as distÂncias        
        dx= outraJunta.x - self.x
        dy= outraJunta.y - self.y
        dz= outraJunta.z - self.z 
        
        #calcula a distancia entreos pontos
        r=(dx**2+dy**2+dz**2)**0.5
        #Calcula alfa (angulo entre o ponto e os planos x e y)        
        #evita a divisão por zero
        if dx == 0:
            if dy > 0:
                alfa = 90#np.pi/2*(180/np.pi)
            else:
                alfa=-90
        else:
            if dx>0 and dy>=0:
                alfa = numpy.arctan(numpy.abs(dy/dx))*(180/numpy.pi)
            elif dx<0 and dy>0:
                alfa = 180 - numpy.arctan(numpy.abs(dy/dx))*(180/numpy.pi)
            elif dx>0 and dy<0:
                alfa = -numpy.arctan(numpy.abs(dy/dx))*(180/numpy.pi)
            elif dx<0 and dy<0:
                alfa = -180 + numpy.arctan(numpy.abs(dy/dx))*(180/numpy.pi)           
        
        #Calcula beta (angulo entre o ponto e os planos y e z)
        if dy == 0:
            if dz > 0:
                beta = 0#np.pi/2*(180/np.pi)
            else:
                beta=-180
        else:
            if dy>0 and dz>=0:
                beta = numpy.arctan(numpy.abs(dz/dy))*(180/numpy.pi)
            elif dy<0 and dz>=0:
                beta = 180 - numpy.arctan(numpy.abs(dz/dy))*(180/numpy.pi)
            elif dy>0 and dz<0:
                beta = -numpy.arctan(numpy.abs(dz/dy))*(180/numpy.pi)
            elif dy<0 and dz<0:
                beta = -180 + numpy.arctan(numpy.abs(dz/dy))*(180/numpy.pi)    
                
        
        return [r,alfa,beta]
    
    def getMemberMemberAngle(self, outraJunta1, outraJunta2):
        """
        usar cordenada esférica: angulo alfa e angulo beta, com o raio r
        alfa(x,y)
        beta(z,y)
        
        """
        
        #calcula os vetores do membro 1        
        dx1= outraJunta1.x - self.x
        dy1= outraJunta1.y - self.y
        dz1= outraJunta1.z - self.z 
        
        #calcula os vetores do membro 2        
        dx2= outraJunta2.x - self.x
        dy2= outraJunta2.y - self.y
        dz2= outraJunta2.z - self.z 
        
        #calcula o mod
        r1=(dx1**2+dy1**2+dz1**2)**0.5
        r2=(dx2**2+dy2**2+dz2**2)**0.5
        
        angle=numpy.arccos( ( (dx1*dx2)+(dy1*dy2)+(dz1*dz2) ) / (r1*r2))
        angle=angle*(180/numpy.pi)
              
        
        return angle
        
        
    


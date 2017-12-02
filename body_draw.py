# -*- coding: utf-8 -*-
import pygame

def draw_recorded_body (data, screen, color, line_size, frame):
    #desenha cabeça|pescoço_topo (3-2)
    pygame.draw.line(screen,color,[data[3][frame][0],data[3][frame][1]],[data[2][frame][0],data[2][frame][1]],line_size)
    #desenha pescoço_topo|pescoço_base (2-20)
    pygame.draw.line(screen,color,[data[2][frame][0],data[2][frame][1]],[data[20][frame][0],data[20][frame][1]],line_size)

    #desenha pescoço_base|ombro_direito (20-8)
    pygame.draw.line(screen,color,[data[20][frame][0],data[20][frame][1]],[data[8][frame][0],data[8][frame][1]],line_size)
    #desenha ombro_direito|cutuvelo_direito (8-9)
    pygame.draw.line(screen,color,[data[8][frame][0],data[8][frame][1]],[data[9][frame][0],data[9][frame][1]],line_size)
    #desenha cutuvelo_direito|mao_base_direita (9-10)
    pygame.draw.line(screen,color,[data[9][frame][0],data[9][frame][1]],[data[10][frame][0],data[10][frame][1]],line_size)
    #desenha mao_base_direita|mao_topo_direita (10-11)
    pygame.draw.line(screen,color,[data[10][frame][0],data[10][frame][1]],[data[11][frame][0],data[11][frame][1]],line_size)
    #desenha mao_topo_direita|dedo_direito (11-23)
    pygame.draw.line(screen,color,[data[11][frame][0],data[11][frame][1]],[data[23][frame][0],data[23][frame][1]],line_size)
    #desenha mao_base_direita|polegar_direito (10-24)
    pygame.draw.line(screen,color,[data[10][frame][0],data[10][frame][1]],[data[24][frame][0],data[24][frame][1]],line_size)

    #desenha pescoço_base|ombro_esquerdo (20-4)
    pygame.draw.line(screen,color,[data[20][frame][0],data[20][frame][1]],[data[4][frame][0],data[4][frame][1]],line_size)
    #desenha ombro_esquerdo|cutuvelo_esquerdo (4-5)
    pygame.draw.line(screen,color,[data[4][frame][0],data[4][frame][1]],[data[5][frame][0],data[5][frame][1]],line_size)
    #desenha cutuvelo_esquerdo|mao_base_esquerda (5-6)
    pygame.draw.line(screen,color,[data[5][frame][0],data[5][frame][1]],[data[6][frame][0],data[6][frame][1]],line_size)
    #desenha mao_base_esquerda|mao_topo_esquerda (6-7) 
    pygame.draw.line(screen,color,[data[6][frame][0],data[6][frame][1]],[data[7][frame][0],data[7][frame][1]],line_size)
    #desenha mao_topo_esquerda|dedo_esquerdo (7-21)
    pygame.draw.line(screen,color,[data[7][frame][0],data[7][frame][1]],[data[21][frame][0],data[21][frame][1]],line_size)
    #desenha mao_base_esquerda|polegar_esquerdo (6-22)
    pygame.draw.line(screen,color,[data[6][frame][0],data[6][frame][1]],[data[22][frame][0],data[22][frame][1]],line_size)

    #desenha pescoço_base|coluna_meio (20-1)
    pygame.draw.line(screen,color,[data[20][frame][0],data[20][frame][1]],[data[1][frame][0],data[1][frame][1]],line_size)
    #desenha coluna_meio|coluna_base (1-0)
    pygame.draw.line(screen,color,[data[1][frame][0],data[1][frame][1]],[data[0][frame][0],data[0][frame][1]],line_size)

    #desenha coluna_base|cintura_direita (0-16)
    pygame.draw.line(screen,color,[data[0][frame][0],data[0][frame][1]],[data[16][frame][0],data[16][frame][1]],line_size)
    #desenha cintura_direita|joelho_direito (16-17)
    pygame.draw.line(screen,color,[data[16][frame][0],data[16][frame][1]],[data[17][frame][0],data[17][frame][1]],line_size)
    #desenha joelho_direito|calcanhar_direito (17-18)
    pygame.draw.line(screen,color,[data[17][frame][0],data[17][frame][1]],[data[18][frame][0],data[18][frame][1]],line_size)
    #desenha calcanhar_direito|pé_direito (18-19)
    pygame.draw.line(screen,color,[data[18][frame][0],data[18][frame][1]],[data[19][frame][0],data[19][frame][1]],line_size)

    #desenha coluna_base|cintura_esquerda (0-12)
    pygame.draw.line(screen,color,[data[0][frame][0],data[0][frame][1]],[data[12][frame][0],data[12][frame][1]],line_size)
    #desenha cintura_esquerdo|joelho_esquerdo (12-13)
    pygame.draw.line(screen,color,[data[12][frame][0],data[12][frame][1]],[data[13][frame][0],data[13][frame][1]],line_size)
    #desenha joelho_esquerdo|calcanhar_esquerdo (13-14)
    pygame.draw.line(screen,color,[data[13][frame][0],data[13][frame][1]],[data[14][frame][0],data[14][frame][1]],line_size)
    #desenha calcanhar_esquerdo|pé_esquerdo (14-15)
    pygame.draw.line(screen,color,[data[14][frame][0],data[14][frame][1]],[data[15][frame][0],data[15][frame][1]],line_size)


def draw_live_body (data, screen, color, line_size):
    kinect_width=512
    
    #desenha cabeça|pescoço_topo (3-2)
    #if(data[3][0]) #confere se algum dos dos elementos é -1
    if (not (data[3][0]==-1 or data[2][0]==-1) ):
       pygame.draw.line(screen,color,[data[3][0]+kinect_width,data[3][1]],[data[2][0]+kinect_width,data[2][1]],line_size)
    #desenha pescoço_topo|pescoço_base (2-20)
    if (not (data[2][0]==-1 or data[20][0]==-1) ):
        pygame.draw.line(screen,color,[data[2][0]+kinect_width,data[2][1]],[data[20][0]+kinect_width,data[20][1]],line_size)

    #desenha pescoço_base|ombro_direito (20-8)
    if (not (data[20][0]==-1 or data[8][0]==-1) ):
        pygame.draw.line(screen,color,[data[20][0]+kinect_width,data[20][1]],[data[8][0]+kinect_width,data[8][1]],line_size)
    #desenha ombro_direito|cutuvelo_direito (8-9)
    if (not (data[8][0]==-1 or data[9][0]==-1) ):
        pygame.draw.line(screen,color,[data[8][0]+kinect_width,data[8][1]],[data[9][0]+kinect_width,data[9][1]],line_size)
    #desenha cutuvelo_direito|mao_base_direita (9-10)#2 mao aberta #3 mao fechada
    if (not (data[9][0]==-1 or data[12][0]==-1) ):
        pygame.draw.line(screen,color,[data[9][0]+kinect_width,data[9][1]],[data[10][0]+kinect_width,data[10][1]],line_size)
    
    #se a mao estiver fechada a cor muda para cyan
    if (data[25][1]==3): 
        #desenha mao_base_direita|mao_topo_direita (10-11)
        if (not (data[10][0]==-1 or data[11][0]==-1) ):
            pygame.draw.line(screen,(0,255,255),[data[10][0]+kinect_width,data[10][1]],[data[11][0]+kinect_width,data[11][1]],line_size)
        #desenha mao_topo_direita|dedo_direito (11-23)
        if (not (data[11][0]==-1 or data[23][0]==-1) ):
            pygame.draw.line(screen,(0,255,255),[data[11][0]+kinect_width,data[11][1]],[data[23][0]+kinect_width,data[23][1]],line_size)
        #desenha mao_base_direita|polegar_direito (10-24)
        if (not (data[10][0]==-1 or data[24][0]==-1) ):
            pygame.draw.line(screen,(0,255,255),[data[10][0]+kinect_width,data[10][1]],[data[24][0]+kinect_width,data[24][1]],line_size)
        
    else:   

        #desenha mao_base_direita|mao_topo_direita (10-11)
        if (not (data[10][0]==-1 or data[11][0]==-1) ):
            pygame.draw.line(screen,color,[data[10][0]+kinect_width,data[10][1]],[data[11][0]+kinect_width,data[11][1]],line_size)
        #desenha mao_topo_direita|dedo_direito (11-23)
        if (not (data[11][0]==-1 or data[23][0]==-1) ):
            pygame.draw.line(screen,color,[data[11][0]+kinect_width,data[11][1]],[data[23][0]+kinect_width,data[23][1]],line_size)
        #desenha mao_base_direita|polegar_direito (10-24)
        if (not (data[10][0]==-1 or data[24][0]==-1) ):
            pygame.draw.line(screen,color,[data[10][0]+kinect_width,data[10][1]],[data[24][0]+kinect_width,data[24][1]],line_size)
            
        

    #desenha pescoço_base|ombro_esquerdo (20-4)
    if (not (data[20][0]==-1 or data[4][0]==-1) ):
        pygame.draw.line(screen,color,[data[20][0]+kinect_width,data[20][1]],[data[4][0]+kinect_width,data[4][1]],line_size)
    #desenha ombro_esquerdo|cutuvelo_esquerdo (4-5)
    if (not (data[4][0]==-1 or data[5][0]==-1) ):
        pygame.draw.line(screen,color,[data[4][0]+kinect_width,data[4][1]],[data[5][0]+kinect_width,data[5][1]],line_size)
    #desenha cutuvelo_esquerdo|mao_base_esquerda (5-6)
    if (not (data[5][0]==-1 or data[6][0]==-1) ):
        pygame.draw.line(screen,color,[data[5][0]+kinect_width,data[5][1]],[data[6][0]+kinect_width,data[6][1]],line_size)
    
    #desenha mao_base_esquerda|mao_topo_esquerda (6-7) #2 mao aberta #3 mao fechada
    #se a mao estiver fechada a cor muda para azul
    if (data[25][0]==3):
        if (not (data[6][0]==-1 or data[7][0]==-1) ):
            pygame.draw.line(screen,(0,255,255),[data[6][0]+kinect_width,data[6][1]],[data[7][0]+kinect_width,data[7][1]],line_size)
    else:
        if (not (data[6][0]==-1 or data[7][0]==-1) ):
            pygame.draw.line(screen,color,[data[6][0]+kinect_width,data[6][1]],[data[7][0]+kinect_width,data[7][1]],line_size)

    #desenha mao_topo_esquerda|dedo_esquerdo (7-21) #2 mao aberta #3 mao fechada
    #se a mao estiver fechada a cor muda para azul
    if (data[25][0]==3):
        if (not (data[7][0]==-1 or data[21][0]==-1) ):
            pygame.draw.line(screen,(0,255,255),[data[7][0]+kinect_width,data[7][1]],[data[21][0]+kinect_width,data[21][1]],line_size)
    #se não continua na cor original
    else:
        if (not (data[7][0]==-1 or data[21][0]==-1) ):
            pygame.draw.line(screen,color,[data[7][0]+kinect_width,data[7][1]],[data[21][0]+kinect_width,data[21][1]],line_size)
    
    #desenha mao_base_esquerda|polegar_esquerdo (6-22) #2 mao aberta #3 mao fechada
    #se a mao estiver fechada a cor muda para azul
    if (not (data[6][0]==-1 or data[22][0]==-1) ):
        if (data[25][0]==3):
            pygame.draw.line(screen,(0,255,255),[data[6][0]+kinect_width,data[6][1]],[data[22][0]+kinect_width,data[22][1]],line_size)
        else:
            pygame.draw.line(screen,color,[data[6][0]+kinect_width,data[6][1]],[data[22][0]+kinect_width,data[22][1]],line_size)

    #desenha pescoço_base|coluna_meio (20-1)
    if (not (data[20][0]==-1 or data[1][0]==-1) ):
        pygame.draw.line(screen,color,[data[20][0]+kinect_width,data[20][1]],[data[1][0]+kinect_width,data[1][1]],line_size)
    #desenha coluna_meio|coluna_base (1-0)
    if (not (data[1][0]==-1 or data[0][0]==-1) ):
        pygame.draw.line(screen,color,[data[1][0]+kinect_width,data[1][1]],[data[0][0]+kinect_width,data[0][1]],line_size)

    #desenha coluna_base|cintura_direita (0-16)
    if (not (data[0][0]==-1 or data[16][0]==-1) ):
        pygame.draw.line(screen,color,[data[0][0]+kinect_width,data[0][1]],[data[16][0]+kinect_width,data[16][1]],line_size)
    #desenha cintura_direita|joelho_direito (16-17)
    if (not (data[16][0]==-1 or data[17][0]==-1) ):
        pygame.draw.line(screen,color,[data[16][0]+kinect_width,data[16][1]],[data[17][0]+kinect_width,data[17][1]],line_size)
    #desenha joelho_direito|calcanhar_direito (17-18)
    if (not (data[17][0]==-1 or data[18][0]==-1) ):
        pygame.draw.line(screen,color,[data[17][0]+kinect_width,data[17][1]],[data[18][0]+kinect_width,data[18][1]],line_size)
    #desenha calcanhar_direito|pé_direito (18-19)
    if (not (data[18][0]==-1 or data[19][0]==-1) ):
        pygame.draw.line(screen,color,[data[18][0]+kinect_width,data[18][1]],[data[19][0]+kinect_width,data[19][1]],line_size)

    #desenha coluna_base|cintura_esquerda (0-12)
    if (not (data[0][0]==-1 or data[12][0]==-1) ):
        pygame.draw.line(screen,color,[data[0][0]+kinect_width,data[0][1]],[data[12][0]+kinect_width,data[12][1]],line_size)
    #desenha cintura_esquerdo|joelho_esquerdo (12-13)
    if (not (data[12][0]==-1 or data[13][0]==-1) ):
        pygame.draw.line(screen,color,[data[12][0]+kinect_width,data[12][1]],[data[13][0]+kinect_width,data[13][1]],line_size)
    #desenha joelho_esquerdo|calcanhar_esquerdo (13-14)
    if (not (data[13][0]==-1 or data[14][0]==-1) ):
        pygame.draw.line(screen,color,[data[13][0]+kinect_width,data[13][1]],[data[14][0]+kinect_width,data[14][1]],line_size)
    #desenha calcanhar_esquerdo|pé_esquerdo (14-15)
    if (not (data[14][0]==-1 or data[15][0]==-1) ):
        pygame.draw.line(screen,color,[data[14][0]+kinect_width,data[14][1]],[data[15][0]+kinect_width,data[15][1]],line_size)



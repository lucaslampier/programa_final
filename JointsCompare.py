# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 19:44:13 2017
Função do jogo em sí
recebe de entrada oframe que será analisado dos dados 
gravados e o frame ao vivo pego pelo kinect

#calcula os angulos dos dois
#faz a diferença e retorna o resultado

entrada:
    rec_data_frame
    live_data_frame
    
saida:
    [junta principal,angulo_rec, angulo_live]%
@author: Lucas
"""
import junta
#jn:[anterior, centro, pposterior]
#compara só uma junta
def JointsCompare(rec_data,live_data,frame,k,jn):
    if live_data is None:        
        return None
    
    j0_rec = junta.Junta(rec_data[jn[0]][frame][0]*k,rec_data[jn[0]][frame][1]*k,rec_data[jn[0]][frame][2]/10)
    j1_rec = junta.Junta(rec_data[jn[1]][frame][0]*k,rec_data[jn[1]][frame][1]*k,rec_data[jn[1]][frame][2]/10)
    j2_rec = junta.Junta(rec_data[jn[2]][frame][0]*k,rec_data[jn[2]][frame][1]*k,rec_data[jn[2]][frame][2]/10)
    
    j0_live = junta.Junta(live_data[jn[0]][0]*k,live_data[jn[0]][1]*k,live_data[jn[0]][2]/10)
    j1_live = junta.Junta(live_data[jn[1]][0]*k,live_data[jn[1]][1]*k,live_data[jn[1]][2]/10)
    j2_live = junta.Junta(live_data[jn[2]][0]*k,live_data[jn[2]][1]*k,live_data[jn[2]][2]/10)
    
    #print ("a1=",j1_live.getMemberMemberAngle(j0_live,j2_live)," a2= ",j1_rec.getMemberMemberAngle(j0_rec,j2_rec))
    ang = [jn[1],j1_live.getMemberMemberAngle(j0_live,j2_live),j1_rec.getMemberMemberAngle(j0_rec,j2_rec)]
    
    return ang
##fazer inicialmente os joelhos, cotovelos 

#def JointsCompare(rec_data,live_data,frame,k):
#    if live_data is None:
#        return None
#    ####Parte gravada
#    #braço direito
#    rec_ombro_direito = junta.Junta(rec_data[8][frame][0]*k,rec_data[8][frame][1]*k,rec_data[8][frame][2]/10)
#    rec_cotovelo_direito = junta.Junta(rec_data[9][frame][0]*k,rec_data[9][frame][1]*k,rec_data[9][frame][2]/10)
#    rec_pulso_direito = junta.Junta(rec_data[10][frame][0]*k,rec_data[10][frame][1]*k,rec_data[10][frame][2]/10)
#    #braço esquerdo
#    rec_ombro_esquerdo = junta.Junta(rec_data[4][frame][0]*k,rec_data[4][frame][1]*k,rec_data[4][frame][2]/10)
#    rec_cotovelo_esquerdo = junta.Junta(rec_data[5][frame][0]*k,rec_data[5][frame][1]*k,rec_data[5][frame][2]/10)
#    rec_pulso_esquerdo = junta.Junta(rec_data[6][frame][0]*k,rec_data[6][frame][1]*k,rec_data[6][frame][2]/10)
#    #perna direita
#    rec_quadril_direito = junta.Junta(rec_data[16][frame][0]*k,rec_data[16][frame][1]*k,rec_data[16][frame][2]/10)
#    rec_joelho_direito = junta.Junta(rec_data[17][frame][0]*k,rec_data[17][frame][1]*k,rec_data[17][frame][2]/10)
#    rec_calcanhar_direito = junta.Junta(rec_data[18][frame][0]*k,rec_data[18][frame][1]*k,rec_data[18][frame][2]/10)
#    #perna esquerda
#    rec_quadril_esquerdo = junta.Junta(rec_data[16][frame][0]*k,rec_data[16][frame][1]*k,rec_data[16][frame][2]/10)
#    rec_joelho_esquerdo = junta.Junta(rec_data[17][frame][0]*k,rec_data[17][frame][1]*k,rec_data[17][frame][2]/10)
#    rec_calcanhar_esquerdo = junta.Junta(rec_data[18][frame][0]*k,rec_data[18][frame][1]*k,rec_data[18][frame][2]/10)
#    
#       
#    ####parte live
#    live_ombro_direito = junta.Junta(live_data[8][0]*k,live_data[8][1]*k,live_data[8][2]/10)
#    live_cotovelo_direito = junta.Junta(live_data[9][0]*k,live_data[9][1]*k,live_data[9][2]/10)
#    live_pulso_direito = junta.Junta(live_data[10][0]*k,live_data[10][1]*k,live_data[10][2]/10)
#    #braço esquerdo
#    live_ombro_esquerdo = junta.Junta(live_data[4][0]*k,live_data[4][1]*k,live_data[4][2]/10)
#    live_cotovelo_esquerdo = junta.Junta(live_data[5][0]*k,live_data[5][1]*k,live_data[5][2]/10)
#    live_pulso_esquerdo = junta.Junta(live_data[6][0]*k,live_data[6][1]*k,live_data[6][2]/10)
#    #perna direita
#    live_quadril_direito = junta.Junta(live_data[16][0]*k,live_data[16][1]*k,live_data[16][2]/10)
#    live_joelho_direito = junta.Junta(live_data[17][0]*k,live_data[17][1]*k,live_data[17][2]/10)
#    live_calcanhar_direito = junta.Junta(live_data[18][0]*k,live_data[18][1]*k,live_data[18][2]/10)
#    #perna esquerda
#    live_quadril_esquerdo = junta.Junta(live_data[12][0]*k,live_data[12][1]*k,live_data[12][2]/10)
#    live_joelho_esquerdo = junta.Junta(live_data[13][0]*k,live_data[13][1]*k,live_data[13][2]/10)
#    live_calcanhar_esquerdo = junta.Junta(live_data[14][0]*k,live_data[14][1]*k,live_data[14][2]/10)
#    
#    #inicializa a matriz resultado
#    result = []
#    
#    #cotovelo direito
#    result.append([9,live_cotovelo_direito.getMemberMemberAngle(live_ombro_direito,live_pulso_direito),rec_cotovelo_direito.getMemberMemberAngle(rec_ombro_direito,rec_pulso_direito)])
#    #cotovelo esquerdo
#    result.append([5,live_cotovelo_esquerdo.getMemberMemberAngle(live_ombro_esquerdo,live_pulso_esquerdo),rec_cotovelo_esquerdo.getMemberMemberAngle(rec_ombro_esquerdo,rec_pulso_esquerdo)])
#    #Joelho direito
#    result.append([17,live_joelho_direito.getMemberMemberAngle(live_quadril_direito,live_calcanhar_direito),rec_joelho_direito.getMemberMemberAngle(rec_quadril_direito,rec_calcanhar_direito)])
#    #Joelho esquerdo
#    result.append([13,live_joelho_esquerdo.getMemberMemberAngle(live_quadril_esquerdo,live_calcanhar_esquerdo),rec_joelho_esquerdo.getMemberMemberAngle(rec_quadril_esquerdo,rec_calcanhar_esquerdo)])
#    
#    return result
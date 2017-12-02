# -*- coding: cp1252 -*-
import pygame
import numpy as np
import datetime as dt
import os

import load_recorded_data
import JointsCompare
import Kinect_live
import DrawButton as Button
import body_draw
import numpy

kinect_width = 512

width=512*2
height=424

#data=load_recorded_data.get_data(filepath)

#constantepara transformar x e y de y para mm
k=0.57430990363651113;

kinect = Kinect_live.Body_Position()

#lista de juntas
BODY_LIST = [

        ['SpineBase' , 0],
        ['SpineMid' , 1],
        ['Neck' , 2],
        ['Head' , 3],
        ['ShoulderLeft' , 4],
        ['ElbowLeft' , 5],
        ['WristLeft' , 6],
        ['HandLeft' , 7],
        ['ShoulderRight' , 8],
        ['ElbowRight' , 9],
        ['WristRight' , 10],
        ['HandRight' , 11],
        ['HipLeft' , 12],
        ['KneeLeft' , 13],
        ['AnkleLeft' , 14],
        ['FootLeft' , 15],
        ['HipRight' , 16],
        ['KneeRight' , 17],
        ['AnkleRight' , 18],
        ['FootRight' , 19],
        ['SpineShoulder' , 20],
        ['HandTipLeft' , 21],
        ['ThumbLeft' , 22],
        ['HandTipRight' , 23],
        ['ThumbRight' , 24]
        ]

def Live_Data():
    data = kinect.take_matrix()
    return data

def find_k(frame,cutuvelo,punho):
    D = 25

    x0p=cutuvelo[0]#df['ElbowRight_x'].values[frame]
    y0p=cutuvelo[1]#df['ElbowRight_y'].values[frame]
    z0p=cutuvelo[2]/10#df['ElbowRight_z'].values[frame]/10

    x1p=punho[0]#df['WristRight_x'].values[frame]
    y1p=punho[1]#df['WristRight_y'].values[frame]
    z1p=punho[2]/10#df['WristRight_z'].values[frame]/10

    dx = x1p - x0p
    dy = y1p - y0p
    dz = z1p - z0p

    k=((D**2-dz**2)/(dx**2+dy**2))**0.5

    return k


def WriteFile(filename,List,mode):
    file = open(filename, mode)
    for idx,item in enumerate(List):
        if idx==len(List)-1:
            file.write(item+"\n")
        else:
            file.write(item + ",")
    file.close()

def DrawButton(button, button_points,hand_points,hand_state, myfont, screen):
    button.button_points = button_points
    button.draw(hand_points,hand_state)

    #poe o texto no botão
    button_label = myfont.render(button.text, 1, (0,0,0))
    screen.blit(button_label, (button_points[0]+2, button_points[1]+2))
    return button

def ShowMessage(time,myfont,screen,position,color):    
    label =  myfont.render(str(time), 1, color)
    screen.blit(label, (position[0],position [1]))

"""
######################
essa função rodará o jogo propiamente 
ele recebe o frame alvo, até que os angulos 
do livebody nao chegem proximo (10% erro) dos
angulos gravados 
entradas:
    angulo_alvo[cotovelo_direito,joelho_direito,cotovelo_esquerdo,joelho_esquerdo]
    angulo_atual[cotovelo_direito,joelho_direito,cotovelo_esquerdo,joelho_esquerdo]
    T(periodo entre dois frames)
    fps

saídas
    prox_frame 
"""
def AnguloAlvo(ang_matriz,T,fps,frame,erro):
    if ang_matriz is None:
        return (frame + 1)

    for idx in range(0,len(ang_matriz)):
        if ang_matriz[idx][1] > ang_matriz[idx][2]+erro or ang_matriz[idx][1] < ang_matriz[idx][2]-erro:
            return frame
    return int(frame + T*fps) 

def ang_colors(ang_matriz,idx,erro):
    if (ang_matriz[idx][1]<(ang_matriz[idx][2]-erro) ):
        ang_color = (255,0,0)
    elif(ang_matriz[idx][1]>(ang_matriz[idx][2]+erro) ):
        ang_color = (0,0,255)
    else:
        ang_color = (0,255,0)
    return ang_color
        

def main():
    millseconds=40
    fps = 1000/millseconds

    #inicializa os módulos
    pygame.init()

    #Inicializa a tela no tamanho desejado
    screen = pygame.display.set_mode((width, height))

    #flag
    done = False

    #contador de frames(play)
    frame=0
    
    #contador de frames(apenas mostrar)
    rec_frame=0    
    
    #erro aceitavel pelo programa
    erro = 20

    #definir a fonte do texto
    myfont = pygame.font.SysFont("monospace", 20)
    
    #backcounterfont
    bcfont=pygame.font.SysFont("monospace", 50)

    #inicializar o Botão menu
    button_color = (255,51,255) #rosa
    menu_button = Button.button(screen,[0,0,0,0], button_color, "MENU")

    #iniciar o botão gravar
    rec_button = Button.button(screen,[0,0,0,0], button_color, "REC")
    rec_button.visible = False
    #iniciar o botão reproduzir
    rep_button = Button.button(screen,[0,0,0,0], button_color, "REP")
    rep_button.visible = False
    #botão de voltar
    back_button = Button.button(screen,[0,0,0,0], button_color, "<<<")
    back_button.visible = False

    #botoes da lista de aulas
    #rep_cima
    rep_up_button = Button.button(screen,[0,0,0,0], button_color, "^^^")
    rep_up_button.visible = False
    #rep_aula
    rep_aula_button = Button.button(screen,[0,0,0,0], button_color, "Aula x")
    rep_aula_button.visible = False
    #rep_baixo
    rep_down_button = Button.button(screen,[0,0,0,0], button_color, "vvv")
    rep_down_button.visible = False


    #define se é a mesma ou uma nova gravação
    rec_inicializada = False
    #escrever o arquivo
    savepath="C:\\Users\\aluno\\Documents\\Lucas TCC\\DataBase\\"
    filename =""

    replist =[]
    repidx = 0

    #arquivo que será carregado
    db_file = None
    
    #flag para inicialização de jogo
    play=False

    #contagem de tempo para cortar um pouco do inicio e do fim
    start_rec_time=4
    rec_time=0
    
    data = []

    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        color = (0,255,0)
        line_size= 5

        #limpar a tela
        screen.fill((0,0,0))

        #desenhar o corpo da camera
        live_data = Live_Data()
        if (live_data != None):
            #print (live_data)
            if ( (live_data[0][2]>=2000) and (live_data[0][2]<=3000)):
                try:

                    menu_button_points = [live_data[8][0]+kinect_width, live_data[3][1]-30, 50, 20]
                    hand_points = [live_data[11][0]+kinect_width,live_data[11][1]]
                    hand_state = live_data[25][1]

#                #desenhar o botão menu
                    menu_button = DrawButton(menu_button, menu_button_points ,hand_points,hand_state, myfont, screen)

                    #se o botão de menu for pressionado( menu.state==3 )
                    if menu_button.on_off:
                        menu_button.visible = False
                        #desenhar os botoes de gravar, reproduzir e voltar
                        #gravar
                        rec_button_points = [menu_button_points[0],menu_button_points[1],50,20]
                        rec_button.visible = True
                        rec_button = DrawButton(rec_button, rec_button_points ,hand_points,hand_state, myfont, screen)

                        #reproduzir
                        rep_button_points =  [menu_button_points[0],menu_button_points[1]+25,50,20]
                        rep_button.visible = True
                        rep_button = DrawButton(rep_button, rep_button_points ,hand_points,hand_state, myfont, screen)

                        #voltar
                        back_button_points = [menu_button_points[0],menu_button_points[1]+50,50,20]
                        back_button.visible = True
                        back_button = DrawButton(back_button, back_button_points ,hand_points,hand_state, myfont, screen)

                    #se o botão back for pressionado, voltar ao menu
                    if back_button.state==3:
                        rec_button.visible = False
                        rep_button.visible = False
                        rep_up_button.visible = False
                        rep_aula_button.visible = False
                        rep_down_button.visible = False
                        back_button.visible = False

                        #tornar o menu visível
                        menu_button.on_off = False
                        menu_button.state = 0
                        menu_button.visible = True
                        #dessetar o back button
                        back_button.state=0
                        back_button.on_off = False


                    #desenha o corpo
                    body_draw.draw_live_body(live_data, screen, (0,255,0), line_size)

                except:
                    print("Erro")
                    pass
            else:
                try:
                    msg = ""
                    if (live_data[0][2]<2000):
                        msg = "Por favor, afarte-se da camera"
                    else:
                        msg = "Por favor, aproxime-se da camera"
                    infoLabel =  myfont.render(msg, 1, (255,255,0))
                    screen.blit(infoLabel, (100+kinect_width, 10))
                    body_draw.draw_live_body(live_data, screen, (255,0,0), line_size)

                except:
                    pass

        #desenhar o arquivo guardado
        if rep_button.on_off:
            
            #TODO ficar petitindo os mevimentos enquanto o jogador não apertar 
            #a aula, quando ele apertar
            
            
            #mostrar a lista de arquivos
            replist = os.listdir(savepath)            
            if live_data is not None:
                if ( (live_data[0][2]>=2000) and (live_data[0][2]<=3000)):
                    #desenhar um botão pra cima, um pra baixo e o do centro
                    #botão "pra cima"
                    rep_up_button_points = [rep_button.button_points[0]+55,rep_button.button_points[1]-25,50,20]
                    rep_up_button.visible = True
                    rep_up_button = DrawButton(rep_up_button, rep_up_button_points ,hand_points,hand_state, myfont, screen)


                    #botão "Aula"
                    rep_aula_button.text = "A-"+str(repidx)
                    rep_aula_button_points = [rep_button.button_points[0]+55,rep_button.button_points[1],50,20]
                    rep_aula_button.visible = True
                    rep_aula_button = DrawButton(rep_aula_button, rep_aula_button_points ,hand_points,hand_state, myfont, screen)

                    #botão "pra baixo"
                    rep_down_button_points = [rep_button.button_points[0]+55,rep_button.button_points[1]+25,50,20]
                    rep_down_button.visible = True
                    rep_down_button = DrawButton(rep_down_button, rep_down_button_points ,hand_points,hand_state, myfont, screen)

                    #checar se o butão up foi ativado
                    if rep_up_button.state==3:
                        if repidx > 0:
                            repidx-=1
                            frame = 0
                            db_file=None


                    #checar se o butão down foi ativado
                    if rep_down_button.state==3:
                        if repidx < len(replist)-1:
                            repidx+=1
                            frame=0
                            db_file=None
                            
                    #TODO a reprodução só vai inicializar após apertar o botão
                    if rep_aula_button.state==3:
                        if repidx < len(replist):
                            play=True
            #uma rodada de demonstração e outra com o jogo rodando
            #carregar o arquivo do banco de dados
            if db_file is None:
                #carregar os dados

                #carregar o primeiro arquivo apenas para teste
                data=load_recorded_data.get_data(savepath+replist[repidx])

                #TODO no futuro será o dado pelo arquivo selecionado
                db_file = ""
                #print("idx=",repidx,"::::",savepath+replist[repidx])
                #print(data)
                rec_frame=0
            elif not play: 
                 body_draw.draw_recorded_body(data, screen, (0,255,255), line_size, rec_frame)
                 rec_frame+=1
                 if len(data[0])-75<=rec_frame:
                     rec_frame=0

            elif play:
                body_draw.draw_recorded_body(data, screen, (0,255,255), line_size, frame)


                cotovelo=[data[9][frame][0],data[9][frame][1],data[9][frame][2]]
                punho = [data[10][frame][0],data[10][frame][1],data[10][frame][2]]

                new_k = find_k(frame,cotovelo,punho)
                if not np.isnan(new_k):
                    k=new_k
                
                #compara os angulos
                ang_matriz=JointsCompare.JointsCompare(data,live_data,frame,k)
                
                if ang_matriz is not None or not numpy.isnan(ang_matriz).any():
                    #desenha o angulo do cotovelo direito rec
                    ShowMessage(int(ang_matriz[0][2]),myfont,screen,[data[9][frame][0]+10,data[9][frame][1]],(255,255,0))
                    #desenha o angulo do cotovelo esquerdo rec
                    ShowMessage(int(ang_matriz[1][2]),myfont,screen,[data[5][frame][0]-40,data[5][frame][1]],(255,255,0))
                    #desenha o angulo do joelho direito rec
                    ShowMessage(int(ang_matriz[2][2]),myfont,screen,[data[17][frame][0]+10,data[17][frame][1]],(255,255,0))
                    #desenha o angulo do joelho esquerdo rec
                    ShowMessage(int(ang_matriz[3][2]),myfont,screen,[data[13][frame][0]-40,data[13][frame][1]],(255,255,0))
                    
                    
                    #desenha os angulos no corpo do jogador                 
                    #desenha o angulo do cotovelo direito live
                    ang_color = ang_colors(ang_matriz,0,erro)
                    ShowMessage(int(ang_matriz[0][1]),myfont,screen,[live_data[9][0]+10+kinect_width,live_data[9][1]],ang_color)
                    #desenha o angulo do cotovelo esquerdo live
                    ang_color = ang_colors(ang_matriz,1,erro)
                    ShowMessage(int(ang_matriz[1][1]),myfont,screen,[live_data[5][0]-40+kinect_width,live_data[5][1]],ang_color)
                    #desenha o angulo do joelho direito live
                    ang_color = ang_colors(ang_matriz,2,erro)
                    ShowMessage(int(ang_matriz[2][1]),myfont,screen,[live_data[17][0]+10+kinect_width,live_data[17][1]],ang_color)
                    #desenha o angulo do joelho esquerdo live
                    ang_color = ang_colors(ang_matriz,3,erro)
                    ShowMessage(int(ang_matriz[3][1]),myfont,screen,[live_data[13][0]-40+kinect_width,live_data[13][1]],ang_color)
                    
                frame = AnguloAlvo(ang_matriz,0.1,fps,frame,erro) 
                #frame+=1
            #exclui os ultimos 3 segundos de frames (tempo para
            #apertar o botão de parar a gravação)
            if len(data[0])-75<=frame:
                play = False
                frame=0

        else:
            db_file = None
            frame = 0


        #gravar sequencia de movimentos
        if rec_button.on_off:
            if(start_rec_time >=0):
                start_rec_time = start_rec_time-millseconds/1000            
                #fazer a contagem de tempo
                ShowMessage(int(start_rec_time),bcfont,screen,[kinect_width/2,10],(255,255,0))
            else:
                #desenhar um quadrado vermelho informando que está gravando
                pygame.draw.rect(screen,(255,0,0),[width-30,height-30,20,20])
                                        
                #fazer a contagem de tempo
                ShowMessage(int(rec_time),bcfont,screen,[kinect_width+kinect_width/2,10],(255,255,0))
                rec_time = rec_time+millseconds/1000  
                #iniciar o arquivo
                if (not rec_inicializada):
                    #escrever o nome das colunas
                    cName=[]
                    for jointName in [row[0] for row in BODY_LIST]:
                        cName.append(jointName+"_x")
                        cName.append(jointName+"_y")
                        cName.append(jointName+"_z")
    
                    #escrever o arquivo
                    now=dt.datetime.now()
                    filename = "kinect_data_"+now.strftime("%Y-%m-%d_%H-%M-%S")+".csv"
                    WriteFile(savepath+filename,cName,'w')
                    rec_inicializada = True
                #arquivo já inicializado, acionar os dados
                else:
                    #se tiver algo nos dados
                    rec_dados = []
                    if (live_data != None):
                        for idx1 in range(0,25):
                            for idx2 in range(0,3):
                                rec_dados.append(str(live_data[idx1][idx2]))
    
                    WriteFile(savepath+filename,rec_dados,'a')
        else:
            rec_inicializada = False
            start_rec_time = 4
            rec_time = 0


        #espera um tempo até o proximo frame
        pygame.time.wait(millseconds)

        #atualiza a tela
        pygame.display.flip()

main()
pygame.quit()
quit()

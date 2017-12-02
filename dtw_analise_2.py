# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:53:13 2017

@author: aluno
"""

# carregar os dois dados
import load_recorded_data
from dtw import dtw
import numpy as np
import junta
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#################################
def find_k(cotovelo,punho):
    D = 25

    x0p=cotovelo[0]#df['ElbowRight_x'].values[frame]
    y0p=cotovelo[1]#df['ElbowRight_y'].values[frame]
    z0p=cotovelo[2]/10#df['ElbowRight_z'].values[frame]/10

    x1p=punho[0]#df['WristRight_x'].values[frame]
    y1p=punho[1]#df['WristRight_y'].values[frame]
    z1p=punho[2]/10#df['WristRight_z'].values[frame]/10

    dx = x1p - x0p
    dy = y1p - y0p
    dz = z1p - z0p

    k=((D**2-dz**2)/(dx**2+dy**2))**0.5

    return k
#####################################


aluno_path="C:\\Users\\Lucas\\Documents\\TCC\Lucas TCC-30-10\\Lucas TCC\\ResultDataBase\\"
mestre_path="C:\\Users\\Lucas\\Documents\TCC\\Lucas TCC-30-10\\Lucas TCC\\DataBase\\"

aluno_file="teste123.csv.csv"
mestre_file="kinectData_4-5-6_2017-10-16_18-07-52.csv"
data_aluno = load_recorded_data.get_data(aluno_path+aluno_file)
data_mestre = load_recorded_data.get_data(mestre_path+mestre_file)

#destrinchar o nome dos arquivos para pegar as juntas 
joints_vector =  mestre_file.split('_')
joints_vector = joints_vector[1].split('-')
joints_vector = np.array([int(joints_vector[0]), int(joints_vector[1]), int(joints_vector[2])])



#fazer o vetor de angulos
#calcular o vetor de angulos do aluno
len(data_aluno[0])
#inicializando os vetores
ang_aluno = np.zeros([len(data_aluno[0])])
ang_mestre = np.zeros([len(data_mestre[0])])


##mestre
k=1
for frame in range(0,ang_mestre.size):
    
    #achar o valor de k
    cotovelo=[data_mestre[9][frame][0],data_mestre[9][frame][1],data_mestre[9][frame][2]]
    punho = [data_mestre[10][frame][0],data_mestre[10][frame][1],data_mestre[10][frame][2]]
    new_k = find_k(cotovelo,punho)
    if not np.isnan(new_k):
        k=new_k
    
    j0 = junta.Junta(data_mestre[joints_vector[0]][frame][0]*k,data_mestre[joints_vector[0]][frame][1]*k,data_mestre[joints_vector[0]][frame][2]/10)
    j1 = junta.Junta(data_mestre[joints_vector[1]][frame][0]*k,data_mestre[joints_vector[1]][frame][1]*k,data_mestre[joints_vector[1]][frame][2]/10)
    j2 = junta.Junta(data_mestre[joints_vector[2]][frame][0]*k,data_mestre[joints_vector[2]][frame][1]*k,data_mestre[joints_vector[2]][frame][2]/10)
        
    #print ("a1=",j1_live.getMemberMemberAngle(j0_live,j2_live)," a2= ",j1_rec.getMemberMemberAngle(j0_rec,j2_rec))
    ang_mestre[frame] = j1.getMemberMemberAngle(j0,j2)
    

##aluno    
for frame in range(0,ang_aluno.size):
    
    #achar o valor de k
    cotovelo=[data_aluno[9][frame][0],data_aluno[9][frame][1],data_aluno[9][frame][2]]
    punho = [data_aluno[10][frame][0],data_aluno[10][frame][1],data_aluno[10][frame][2]]
    new_k = find_k(cotovelo,punho)
    if not np.isnan(new_k):
        k=new_k
    
    j0 = junta.Junta(data_aluno[joints_vector[0]][frame][0]*k,data_aluno[joints_vector[0]][frame][1]*k,data_aluno[joints_vector[0]][frame][2]/10)
    j1 = junta.Junta(data_aluno[joints_vector[1]][frame][0]*k,data_aluno[joints_vector[1]][frame][1]*k,data_aluno[joints_vector[1]][frame][2]/10)
    j2 = junta.Junta(data_aluno[joints_vector[2]][frame][0]*k,data_aluno[joints_vector[2]][frame][1]*k,data_aluno[joints_vector[2]][frame][2]/10)
        
    #print ("a1=",j1_live.getMemberMemberAngle(j0_live,j2_live)," a2= ",j1_rec.getMemberMemberAngle(j0_rec,j2_rec))
    ang_aluno[frame] = j1.getMemberMemberAngle(j0,j2)
    
#usar o dtw

x=ang_aluno
y=ang_mestre[:-75]

#plotar os dois angulos
fig_ang = plt.figure()
ax_ang_aluno = fig_ang.add_subplot(211)
ax_ang_mestre = fig_ang.add_subplot(212)

ax_ang_aluno.plot(list(range(0,x.size)), x)
ax_ang_mestre.plot(list(range(0,y.size)), y)
ax_ang_aluno.set_ylabel('Ângulo do jogador (º)') 
ax_ang_mestre.set_ylabel('Ângulo do arquivo (º)')
ax_ang_mestre.set_xlabel('Amostra')

ax_ang_aluno.set_title('Ângulos gerados \n',fontweight='bold',fontsize=14)

dist, cost, acc, path = dtw(x, y, dist=euclidean)

fig_dtw = plt.figure()
ax_dtw = plt.subplot(111)
box_dtw = ax_dtw.get_position()

ax_dtw.imshow(acc.T, origin='lower', cmap=cm.gray, interpolation='nearest')
ax_dtw.plot(path[0], path[1], 'w')
ax_dtw.set_xlabel('Amostra jogador') 
ax_dtw.set_ylabel('Amostra arquivo')

ax_dtw.set_title('Caminho entre os angulos gerado pelo DTW \n',fontweight='bold',fontsize=14)

for item in ([ax_dtw.xaxis.label, ax_dtw.yaxis.label] +
             ax_dtw.get_xticklabels() + ax_dtw.get_yticklabels()):
    item.set_fontsize(12)
    
for item in ([ax_ang_aluno.xaxis.label, ax_ang_aluno.yaxis.label] +
             ax_ang_aluno.get_xticklabels() + ax_ang_aluno.get_yticklabels()):
    item.set_fontsize(12)
    
for item in ([ax_ang_mestre.xaxis.label, ax_ang_mestre.yaxis.label] +
             ax_ang_mestre.get_xticklabels() + ax_ang_mestre.get_yticklabels()):
    item.set_fontsize(12)

plt.xlim((-0.5, acc.shape[0]-0.5))
plt.ylim((-0.5, acc.shape[1]-0.5))

#load_recorded_data
'''
out = data[lista das partes][linha][x,y,z]
'''
import pandas as pd

def get_data(filepath):
    df = pd.read_csv(filepath)
    jointpoints = []
    cont=0
    for part in range(0,25):
        jointpoints.append( df.iloc[:, [cont, cont+1, cont+2]].values)     
        cont+=3
    return jointpoints

#filepath="C:\\Users\\Lucas\\Documents\\TCC\\take_kinect_data\\kinect_data_2017-08-17_17-4-9.csv"
#teste=get_data(filepath)
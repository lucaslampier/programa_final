from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime

#import sys
import numpy as np
#import datetime

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

def name_cols(B_LIST):
    cName=[]
    for jointName in [row[0] for row in B_LIST]:
        cName.append(jointName+"_x")
        cName.append(jointName+"_y")
        cName.append(jointName+"_z")
    return cName

c_names = name_cols(BODY_LIST)

#def WriteFile(filename,List,mode):
#    file = open(filename, mode)
#    for joint in List:
#        for idx,item in enumerate(joint):
#            if idx==len(List)-1:
#                file.write(str(item))
#            else:
#                file.write(str(item) + ",")
#    file.write("\n")
#    file.close()

class Body_Position(object):
    def __init__(self):
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Depth | PyKinectV2.FrameSourceTypes_Body)

        self._bodies = None
        self.save=False
        

    def take_body_xyz(self,jointPoints, depth_frame,L_hand_state,R_hand_state):        
        data=[]
        for joint in BODY_LIST:
            
            if abs(jointPoints[joint[1]].x) != float("inf") or abs(jointPoints[joint[1]].y) != float("inf"):
                x = jointPoints[joint[1]].x
                y = jointPoints[joint[1]].y

                if (abs(round(y) * 512 + round(x)) <= 512*424):
                    z = depth_frame[(round(y) * 512 + round(x)) ]
                    data.append([round (x),round(y),z])
                    
                else:
                    x=-1
                    y=-1
                    z=-1
                    data.append([x,y,z])
        #print(data)
        #
        #Definir qundo salvare onde salvar
        #
        #WriteFile("Teste.csv",data,'a')
        data.append([L_hand_state,R_hand_state])
        return data 
                
    
    def take_matrix(self):        
        # --- verificar se possui um novo frame
        if self._kinect.has_new_depth_frame():
            frame = self._kinect.get_last_depth_frame()
            
            # --- Cool! We have a body frame, so can get skeletons
            if self._kinect.has_new_body_frame(): 
                self._bodies = self._kinect.get_last_body_frame()
            
                # --- draw skeletons to _frame_surface
                if self._bodies is not None: 
                    for i in range(0, self._kinect.max_body_count):
                    #for i in range(0, 1):
                        body = self._bodies.bodies[i]                        
                        if not body.is_tracked: 
                            continue 
                        
                        joints = body.joints 
                        # convert joint coordinates to depth space                         
                        joint_points = self._kinect.body_joints_to_depth_space(joints)
                        
                        L_hand_state = -1
                        R_hand_state = -1
                        if body.is_tracked == True:
                            L_hand_state = body.hand_left_state
                            R_hand_state = body.hand_right_state
                            #print(body.hand_right_state )
                        data = self.take_body_xyz(joint_points, frame,L_hand_state,R_hand_state)
                                                    
                        return data
                
                else:
                    return None
            
            else:
                return None
            
        else:
            return None
        
    

        
        


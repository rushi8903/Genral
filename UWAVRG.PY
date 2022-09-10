import cv2 
import mediapipe as mp
import math
mphands = mp.solutions.hands
hands = mphands.Hands()
mpDraw = mp.solutions.drawing_utils


from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume.iid, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.GetMute()
volume.GetMasterVolumeLevel()
volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-20.0, None)


camera = cv2.VideoCapture(0)

while True :
    ret,img = camera.read()
    imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handslms in results.multi_hand_landmarks:
            for id , lm in enumerate(handslms.landmark):
                h, w, c =img.shape
                cx, cy = int(lm.x *w) , int(lm.y*h)

                if id == 4:
                    x1,y1 = cx,cy 
                if id == 8:
                    x2,y2 = cx,cy       
                if id == 4 or id == 8:
                    cv2.circle(img,(x1,x2),15, (255,0,255),cv2.FILLED)
                
                   
                
            mpDraw.draw_landmarks(img,handslms,mphands.HAND_CONNECTIONS) 






    cv2.imshow("camera",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 
    cv2.destroyAllWindows()
    camera.release()

    
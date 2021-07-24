import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller

keyboard = Controller()

cap = cv2.VideoCapture(0)
cap.set(3, 640)
h, w = 480, 640

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils


while(True):
    success, img = cap.read()
    imgResult = cv2.flip(img,1)
    
    imgRGB = cv2.cvtColor(imgResult, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for ids, lm in enumerate(handlms.landmark):
                #print(ids,lm)
                cx, cy = int(lm.x*w),int(lm.y*h)
                #print(ids, cx, cy)
                if ids == 9:
                    #cv2.circle(imgResult, (cx,cy), 25, (255,0,255), cv2.FILLED)
                    try:
                        if cx < 210:
                            if cy < 160:
                                #cv2.putText(imgResult,"LEFT-TOP",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2

                                
                                keyboard.press(Key.up)
                                keyboard.press(Key.left)
                                keyboard.release(Key.up)
                                keyboard.release(Key.left)
                                
                            elif cy>=160 and cy < 320:
                                keyboard.press(Key.left)
                                keyboard.release(Key.left)
                            #cv2.putText(imgResult,"LEFT",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                            else:
                                keyboard.press(Key.down)
                                keyboard.press(Key.left)
                                keyboard.release(Key.down)
                                keyboard.release(Key.left)
                                #cv2.putText(imgResult,"LEFT-BOTTOM",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
            
                        elif cx >= 210 and cx < 430:
                            if cy < 160:
                                keyboard.press(Key.up)
                                keyboard.release(Key.up)
                                
                                #cv2.putText(imgResult,"TOP",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                            elif cy>=160 and cy < 320:
                                pass
                                #cv2.putText(imgResult,"IDLE-CENTER",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                            else:
                                keyboard.press(Key.down)
                                keyboard.release(Key.down)
                                #cv2.putText(imgResult,"BOTTOM",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                    
                        else:
                            if cy < 160:
                                keyboard.press(Key.up)
                                keyboard.press(Key.right)
                                keyboard.release(Key.up)
                                keyboard.release(Key.right)
                                #cv2.putText(imgResult,"TOP-RIGHT",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                            elif cy>=160 and cy < 320:
                                keyboard.press(Key.right)
                                keyboard.release(Key.right)
                                #cv2.putText(imgResult,"RIGHT",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                            else:
                                keyboard.press(Key.down)
                                keyboard.press(Key.right)
                                keyboard.release(Key.down)
                                keyboard.release(Key.right)
                                #cv2.putText(imgResult,"BOTTOM-RIGHT",(280,220), cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
                    except:
                        pass
                            
                        
            mpDraw.draw_landmarks(imgResult, handlms )
    
    #Drawing the boxes on output window to help user
    
    # Forward-Left |  Forward  | Forward-Right
    # -------------|-----------|--------------
    #     Left     |   Idle    |    Right
    # -------------|-----------|--------------
    # Backward-left|  Backward | Backard-Right
  
    cv2.line(imgResult, (210,0), (210,480), (200,190,0), 2)
    cv2.line(imgResult, (430,0), (430,480), (200,190,0), 2)
    cv2.line(imgResult, (0,160), (640,160), (200,190,0), 2)
    cv2.line(imgResult, (0,320), (640,320), (200,190,0), 2)
    
    # Output window
    cv2.imshow("Video", imgResult)
    cv2.waitKey(1)


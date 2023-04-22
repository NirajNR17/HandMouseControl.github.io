import cv2
import time
import mediapipe as mp
import pyautogui
import pydirectinput
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

# Define the position and size of the blocks
scaling_factor = 5
block_width = int(screen_width / 10) * scaling_factor
block_height = int(screen_height / 10) * scaling_factor
left_block_x = int(screen_width / 5) - block_width
left_block_y = int(screen_height / 2) - int(block_height / 2)
right_block_x = int(screen_width * 4 / 5)
right_block_y = int(screen_height / 2) - int(block_height / 2)
top_block_x = int(screen_width / 2) - int(block_width / 2)
top_block_y = int(screen_height / 5) - block_height
bottom_block_x = int(screen_width / 2) - int(block_width / 2)
bottom_block_y = int(screen_height * 4 / 5)


while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    # Draw the four blocks on the frame
    #up
    cv2.rectangle(frame,(180,20),(480,100), (0, 255, 0), 1)
    #Leftblock
    cv2.rectangle(frame,(20,138),(150,380), (0, 255, 0), 1)
    #rightblock
    cv2.rectangle(frame,(500,138),(630,380), (0, 255, 0), 1)
    #down
    cv2.rectangle(frame,(180,400),(480,480), (0, 255, 0), 1)


    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x=int(landmark.x*frame_width)
                y=int(landmark.y*frame_height)
                if id==8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x, index_y)

                    # Check if the index finger is on top of a block and press the corresponding key
                    if left_block_x < index_x < left_block_x + block_width and left_block_y < index_y < left_block_y + block_height:
                        # pyautogui.press('left')
                        # pydirectinput.press('left')
                        pydirectinput.keyDown('left')
                        time.sleep(1)  # hold the left key for 1 second
                        pydirectinput.keyUp('left')
                        print('left')
                    elif right_block_x < index_x < right_block_x + block_width and right_block_y < index_y < right_block_y + block_height:
                        # pyautogui.press('right')
                        # pydirectinput.press('right')
                        pydirectinput.keyDown('right')
                        time.sleep(1)  # hold the left key for 1 second
                        pydirectinput.keyUp('right')
                        print('right')
                    elif top_block_x < index_x < top_block_x + block_width and top_block_y < index_y < top_block_y + block_height:
                        # pyautogui.press('up')
                        # pydirectinput.press('up')
                        pydirectinput.keyDown('up')
                        time.sleep(1)  # hold the left key for 1 second
                        pydirectinput.keyUp('up')
                        print('up')
                    elif bottom_block_x < index_x < bottom_block_x + block_width and bottom_block_y < index_y < bottom_block_y + block_height:
                        # pyautogui.press('down')
                        # pydirectinput.press('down')
                        pydirectinput.keyDown('down')
                        time.sleep(1)  # hold the left key for 1 second
                        pydirectinput.keyUp('down')
                        print('down')
                    

                if id==12:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    mid_x = screen_width/frame_width*x
                    mid_y = screen_height/frame_height*y
                    print('outside', abs(index_y - mid_y))
                    if abs(mid_y - index_y) < 10:
                        print('click')
                        pyautogui.doubleClick()
                        pyautogui.sleep(1)
                if id==4: 
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,255))
                    thumb_x= screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    if abs(thumb_y - index_y) < 10:
                        print('rightclick')
                        pyautogui.rightClick()
                        pyautogui.sleep(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
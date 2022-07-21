from keras.models import load_model
import cv2
import numpy as np
from random import choice
import sys
import tensorflow as tf
import os
import warnings
import logging
warnings.filterwarnings("ignore", message=r"Passing", category=FutureWarning)
warnings.filterwarnings("ignore")
logging.getLogger('tensorflow').disabled = True
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.get_logger().setLevel('ERROR')
import time
REV_CLASS_MAP_RPS = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

REV_CLASS_MAP_OE = {
    0:"odd",
    1:"even",
    2:"none"
}
def mapper_rps(val):
    return REV_CLASS_MAP_RPS[val]
def mapper_oe(val):
    return REV_CLASS_MAP_OE[val]

def calculate_winner_rps(move1, move2):
    if move1 == move2:
        return "Tie"

    if move1 == "rock":
        if move2 == "scissors":
            return "User"
        if move2 == "paper":
            return "Computer"

    if move1 == "paper":
        if move2 == "rock":
            return "User"
        if move2 == "scissors":
            return "Computer"

    if move1 == "scissors":
        if move2 == "paper":
            return "User"
        if move2 == "rock":
            return "Computer"

def calculate_winner_oe(move1, move2, player_choice):
    if move1 == move2 and player_choice == "even":
        return "User"
    elif move1 == move2 and player_choice == "odd":
        return "Computer"
    elif move1 != move2 and player_choice == "even":
        return "Computer"
    else:
        return "User"


def play_rps():
    model = load_model("rock-paper-scissors-model.h5")

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    computer_score = 0
    user_score = 0
    prev_move = None
    # This the ROI size, the size of images saved will be box_size -10
    box_size = 234
    # Getting the width of the frame from the camera properties
    width = int(cap.get(3))
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        #exit(frame.shape)
        if not ret:
            continue
        # rectangle for user to play
        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)
        # rectangle for computer to play
        cv2.rectangle(frame, (box_size, 0), (0, box_size), (0, 250, 150), 2)

        # extract the region of image within the user rectangle
        roi = frame[5: box_size - 5, width - box_size + 5: width - 5]
        img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (227, 227))

        # predict the move made
        pred = model.predict(np.array([img]))
        move_code = np.argmax(pred[0])
        user_move_name = mapper_rps(move_code)
        # predict the winner (human vs computer)
        if prev_move != user_move_name:
            if user_move_name != "none":
                computer_move_name = choice(['rock', 'paper', 'scissors'])
                winner = calculate_winner_rps(user_move_name, computer_move_name)
                if winner == 'User':
                    user_score += 1
                elif winner == 'Computer':
                    computer_score += 1
            else:
                computer_move_name = "none"
                winner = "Waiting..."
        prev_move = user_move_name

        # display the information
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Your Move: " + user_move_name,(width-box_size, box_size+25), font, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Computer's Move: " + computer_move_name,(0, box_size+25), font, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "Winner: " + winner,(width//2 - box_size//2, box_size*2), font, 1, (0, 0, 255), 4, cv2.LINE_AA)
        cv2.putText(frame, "Score: " + str(computer_score) + " - " + str(user_score),
                    (width // 2 - box_size // 2, box_size + 150), font, 1, (0, 165, 255), 4, cv2.LINE_AA)
        if computer_move_name != "none":

            icon = cv2.imread(
                "images/{}.png".format(computer_move_name))
            icon = cv2.resize(icon, (box_size, box_size))
            frame[0: box_size, 0: box_size] = icon
        cv2.imshow("Rock Paper Scissors", frame)

        k = cv2.waitKey(10)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def play_oe():
    model = load_model("odd-even-model.h5")
    computer_score = 0
    user_score = 0
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1200)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    prev_move = None
    # This the ROI size, the size of images saved will be box_size -10
    box_size = 234
    # Getting the width of the frame from the camera properties
    width = int(cap.get(3))
    flag = True
    player_choice = ""
    fps = cv2.CAP_PROP_FPS

    counter=0
    gametime = 3
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        font = cv2.FONT_HERSHEY_SIMPLEX

        if not ret:
            continue
        while flag:
            print("Enter 'e' to choose even or enter 'o' to choose odd.")
            k = input()
            # If user press 'o' then class_name is set to odd and trigger set to True
            if k == 'e':
                player_choice = "even"
                flag = False
            elif k == 'o':
                player_choice = "odd"
                flag = False


        # rectangle for user to play
        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)
        # rectangle for computer to play
        cv2.rectangle(frame, (box_size, 0), (0, box_size), (0, 250, 150), 2)

        # extract the region of image within the user rectangle
        roi = frame[5: box_size - 5, width - box_size + 5: width - 5]
        img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (227, 227))

        # predict the move made
        pred = model.predict(np.array([img]))
        move_code = np.argmax(pred[0])
        user_move_name = mapper_oe(move_code)
        # predict the winner (human vs computer)
        if prev_move != user_move_name:
            if user_move_name != "none":
                computer_move_name = choice(['odd', 'even'])
                winner = calculate_winner_oe(user_move_name, computer_move_name, player_choice)
                if winner == 'User':
                    user_score += 1
                elif winner == 'Computer':
                    computer_score += 1
            else:
                computer_move_name = "none"
                winner = "Waiting..."
        prev_move = user_move_name

        # display the information

        cv2.putText(frame, "Your Move: " + user_move_name, (width - box_size, box_size + 25), font, 0.7, (255, 0, 0), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, "Computer's Move: " + computer_move_name, (0, box_size + 25), font, 0.7, (255, 0, 0), 2,
                    cv2.LINE_AA)
        cv2.putText(frame, "Winner: " + winner, (width // 2 - box_size // 2, box_size * 2), font, 1, (0, 0, 255), 4,
                    cv2.LINE_AA)
        cv2.putText(frame, "Score: " + str(computer_score) + " - " + str(user_score),
                    (width // 2 - box_size // 2, box_size + 150), font, 1, (0, 165, 255), 4, cv2.LINE_AA)
        if computer_move_name != "none":
            icon = cv2.imread("images/{}.png".format(computer_move_name))
            icon = cv2.resize(icon, (box_size, box_size))
            frame[0: box_size, 0: box_size] = icon
        cv2.imshow("Odd or Even", frame)

        k = cv2.waitKey(10)
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Arguments Error: Format is  play.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)
    elif sys.argv[1] == "rps":
        play_rps()
    elif sys.argv[1] == "oe":
        play_oe()
    else:
        print("Arguments Error: Format is  train.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)

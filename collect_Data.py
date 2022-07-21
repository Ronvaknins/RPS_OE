import os
import cv2
import sys

def gather_data_rps(num_samples):
    # Initialize the camera
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # trigger tells us when to start recording
    trigger = False
    # This the ROI size, the size of images saved will be box_size -10
    box_size = 234
    # Getting the width of the frame from the camera properties
    width = int(cap.get(3))
    rockcounter = 0
    scissorcounter = 0
    papercounter = 0
    nothingcounter = 0
    while True:
        # Read frame by frame
        ret, frame = cap.read()
        # Flip the frame laterally
        frame = cv2.flip(frame, 1)
        # Break the loop if there is trouble reading the frame.
        if not ret:
            break
        # Define ROI for capturing samples
        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)
        # Make a resizable window.
        cv2.namedWindow("Collecting images", cv2.WINDOW_NORMAL)
        # If trigger is True than start capturing the samples
        if trigger:
            # Grab only slected roi
            roi = frame[5: box_size - 5, width - box_size + 5: width - 5]
            # Append the roi and class name to the list with the selected class_name
            #eval(class_name).append([roi, class_name])
            if class_name == 'rock' and rockcounter <= num_samples:
                cv2.imwrite('image_data//rps//rock//{0}.jpg'.format(rockcounter),roi)
                text = "Collected Samples of {}: {}".format(class_name, rockcounter)
                rockcounter+=1
                if rockcounter == num_samples:
                    trigger = not trigger
            elif class_name == 'paper' and papercounter <= num_samples:
                cv2.imwrite('image_data//rps//paper//{0}.jpg'.format(papercounter),roi)
                text = "Collected Samples of {}: {}".format(class_name, papercounter)
                papercounter+=1
                if papercounter == num_samples:
                    trigger = not trigger
            elif class_name == 'scissors' and scissorcounter <= num_samples:
                cv2.imwrite('image_data//rps//scissors//{0}.jpg'.format(scissorcounter),roi)
                text = "Collected Samples of {}: {}".format(class_name, scissorcounter)
                scissorcounter+=1
                if scissorcounter == num_samples:
                    trigger = not trigger
            elif class_name == 'none' and nothingcounter <= num_samples:
                cv2.imwrite('image_data//rps//none//{0}.jpg'.format(nothingcounter), roi)
                text = "Collected Samples of {}: {}".format(class_name, nothingcounter)
                nothingcounter += 1
                if nothingcounter == num_samples:
                    trigger = not trigger
        else:
            text = "Press 'r' to collect rock samples, 'p' for paper, 's' for scissors, 'n' for nothing and 'q'  to finish"
        # Show the counter on the imaege
        cv2.putText(frame, text, (3, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.56, (0, 0, 255), 1, cv2.LINE_AA)
        # Display the window
        cv2.imshow("Collecting images", frame)
        # Wait 1 ms
        k = cv2.waitKey(1)
        # If user press 'r' than set the path for rock directoryq
        if k == ord('r'):
            # Trigger the variable inorder to capture the samples
            trigger = not trigger
            class_name = 'rock'
        # If user press 'p' then class_name is set to paper and trigger set to True
        if k == ord('p'):
            trigger = not trigger
            class_name = 'paper'
        # If user press 's' then class_name is set to scissor and trigger set to True
        if k == ord('s'):
            trigger = not trigger
            class_name = 'scissors'
        # If user press 's' then class_name is set to nothing and trigger set to True
        if k == ord('n'):
            trigger = not trigger
            class_name = 'none'
        # Exit if user presses 'q'
        if k == ord('q'):
            break
    #  Release the camera and destroy the window
    cap.release()
    cv2.destroyAllWindows()

def gather_data_oe(num_samples):
    # Initialize the camera
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    # trigger tells us when to start recording
    trigger = False
    # This the ROI size, the size of images saved will be box_size -10
    box_size = 234
    # Getting the width of the frame from the camera properties
    width = int(cap.get(3))
    oddcounter = 0
    evencounter = 0
    nonecounter = 0
    while True:
        # Read frame by frame
        ret, frame = cap.read()
        # Flip the frame laterally
        frame = cv2.flip(frame, 1)
        # Break the loop if there is trouble reading the frame.
        if not ret:
            break
        # Define ROI for capturing samples
        cv2.rectangle(frame, (width - box_size, 0), (width, box_size), (0, 250, 150), 2)
        # Make a resizable window.
        cv2.namedWindow("Collecting images", cv2.WINDOW_NORMAL)
        # If trigger is True than start capturing the samples
        if trigger:
            # Grab only slected roi
            roi = frame[5: box_size - 5, width - box_size + 5: width - 5]
            # Append the roi and class name to the list with the selected class_name
            #eval(class_name).append([roi, class_name])
            if class_name == 'odd' and oddcounter <= num_samples:
                cv2.imwrite('image_data//oe//odd//{0}.jpg'.format(oddcounter),roi)
                text = "Collected Samples of {}: {}".format(class_name, oddcounter)
                oddcounter+=1
                if oddcounter == num_samples:
                    trigger = not trigger
            elif class_name == 'even' and evencounter <= num_samples:
                cv2.imwrite('image_data//oe//even//{0}.jpg'.format(evencounter),roi)
                text = "Collected Samples of {}: {}".format(class_name, evencounter)
                evencounter+=1
                if evencounter == num_samples:
                    trigger = not trigger
            elif class_name == 'none' and nonecounter <= num_samples:
                cv2.imwrite('image_data//oe//none//{0}.jpg'.format(nonecounter), roi)
                text = "Collected Samples of {}: {}".format(class_name, nonecounter)
                nonecounter += 1
                if nonecounter == num_samples:
                    trigger = not trigger
        else:
            text = "Press 'o' to collect odd samples, 'e' for even, 'n' for none, 'q' to finish"
        # Show the counter on the imaege
        cv2.putText(frame, text, (3, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.56, (0, 0, 255), 1, cv2.LINE_AA)
        # Display the window
        cv2.imshow("Collecting images", frame)
        # Wait 1 ms
        k = cv2.waitKey(1)
        # If user press 'o' then class_name is set to odd and trigger set to True
        if k == ord('o'):
            trigger = not trigger
            class_name = 'odd'
        # If user press 's' then class_name is set to even and trigger set to True
        if k == ord('e'):
            trigger = not trigger
            class_name = 'even'
        # If user press 'n then class_name is set to none and trigger set to True
        if k == ord('n'):
            trigger = not trigger
            class_name = 'none'
        # Exit if user presses 'q'
        if k == ord('q'):
            break
    #  Release the camera and destroy the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    num_samples = 50
    try:
        os.mkdir('image_data')
    except FileExistsError:
        pass
    if len(sys.argv) != 2:
        print("Arguments Error: Format is collect_data.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)
    elif sys.argv[1] == "rps":
        try:
            os.mkdir('image_data//rps')
            os.mkdir('image_data//rps//rock')
            os.mkdir('image_data//rps//paper')
            os.mkdir('image_data//rps//scissors')
            os.mkdir('image_data//rps//none')
        except FileExistsError:
            pass
        gather_data_rps(num_samples)
    elif sys.argv[1] == "oe":
        try:
            os.mkdir('image_data//oe')
            os.mkdir('image_data//oe//odd')
            os.mkdir('image_data//oe//even')
            os.mkdir('image_data//oe//none')
        except FileExistsError:
            pass
        gather_data_oe(num_samples)
    else:
        print("Arguments Error: Format is collect_data.py {rps(rock paper scissors) or oe(odd even)}.")
        exit(0)

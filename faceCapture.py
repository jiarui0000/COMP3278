import cv2
import os

# input user_id to capture faces for that user_id

def faceCapture(user_id):

    faceCascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

    video_capture = cv2.VideoCapture(0)

    # Specify the `user_id` and `NUM_IMGS` here.
    NUM_IMGS = 50
    if not os.path.exists('data/{}'.format(user_id)):
        os.mkdir('data/{}'.format(user_id))

    cnt = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (80, 50)
    fontScale = 1
    fontColor = (102, 102, 225)
    lineType = 2

    # Open camera
    while cnt <= NUM_IMGS:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        """
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE,
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        msg = "Saving {}'s Face Data [{}/{}]".format(user_id, cnt, NUM_IMGS)
        cv2.putText(frame, msg,
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    lineType)
        """
        

        # Display the resulting frame
        cv2.imshow('Video', frame)
        # Store the captured images in `data/Jack`
        cv2.imwrite("data/{}/{}{:03d}.jpg".format(user_id, user_id, cnt), frame)
        cnt += 1

        key = cv2.waitKey(100)

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    user_id = "001"
    faceCapture(user_id)

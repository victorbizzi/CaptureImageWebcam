import cv2

def capture_webcam():
    #Start Webcam
    cap = cv2.VideoCapture(0)
    try:
        if not cap.isOpened():
            raise Exception("Error in Cam")

        ret, frame = cap.read()
        if not ret:
            raise Exception("Error in Frame.")

        filename = 'webcam.jpg'
        cv2.imwrite(filename, frame)
        print(f"Saved: '{filename}'.")

    except Exception as e:
        print("Error:", str(e))
        return str(e)

    finally:
        cap.release()
capture_webcam()
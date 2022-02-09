from atexit import register
import cv2
from pyzbar.pyzbar import decode
from warnings import filterwarnings
def decode_qr():
        filterwarnings('ignore')

       # Capture the video from default camera
        capture = cv2.VideoCapture(0)

        print("Escape Key (Esc) to exit...")
        print('--------------------------------------------------------------------------------------------\n')
        received_data = None
        while True:
            # reading frame from the camera
            _, frame = capture.read()
            # Decoding the QR Code
            decoded_data = decode(frame)
            try:
                data = decoded_data[0][0]
                if data != received_data:
                    received_data = data
                    return data
                    #break
            except:
                pass

            # Showing video.
            cv2.imshow("QR CODE Scanner", frame)

            # To exit press Esc Key.
            key = cv2.waitKey(1)
            if key == 27:
                break





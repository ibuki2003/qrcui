import cv2
import pyzbar.pyzbar

def read_qr(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    data = pyzbar.pyzbar.decode(gray)
    return data

def capture_qr(device_idx=0):
    try:
        cap = cv2.VideoCapture(device_idx)
    except e:
        raise "Capture device not found"
    while True:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        data = read_qr(frame)
        if len(data)!=0:
            cap.release() # Do not forget to release
            cv2.destroyAllWindows()
            return data
        if cv2.waitKey(1) == 27: # Esc
            break

    cap.release()
    cv2.destroyAllWindows()

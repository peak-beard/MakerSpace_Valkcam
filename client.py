import base64
import cv2
import zmq
import camera

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')



while True:
    try:

        encoded, buffer = cv2.imencode('.jpg', camera.gray)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
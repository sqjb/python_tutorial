import os.path

import cv2
import threading
import queue


def read_video(path: str, que: queue.Queue):
    cap = cv2.VideoCapture(path)
    while cap.isOpened():
        fp = cap.get(cv2.CAP_PROP_POS_FRAMES)
        _, f = cap.read()
        if f is None:
            break
        elif (fp % 25) == 0 and fp > 0:
            que.put_nowait(f)
            print("frame -> queue")
    cap.release()
    print("read video exit..")


def write_jpg(folder: str, que: queue.Queue):
    if not os.path.exists(folder):
        os.mkdir(folder)
    cnt = 0
    while True:
        frame = que.get(block=True, timeout=2)
        if frame is not None:
            cv2.imwrite(f"{folder}/{cnt}.jpg", frame)
            cnt += 1
            print("save frame")
        else:
            break
            print("no more frames within 2 seconds")
    print("write_jpg exit..")


if __name__ == '__main__':
    video_path = "./Megamind.avi"
    frame_folder = "./frames"
    Q = queue.Queue(maxsize=25)
    ths = [
        threading.Thread(target=read_video, args=(video_path, Q,)),
        threading.Thread(target=write_jpg, args=(frame_folder, Q,))
    ]
    [th.start() for th in ths]

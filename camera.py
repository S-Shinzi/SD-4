import cv2
import os

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:

        cap_cam = cv2.VideoCapture(1)
        ret, frame = cap.read()
        # 表示用(補助線あり)とキャプチャ用の画像を分ける
        edframe = frame
        # 補助線を引く
        cv2.rectangle(edframe, (120,116), (524,360),(0,0,255),3)
        # 表示
        cv2.imshow(window_name, edframe)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            # 画像切り抜き img[top : bottom, left : right]
            frame = frame[116 : 360, 120 : 524]

            # 切り抜いた画像を上下反転
            frame = cv2.rotate(frame, cv2.ROTATE_180)

            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')
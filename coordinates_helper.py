import imghdr
import os

import cv2


def coordinates_helper(src: str) -> None:
    def on_event_lbuttondown(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=2)
            cv2.putText(
                img,
                f"{x}, {y}",
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.0,
                (0, 0, 0),
                thickness=2,
            )
            cv2.imshow("image", img)

    img = cv2.imread(src)
    print(img.shape)

    cv2.namedWindow("image", 0)
    cv2.setMouseCallback("image", on_event_lbuttondown)
    while 1:
        cv2.imshow("image", img)
        if cv2.waitKey(0) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    img_path = ''
    assert os.path.isfile(img_path) and imghdr.what(img_path) in [
        "tiff",
        "jpeg",
        "bmp",
        "png",
    ]
    coordinates_helper(src=img_path)

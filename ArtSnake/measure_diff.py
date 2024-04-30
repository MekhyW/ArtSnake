import cv2

def measure_diff(img1, img2, show_diff=False):
    if img1.shape != img2.shape:
        img1 = cv2.resize(img1, (min(img1.shape[1], img2.shape[1]), min(img1.shape[0], img2.shape[0])))
        img2 = cv2.resize(img2, (min(img1.shape[1], img2.shape[1]), min(img1.shape[0], img2.shape[0])))
    subtracted = cv2.subtract(img1, img2)
    diff = sum(cv2.sumElems(subtracted))
    diff_norm = diff / (img1.shape[0] * img1.shape[1] * 255 * 3) * 100
    if show_diff:
        cv2.imshow('subtracted', subtracted)
        print(f'Difference: {diff_norm}%')
    return diff


if __name__ == '__main__':
    img1 = cv2.imread('image1.jpg')
    img2 = cv2.imread('image2.jpg')
    measure_diff(img1, img2, show_diff=True)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
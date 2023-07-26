import cv2
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def maincode():
    image_path='IMG_3758.jpg'
    img = cv2.imread(image_path)
    shape = img.shape
    color = (255,0,255)

    k=8
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.reshape((img.shape[0] * img.shape[1], 3))
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img)
    COLORS = kmeans.cluster_centers_
    COLORS = COLORS.astype(int)
    plt.figure(figsize=(25, 2))
    for domColor in range(k):
        plt.axis("off")
        plt.subplot(1, k, domColor + 1)
        plt.imshow([[COLORS[domColor]]])

    plt.axis("off")        
    plt.show()
    cv2.waitKey(0)



if __name__ == '__main__':
    maincode()

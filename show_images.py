import cv2
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
image_path = Path.home().joinpath('Desktop','chess board')


# reads image 'opencv-logo.png' as grayscale

for idx,image in enumerate(image_path.glob('*.jpeg')):
    print(f'{idx:02d} -> {image.name}')
    img = cv2.imread(str(image), cv2.IMREAD_COLOR)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig,axes = plt.subplots(1,3,figsize=(10,5))

    img3=np.swapaxes(img,0,2)
    img4=np.array([img3[2],img3[1],img3[0]])
    img5=img4.swapaxes(0,2)

    axes[0].imshow(img)
    axes[1].imshow(img2)
    axes[2].imshow(img5)
    plt.show()
    plt.close(fig)

    fig,axes = plt.subplots(1,3,figsize=(10,5))
    for aa in range(3):
        axes[aa].imshow(img2[:,:,aa],cmap='gray')
        axes[aa].set_title(f'Color channel #{aa}')
    plt.show()
    plt.close(fig)
    break


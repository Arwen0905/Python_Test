from sklearn import datasets
import matplotlib.pyplot as plt
digits = datasets.load_digits()
images_and_labels = list(zip(digits.images,digits.target))
for i,(image,label) in enumerate(images_and_labels[:8]):
    plt.subplot(2,4, i+1)
    plt.axis('off')
    plt.imshow(image,cmap=plt.cm.binary)
    plt.title('Training: '+str(label))
plt.show()
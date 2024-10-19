import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from base import MixedGaussian

def plot_clusters(gaussian:MixedGaussian,label='counts',s=15):
    plt.figure(figsize=(18,16))
    k = gaussian.K
    h = np.ceil(np.sqrt(k)).astype(int)
    w = np.ceil(k/h).astype(int)
    for i in range(gaussian.K):
        plt.subplot(h, w, i + 1)
        plt.scatter(gaussian.kernel.spatial[:,0],gaussian.kernel.spatial[:,1],marker = 's', c=gaussian.mean[:,i], cmap="viridis", s=s)
        plt.axis('equal')
        plt.gca().invert_yaxis()
        if label == 'counts':
            plt.title('{}'.format(np.sum(gaussian.labels==i)))
        else:
            plt.title('{}'.format(gaussian.pi[i]))
        plt.gcf().set_dpi(300)
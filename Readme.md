# SparseAEH

## About

A method to fasten the process of **automatic expression histology** in SpatialDE, especially 
effective in accomplishing the task of clustering high-dimensional gene expression dataset.

## Installation

```Shell
git clone https://github.com/jackywangtj66/SparseAEH.git
```

## Instruction
Input the spatial location and gene expression to get the cluster result.
``` python
import numpy as np

from base import MixedGaussian
from plot import plot_clusters
from FineST.utils import *        
from FineST.datasets import dataset

#adata_impt_all = dataset.CRC_FineST()
adata_impt_all = dataset.CRC_Original()
adata_impt_all.obsm['spatial'] = np.column_stack((np.array(adata_impt_all.obs['array_row']), np.array(adata_impt_all.obs['array_col'])))

gaussian_2 = MixedGaussian(adata_impt_all.obsm['spatial'],group_size=16,d=30,l=1e-5)
cluster_2 = gaussian_2.run_cluster(adata_impt_all.X.toarray(),3,iter=50,init_method='k_means') 
plot_clusters(gaussian_2)
```
More examples can be founded [here](https://github.com/jackywangtj66/NewDE)

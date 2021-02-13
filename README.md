# NMA Glasser surface plot with BrainSpace  
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/b0ae12bf07544a7b9cb870267fab24fd)](https://www.codacy.com/gh/rcruces/2020_NMA_surface-plot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=rcruces/2020_NMA_surface-plot&amp;utm_campaign=Badge_Grade)

## Python and BrainSpace installation ##
[BrainSpace](https://brainspace.readthedocs.io/en/latest/index.html)  
> `pip install brainspace`. 
  
BrainSpace works on `Python 3.5+`, and probably with older versions of Python 3,
although it is not tested.

**Dependencies**   
To use BrainSpace, the following Python packages are required:

*   [`numpy`](https://numpy.org/)  
*   [`scipy`](https://scipy.org/scipylib/index.html)  
*   [`scikit-learn`](https://scikit-learn.org/stable/)  
*   [`vtk`](https://vtk.org/)  
*   [`matplotlib`](https://matplotlib.org/)  
*   [`nibabel`](https://nipy.org/nibabel/index.html)  
*   [`nilearn`](https://nilearn.github.io/)  

## Data ##
Glasser, M., Coalson, T., Robinson, E. et al. A multi-modal parcellation of human cerebral cortex. Nature 536, 171–178 (2016). https://doi.org/10.1038/nature18933  
BALSA laboratory: https://balsa.wustl.edu/study/show/RVVG    
 
 ## Functions ##
`hcp_parcels.csv` credit to [Ansteeg NMA project](https://github.com/ansteeg/NeuroMatchProject)   
`hcp_dataset.py` credit to [Ansteeg NMA project](https://github.com/ansteeg/NeuroMatchProject)   

## Notebooks ##

At the present moment `colab` notebook does not run properly. But the notebooks work fine locally.
|   | Run | View |
| - | --- | ---- |
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/c8c2a889cabe4b1db308557e8f73f457)](https://app.codacy.com/gh/rcruces/2020_NMA_surface-plot?utm_source=github.com&utm_medium=referral&utm_content=rcruces/2020_NMA_surface-plot&utm_campaign=Badge_Grade)
| Surface plot with BrainSpace | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rcruces/2020_NMA_surface-plot/blob/master/data/tutorial-surface_plot_with_BrainSpace.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/rcruces/2020_NMA_surface-plot/blob/master/data/tutorial-surface_plot_with_BrainSpace.ipynb?flush_cache=true) |
| Surface plot with NMA HCP data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rcruces/2020_NMA_surface-plot/blob/master/data/tutorial-surface_plot_hcp_example.ipynb) | [![View the notebook](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.jupyter.org/github/rcruces/2020_NMA_surface-plot/blob/master/data/tutorial-surface_plot_hcp_example.ipynb?flush_cache=true) |

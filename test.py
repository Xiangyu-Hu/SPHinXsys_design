import pyvista as pv
from pyvista import examples

# download an example and display it using physically based rendering.
mesh = examples.download_lucy()
mesh.plot(color='lightgrey', pbr=True, metallic=0.2)
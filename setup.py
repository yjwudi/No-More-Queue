from distutils.core import setup
import py2exe

Mydata_files = [('logo', ['D:/Python/nmq_second/logo/logo.png', 'D:/Python/nmq_second/logo/icon.png'])]

setup(
	name="No More Queue",
	author="Change the World",
    windows=['index.py', 'nmq_second_stc_cc.py', 'nmq_second_cluster_cc.py'],
    data_files = Mydata_files,
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 0,
                        "bundle_files": 3,
                        "includes": ["scipy.sparse.csgraph._validation","sklearn.utils.sparsetools._graph_validation",
                                     "scipy.special._ufuncs_cxx","sklearn.utils.lgamma", "sklearn.neighbors.typedefs",
                                     "sklearn.decomposition.pca","sklearn.utils.weight_vector","sklearn.covariance"],
                        "excludes": ["email"]
                }
        }
)
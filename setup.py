from pathlib import Path
from setuptools import setup, find_packages


setup(
    name='SparseAEH',
    version='0.1.0',
    description='Fastened SpatialDE',
    url='https://github.com/jackywangtj66/NewDE',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy', 'scipy >= 1.0', 'pandas>=0.23', 'scikit-learn'
    ]
)
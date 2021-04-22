from setuptools import setup, find_packages

setup(
    name='mySUNI',
    version='1.0.7',
    description='mySUNI CDS',
    author='Teddy Lee, BAEM1N',
    author_email='teddylee777@gmail.com, baemin.dev@gmail.com',
    url='https://github.com/BAEM1N/mySUNI',
    download_url='https://github.com/BAEM1N/mySUNI/archive/master.zip',
    install_requires=['numpy', 'pandas', 'seaborn', 'requests', 'scikit-learn', 'xgboost', 'lightgbm', 'openpyxl', 'xlrd', 'matplotlib'],
    packages=find_packages(exclude=[]),
    keywords=['mySUNI', 'CDS'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

from setuptools import setup, find_packages

setup(
    name='mySUNI',
    version='1.4.3',
    description='mySUNI CDS',
    author='BAEM1N, Teddy Lee',
    author_email='baemin.dev@gmail.com, teddylee777@gmail.com',
    url='https://github.com/braincrew/cds',
    install_requires=['tqdm', 'scikit-learn', 'pandas', 'matplotlib', 'seaborn', 'jupyter', 'ipywidgets', 'requests'],
    packages=find_packages(exclude=[]),
    keywords=['mySUNI', 'CDS'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)

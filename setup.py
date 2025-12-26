from setuptools import setup

setup(
    name='portzapper',
    version='1.0.0',
    py_modules=['zapper'],
    install_requires=[
        'psutil',
    ],
    entry_points={
        'console_scripts': [
            'zapper=zapper:main',
        ],
    },
)

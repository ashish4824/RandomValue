from setuptools import setup, find_packages

setup(
    name='randomgen',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Ashish',
    author_email='ashishmaurya0408@gmail.com',
    description='A simple package to generate random numbers, characters or both.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/randomgen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
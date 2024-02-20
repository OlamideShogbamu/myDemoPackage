from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['test*']),
    license='MIT',
    description='EDSA example pyhton package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/olamideshogbamu/mypackage',
    author='Olamide SHOGBAMU',
    author_email='shogbamuolamide@gmail.com'
)
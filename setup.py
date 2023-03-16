#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>



from setuptools import setup
import pytorchqbit

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

setup(
    name='pytorchqbit',
    version='0.0.1',
    description='Quantum bit and the usual gates in torch tensors straight from the Wikipedia',
    long_description=README,
    license="MIT",
    author="Pauli Rikula",
    url='https://github.com/kummahiih/pytorchqbit',
    packages=['pytorchqbit'],
    python_requires='~=3.10',
    install_requires=[
          'torch>=2.0.0'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6']
)
    
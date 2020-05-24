#    @copyright: 2020 by Pauli Rikula
#    @license: MIT <http://www.opensource.org/licenses/mit-license.php>



from setuptools import setup
import qbit

with open('README.md', 'r') as readme_file:
    README = readme_file.read()

setup(
    name='pyqbit',
    version='0.2.1',
    description='Quantum bit and the usual gates in numeric forms straight from the Wikipedia',
    long_description=README,
    license="MIT",
    author="Pauli Rikula",
    url='https://github.com/kummahiih/pyqubit',
    packages=['qbit'],
    python_requires='~=3.6',
    install_requires=[
          'numpy>=1.18.1'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6']
)
    
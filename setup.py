import setuptools

setuptools.setup(
    name='rega',
    version='0.1.1',
    scripts=['./src/rega.py'],
    author='Josep Maria Salvia Hornos',
    description='Apply regex in bulk!.',
    packages=['src'],
    entry_points = {
        'console_scripts': ['rega=src.rega:main'],
    },
    install_requires=open('requirements.txt', 'r').read().splitlines(),
    python_requires='>=3.8'
)
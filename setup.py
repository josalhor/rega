import setuptools

setuptools.setup(
    name='reap',
    version='0.1',
    scripts=['./src/reap.py'],
    author='Josep Maria Salvia Hornos',
    description='Apply regex in bulk!.',
    packages=['src'],
    entry_points = {
        'console_scripts': ['reap=src.reap:main'],
    },
    install_requires=open('requirements.txt', 'r').readlines(),
    python_requires='>=3.8'
)
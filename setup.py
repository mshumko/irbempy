# import setuptools
# from setuptools.command.develop import develop
# from setuptools.command.install import install
# import subprocess
# import time
import pathlib

from numpy.distutils.core import Extension, setup

source_dir = pathlib.Path(__file__).parent / 'IRBEM' / 'source'
sources = [str(path) for path in source_dir.glob('*.f')]
print(source_dir)
print(f'{sources=}')
libirbem = Extension(
    name='libirbem', sources=sources,
    extra_f77_compile_args=['-w', '-O2', '-fPIC', '-fno-second-underscore', '-fcheck=all']
    )

setup(
    name = 'irbempy',
    packages = ['irbempy'],
    ext_modules = [libirbem],
)
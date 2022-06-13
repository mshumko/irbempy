import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess
import time

class PreDevelopCommand(develop):
    """Pre-installation for development mode."""
    def run(self):
        subprocess.Popen("make OS=linux64 ENV=gfortran64 clean".split(), cwd="./IRBEM")
        print('Building IRBEM-Lib source')
        subprocess.Popen("make OS=linux64 ENV=gfortran64 all".split(), cwd="./IRBEM")
        print('Installing IRBEM-Lib source')
        subprocess.Popen("make OS=linux64 ENV=gfortran64 install".split(), cwd="./IRBEM")
        install.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        subprocess.Popen("make OS=linux64 ENV=gfortran64 clean".split(), cwd="./IRBEM")
        print('Building IRBEM-Lib source')
        subprocess.Popen("make OS=linux64 ENV=gfortran64 all".split(), cwd="./IRBEM")
        print('Installing IRBEM-Lib source')
        subprocess.Popen("make OS=linux64 ENV=gfortran64 install".split(), cwd="./IRBEM")
        install.run(self)

setuptools.setup(
    cmdclass={
        'develop': PreDevelopCommand,
        'install': PreInstallCommand,
    },
)
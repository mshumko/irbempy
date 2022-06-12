import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import run

# class PreDevelopCommand(develop):
#     """Pre-installation for development mode."""
#     def run(self):
#         # check_call("apt-get install this-package".split())
#         develop.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        print('irbempy install script is running.')
        _pwd = run("pwd", shell=True, check=True)
        print(_pwd.stdout)
        # check_call("cd IRBEM".split(), shell=True)
        _build = run("cd IRBEM/ && make OS=linux64 ENV=gfortran64 all".split(), shell=True, check=True)
        print(_build.stdout)
        print(_build.stderr)
        # run("cd /IRBEM/ && make OS=linux64 ENV=gfortran64 install".split(), shell=True, check=True)
        print('irbempy install script is finished.')
        install.run(self)

setuptools.setup(
    cmdclass={
        # 'develop': PostDevelopCommand,
        'install': PreInstallCommand,
    },
)
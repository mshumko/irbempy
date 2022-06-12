import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

# class PreDevelopCommand(develop):
#     """Pre-installation for development mode."""
#     def run(self):
#         # check_call("apt-get install this-package".split())
#         develop.run(self)

class PreInstallCommand(install):
    """Pre-installation for installation mode."""
    def run(self):
        print('irbempy install script is running.')
        # check_call("apt-get install this-package".split())
        install.run(self)

setuptools.setup(
    cmdclass={
        # 'develop': PostDevelopCommand,
        'install': PreInstallCommand,
    },
)
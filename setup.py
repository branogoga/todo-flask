from setuptools import setup, find_namespace_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

requirements = [
    "importlib_resources; python_version<'3.9'",
    "Flask>=1.0.0",
    "SQLAlchemy==1.4.28",
    "pg8000==1.19.4",
]

test_requirements = [
    "pytest==6.0.1",
    "pytest-repeat==0.8.0",
    "flake8==3.7.3",
]

extras = {"test": test_requirements}


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)


setup(
    name="todo-flask",
    version="0.1",
    packages=find_namespace_packages(include=["app.src.*"], exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    extras_require=extras,
    cmdclass={"install": PostInstallCommand, "develop": PostDevelopCommand},
)

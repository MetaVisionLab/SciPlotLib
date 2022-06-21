import os.path as osp

from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        content = f.read()
    return content


def find_version():
    version_file = "sciplotlib/__init__.py"
    with open(version_file, "r") as f:
        exec(compile(f.read(), version_file, "exec"))
    return locals()["__version__"]


def get_requirements(filename="requirements.txt"):
    here = osp.dirname(osp.realpath(__file__))
    with open(osp.join(here, filename), "r") as f:
        requires = [line.replace("\n", "") for line in f.readlines()]
    return requires


setup(name="sciplotlib",
      version=find_version(),
      description="SciPlotLib: A toolbox for drawing figures commonly "
                  "found in journal or conference papers.",
      author="MetaVisionLab",
      license="GUN",
      long_description=readme(),
      url="https://github.com/MetaVisionLab/SciPlotLib",
      packages=find_packages(),
      install_requires=get_requirements(),
      keywords=["visualization"])

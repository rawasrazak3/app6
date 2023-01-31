from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in app6/__init__.py
from app6 import __version__ as version

setup(
	name="app6",
	version=version,
	description="test",
	author="rawas",
	author_email="rawasrazak3@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

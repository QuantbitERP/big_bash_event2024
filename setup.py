from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in big_bash_event2024/__init__.py
from big_bash_event2024 import __version__ as version

setup(
	name="big_bash_event2024",
	version=version,
	description="Big Bash Event2024",
	author="Big Bash Event2024",
	author_email="21pradipjadhav@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

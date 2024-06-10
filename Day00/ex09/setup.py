from setuptools import setup, find_packages

setup(
	name = "ft_package",
	version = "0.0.1",
	author = "lmoheyma",
	author_email = "lmoheyma@student.42.fr",
	license = "MIT",
	description = "3P aka PPP aka Python Piscine Package",
	classifiers = [
		"Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
	],
	package_dir = {"": "src"},
	packages = find_packages(where="src")
)
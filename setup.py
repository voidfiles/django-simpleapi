from setuptools import setup, find_packages


setup(
    name="django-simpleapi",
    version="1.0",
    author="Alex Kessinger",
    author_email="voidfiles@gmail.com",
    description="A Django package that allows you to write apis simply",
    long_description=open("README.rst").read(),
    license="MIT",
    url="http://github.com/pinax/django-waitinglist",
    packages=find_packages(),
    package_data={"waitinglist": ["templates/*/*/*"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
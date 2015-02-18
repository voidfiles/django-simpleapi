from setuptools import setup

packages = [
    'simpleapi',
]

setup(
    name="django-simpleapi",
    version='1.4.0',
    author="Alex Kessinger",
    author_email="voidfiles@gmail.com",
    description="A Django package that allows you to write APIs simply",
    long_description=open("README.rst").read(),
    license="MIT",
    url="http://github.com/voidfiles/django-simpleapi",
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'simplepai': 'simplepai'},
    include_package_data=True,
    setup_requires=['Django >= 1.7'],
    install_requires=['Django >= 1.7', 'django-cors-headers >= 1.0.0'],
    tests_require=['Django >= 1.7'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)

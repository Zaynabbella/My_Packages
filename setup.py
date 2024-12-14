from setuptools import setup, find_packages

setup(
    name="mathops",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    author="BELLAFRIKH ZAYNAB",
    author_email="zaynabbellafrikh@gmail.com",
    description="A simple mathematical operations package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zaynabbella/mathops",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
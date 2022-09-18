from setuptools import setup, find_packages

setup(
    name="valscreen",
    version="1.0",
    author="Adrien GIVRY",
    author_email="contact@adrien-givry.com",
    description="Command-line quantitative stock screener for publicly-traded companies in the United States and Canada ",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/adriengivry/valscreen",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "valscreen = valscreen.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

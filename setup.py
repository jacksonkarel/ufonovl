import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="ufonovl",
    version="1.0.0",
    description="An NLP pipeline that detects new textual information about UFOs/UAPs",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jacksonkarel/ufonovl",
    author="Jackson Karel",
    author_email="jackson.karel2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["ufonovl"],
    include_package_data=True,
    install_requires=["APScheduler", "praw", "psaw", "sentence_transformers", "setuptools", "spacy", "torch"],
    entry_points={
        "console_scripts": [
            "ufonovl=ufonovl.__main__:main",
        ]
    },
)
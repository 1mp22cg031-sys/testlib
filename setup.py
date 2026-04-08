from setuptools import setup, find_packages

setup(
    name="planning-agent-lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "requests"
    ],
)
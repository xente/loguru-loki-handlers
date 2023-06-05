from setuptools import setup

# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="loguru-loki-handler",
    version="0.1.0",
    author="Xente",
    description="Handler created for Loguru that sends logs to Grafana Loki in JSON format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xente/loguru-loki-handlers",
    packages=["loguru_loki_handler"],  
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="loki, loguru",
    install_requires=[]
)

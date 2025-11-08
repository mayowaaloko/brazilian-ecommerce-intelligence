from setuptools import setup, find_packages

setup(
    name="brazilian-ecommerce-intelligence",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="End-to-end ML + GenAI platform for e-commerce analytics",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/brazilian-ecommerce-intelligence",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Data Scientists",
        "Topic :: Machine Learning :: Analytics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.9",
    install_requires=open("requirements.txt").read().splitlines(),
)

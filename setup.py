import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="wayforpay",
    version="1.0.1",
    author="Serhii Zahranychnyi",
    author_email="serhii.z@edicasoft.com",
    description="WayForPay API wrapper for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zagran/wayforpay",
    packages=setuptools.find_packages(),
    install_requires=["requests==2.32.2", ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

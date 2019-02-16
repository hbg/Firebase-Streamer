import setuptools

with open("README.md", "r") as f:
    description = f.read()
setuptools.setup(
    name="firebase-stream",
    version="0.0.2",
    author="Harris Beg",
    author_email="harris@harrisbeg.com",
    description="A Python library utilizing Firebase-Admin to create live requests",
    long_description=description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
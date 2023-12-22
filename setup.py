import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
__version__ = "0.0.1"

REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_NAME = "Shrey-patel-07"
SRC_REPO = "kidney_classification"
AUTHOR_EMAIL = "shrey07patel@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for kidney disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
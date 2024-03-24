from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

def get_requirements(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

__version__ = "0.0.4"
REPO_NAME = "PyMongo-Atlas-Connector-Seamless-MongoDB-Integration"
PKG_NAME = "databaseconnection"
AUTHOR_USER_NAME = "DeependraVerma"
AUTHOR_EMAIL = "deependra.verma00@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with a database.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
    extras_require={
        'dev': get_requirements("requirements_dev.txt")
    },
    include_package_data=True,
)

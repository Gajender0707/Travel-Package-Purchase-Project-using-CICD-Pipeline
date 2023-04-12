from setuptools import setup,find_packages


def Requirements(filename):
    with open(filename,"r") as f:
        req=f.readlines()
        req=[i.replace("\n","") for i in req]
        if "-e ." in req:
            req.remove("-e .")
    return req



setup(
    name="Travel_Package_Prediction",
    author="Gajender",
    version="0.1",
    author_email="iamsanju0707@gmail.com",
    description="All about the Prediction of Travel Package wheather a customer will purchse it or not.",
    packages=find_packages(),
    install_requires=Requirements("requirements.txt")
)
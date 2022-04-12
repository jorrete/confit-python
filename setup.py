from setuptools import find_packages, setup

setup(
    name="confit",
    version="0.1.0",
    description="",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyyaml",
    ],
    extras_require={
        "dev": [
            "rich",
            "black",
            "flake8",
        ]
    },
    zip_safe=False,
    # url="",
    # author="",
    # author_email="",
)

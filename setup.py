import setuptools

setuptools.setup(
    name="matrix-axiom",
    version="0.1.0",
    author="Jonathan de Jong",
    author_email="jonathan@automatia.nl",
    description="Axiom Matrix HomeServer Implementation",
    url="https://github.com/shadowjonathan/axiom",
    packages=["axiom"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["dataclasses; python_version<'3.7'", "sanic>=20"],
    setup_requires=["wheel"],
    extras_require={
        "dev": ["ipython", "twine", "tox", "bump2version"],
        "lint": [
            # pin all requirements here to get deterministic linting
            "isort==5.7.0",
            "mypy==0.800",
            "black==20.8b1",
            "flake8==3.8.4",
            "flake8-bugbear==20.11.1",
            "flake8-comprehensions==3.3.1",
            "docformatter==1.4",
        ],
    },
)

import os
import setuptools


def read(path, encoding="utf-8"):
    path = os.path.join(os.path.dirname(__file__), path)
    return open(path, encoding=encoding).read() if os.path.exists(path) else ""


setuptools.setup(
    name="ibis-vega-transform",
    version="2.0.1",
    url="https://github.com/Quansight/ibis-vega-transform",
    author="Ian Rose and Saul Shanabrook",
    author_email="ian.rose@quansight.com",
    license="Apache-2.0 license",
    description="Evaluate Vega transforms using Ibis expressions",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        "jupyterlab",
        "altair-transform",
        "altair",
        "vega_datasets",
        "ibis-framework",
        "pymapd",
        "tornado<6",
        "mypy_extensions",
        "typing_extensions",
        "jaeger-client",
        "jupyter_jaeger",
    ],
    extras_require={"dev": ["black"]},
    python_requires=">=3.6",
    include_package_data=True,
)

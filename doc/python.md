# Python on Ampere Processors

Python is a interpreted, high-level and consistently ranks as one of the most popular programming languages. Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, a free and open-source reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development. 

One of most important reason is Python as an interpreted language, it's code will be runtime interpreted on most modern architectures including ARM64. Visit _[Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))_ to get more info about Python.

## Python installation

Python 3.8 and later version is recommanded for Ampere Processors considering _[release cycle](https://devguide.python.org/versions/)_ of varies Python versions.

Most Linux distributions make Python available through their respective package repositories. Ubuntu distributions like 20.04 and or Debian already has Python3 pre-installed, take Ubuntu 22.04 as an example, to check Python3 version:

```shell
$ python3 -V
Python 3.8.10
```

For Python developers, additional development tools are required to setup a programming environment:
```shell
sudo apt update
sudo apt-get install build-essential python3-dev libblas-dev libffi-dev liblapack-dev
```

## Python packages installation

Python use _[pip](https://en.wikipedia.org/wiki/Pip_(package_manager))_ (package-management system) to install and manage software packages. Pip will download required packages from default PyPI repository by simply run:

```shell
pip install <package-name>
```

Or a custom repository can be designated during installation:
```shell
pip install -i <https://your-custom-repo/simple> <package-name>
```

Or you can intsall a whl package on your local disk directly:
```shell
pip install <path-to-whl-package>
```

Usually, whl package is following _[PEP 491](https://peps.python.org/pep-0491/)_ for package name format. We can get whl distribution package name from `Downlaod files` page of each Python package on _[PyPI website](https://pypi.org/)_ to learn whether the Python package support AARCH64 or not.

Per defined in _[PEP 491](https://peps.python.org/pep-0491/)_, the wheel filename is `{distribution}-{version}(-{build tag})?-{python tag}-{abi tag}-{platform tag}.whl`

If `aarch64` is present for `{platform tag}` tag, it means the Python package is ready for AARCH64 architecture including Ampere Processors. In most Python packages, `any` is set for `{platform tag}` tag which means the Python package is compatible with on any CPU architecture including Ampere Processors.

## Python packages for AI

Most popular artificial intelligence (AI) frameworks like TensorFlow, ONNX, PyTorch provides Python package for developers.

Ampere Optimized AI delivers world class AI Inference solutions with a significant inference performance benefit to any existing model that runs on our supported frameworks out of the box. 

Ampere processors support native FP16 data format providing nearly 2X speedup over FP32 with almost no accuracy loss for most AI models. _[Ampere AI}(https://amperecomputing.com/solutions/ampere-ai)_ currently supports the following frameworks available for free download  or at some of our supporting partners:
- TensorFlow
- PyTorch
- ONNX

Ampere Optimized AI inference acceleration engine is fully integrated with the orignal framework.

## Regression results

Ampere running Daily regression tests on platforms powered by Ampere processors with Python official image on DockerHub to ensure each platform based on Ampere processors compatible with last changes from Python official release. Visit _[regression results page](https://amperecomputing.com/solution/python/regression-results)_ to find out regression status.

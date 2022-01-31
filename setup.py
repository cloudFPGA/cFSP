# /*******************************************************************************
#  * Copyright 2016 -- 2022 IBM Corporation
#  *
#  * Licensed under the Apache License, Version 2.0 (the "License");
#  * you may not use this file except in compliance with the License.
#  * You may obtain a copy of the License at
#  *
#  *     http://www.apache.org/licenses/LICENSE-2.0
#  *
#  * Unless required by applicable law or agreed to in writing, software
#  * distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.
# *******************************************************************************/

#  *                       cloudFPGA
#  *     Copyright IBM Research, All Rights Reserved
#  *    =============================================
#  *     Created: Jan. 2022
#  *     Authors: FAB, WEI, NGL, DID
#  *
#  *     Description:
#  *      A setup file used for buidling a PyPi package.
#  *
#  *    License:
#  *     Apache Version 2.0


import setuptools

with open("README_pypi.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cfsp", 
    version="0.0.7",
    author="Dionysios Diamantopoulos",
    author_email="did@zurich.ibm.com",
    description="The cloudFPGA Support Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudFPGA/cfsp",
    bug_tracker = "https://github.com/cloudFPGA/cfsp/issues",
    # this package contains one module,
    # which resides in the subdirectory mymodule
    packages=setuptools.find_packages(),
    setup_requires=['wheel'],
    install_requires=[
        "certifi",
        "charset-normalizer",
        "docopt",
        "idna",
        "prompt-toolkit",
        "Pygments",
        "PyInquirer",
        "regex",
        "requests",
        "six",
        "tqdm",
        "urllib3",
        "wcwidth",
    ],
    # make sure the shared library is included
    package_data={'':['cFSPlib']},
    #data_files=[('', ['cfsp'])],
    scripts=['cfsp'],
    #data_files=['cfsp'],
    #include_package_data=True,
    
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)

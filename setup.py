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
#  *      The setup file used for buidling cfsp PyPi package.
#  *
#  *    License:
#  *     Apache Version 2.0


import setuptools, os
from shutil import copyfile

with open("README_pypi.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
fh.close()


version_path = os.path.dirname(os.path.abspath(__file__))+"/cFSPlib/version.txt"
with open(version_path,"r") as fh:
    for line in fh:
        __version__ = line.rstrip("\n")
fh.close()


setuptools.setup(
    name="cfsp", 
    version=__version__,
    author="Dionysios Diamantopoulos",
    author_email="did@zurich.ibm.com",
    description="The cloudFPGA Support Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cloudFPGA/cfsp",
    project_urls={
        "Bug Tracker": "https://github.com/cloudFPGA/cfsp/issues",
    },    
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
    package_data={'':['cFSPlib']},   
    include_package_data=True,
    scripts=['cfsp'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.6',
)

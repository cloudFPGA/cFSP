<p align="center">
  <a aria-label="License" href="https://github.com/cloudFPGA/cFSP/blob/master/LICENSE">
    <img alt="" src="https://img.shields.io/github/license/cloudFPGA/cFSP?style=for-the-badge&labelColor=000000">
  </a>
  <a aria-label="PyPi" href="https://pypi.org/project/cfsp/">
    <img alt="" src="https://img.shields.io/pypi/v/cfsp?style=for-the-badge&labelColor=000000">
  </a>
  <a aria-label="Python" href="#cFSP">
    <img alt="" src="https://img.shields.io/pypi/pyversions/cfsp?style=for-the-badge&labelColor=000000">
  </a>
</p>

[![Build Status](https://jenkins.cloudfpga.zc2.ibm.com/buildStatus/icon?job=cFSP)](https://jenkins.cloudfpga.zc2.ibm.com/job/cFSP/)

# cFSP

The **cloudFPGA Support Package (cFSP)** for the cloudFPGA project.

Currently, the cFSP includes a library for the control plane of cloudFPGA.

The cFSP control plane includes a [Python package](cFSPlib/python_api_client/README.md) which is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.8
- Package version: 1.0.0

[Instrunctions to update the Python API Client](#update-of-the-python-python-api)

## Requirements

Python 3.6+

## Installation

We recommend the installation at an isolated Python environment, e.g. through [Virtualenv](https://virtualenv.pypa.io).

### Installation through github
Use this option for the most up-to-date installation.

```bash
git clone git@github.com:cloudFPGA/cFSP.git
cd cFSP/
virtualenv -p /usr/bin/python3.8 cfenv
source cfenv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Installation through PyPi

We maintain `cFSP` at [PyPi](https://pypi.org/project/cfsp/).
Use this option for fast installation.

```bash
virtualenv -p /usr/bin/python3.8 cfenv
source cfenv/bin/activate
pip install --upgrade pip
pip install cfsp
```

> **_NOTE:_** If you install `cfsp` through `PyPi`, then the top-level script `cfsp` can be executed from any directory location, and not necessarily from the cFSP root path. Thus, in the following commands you should replace `./cfsp` by `cfsp`.

## Getting Started

### Contents

* [Getting help](#getting-help).
* [Setting up the credentials file for a user](#setting-up-the-credentials-file-for-a-user).
* [Show the credentials of a user](#show-the-credentials-of-a-user).
* [Load new credentials for a user](#load-new-credentials-for-a-user).
* [Upload an image](#upload-an-image).
* [Upload an image for pr](#upload-an-image-for-partial-reconfiguration).
* [Get an image](#get-an-image).
* [Create a cluster](#create-a-cluster).
* [Create a multi-node cluster](#create-a-multi-node-cluster).
* [Update the nodes of a cluster](#update-the-nodes-of-a-cluster).
* [Get a cluster](#get-a-cluster).
* [Extend a cluster](#extend-a-cluster).
* [Reduce a cluster](#reduce-a-cluster).
* [Restart a cluster](#restart-a-cluster).
* [Delete a cluster](#delete-a-cluster).
* [Create an instance](#create-an-instance).
* [Get an instance](#get-an-instance).
* [Restart an instance](#restart-an-instance).
* [Delete an instance](#delete-an-instance).
* [Use cFSP as a Python module](#use-cfsp-as-a-python-module).


A comprehensive example that tests all the supported functions of cFSP is provided in [tests/test_cfsp_module.py](https://github.com/cloudFPGA/cFSP/blob/master/test/test_cfsp_module.py).

### Getting help

Please follow the [installation procedure](#installation--usage) and then run the following:


```bash
./cfsp --help
```

![cfsp-help](doc/img/1.png)

### Setting up the credentials file for a user

Load the credentials for a user. If no credentials file exists, a new one be created. The default filename is `user.json` and it is strored in the cFSP folder. You need to provide your ZYC2 username and password, as well as a project you are member of.

```bash
./cfsp user load  --username=my_username --password=my_password --project=my_project
```

![cfsp-user-load](doc/img/2.png)

The file has the following JSON format:

![cfsp-user-json](doc/img/3.png)


> **_NOTE:_** You may provide a specific configuration file instead of the default (user.json), by using the option `-c my_custom_file` (or `--config my_custom_file`), e.g.

```bash
./cfsp user load --config /home/user/user.json
```

### Show the credentials of a user

Show the credentials of a user from a credentials file.

```bash
./cfsp user show
```

![cfsp-user-show](doc/img/2a.png)


### Load new credentials for a user

You can easily load new credentials by:
* either editing the configuration file (e.g. user.json), 
* or by providing any of the supported command line options (`--username`, `--password`, `--project`). In the latter case, the configuration file is being overwritten.

  ```bash
  ./cfsp user load --username=anotherUser  --password=anotherPassword  --project=anotherProject
  ```

  ![cfsp-user-load-new](doc/img/2b.png)


### Upload an image

Assuming you want to upload the FPGA image which is stored at `/tmp/4_topFMKU60_impl_monolithic.bit`

```bash
./cfsp image post --image_file=4_topFMKU60_impl_monolithic.bit

```

![cfsp-image-post](doc/img/4.png)


### Upload an image for partial reconfiguration

Assuming you want to upload the FPGA image for pr which is stored at `/tmp/example_files_PR/4_topFMKU60_impl_2_pblock_ROLE_partial.bin`. In that case you will also need the corresponding signature file that was produced by the build (`/tmp/example_files_PR/4_topFMKU60_impl_2_pblock_ROLE_partial.bin.sig`), as well as the result of the pr_verify command `/tmp/example_files_PR/5_topFMKU60_impl_2_pblock_ROLE_partial.rpt`. In addition, a configuration json file is selected by default in the parent folder of the provided image file. An example follows:

```bash
./cfsp image post-app-logic --image_file=/tmp/example_files_PR/4_topFMKU60_impl_2_pblock_ROLE_partial.bin --sig_file=/tmp/example_files_PR/4_topFMKU60_impl_2_pblock_ROLE_partial.bin.sig --pr_verify_rpt=/tmp/example_files_PR/5_topFMKU60_impl_2_pblock_ROLE_partial.rpt

```
![cfsp-image-post-pr](doc/img/4a.png)


Please note that those last two files are automatically selected by default, if only the image file is provided, like in the following example:

![cfsp-image-post](doc/img/4b.png)


### Get an image

Assuming you want to get the details of the previously uloaded FPGA image with id `74462cd5-20e3-4228-a47d-258b7e5e583a`

```bash
./cfsp image get 74462cd5-20e3-4228-a47d-258b7e5e583a
```

![cfsp-image-get](doc/img/5.png)


### Create a cluster

Assuming you want to create a cluster with
  * one CPU node from ZYC2 with ip=`10.12.2.100`
  * one FPGA from cloudFPGA platform with the previously uloaded FPGA image with id `74462cd5-20e3-4228-a47d-258b7e5e583a`

```bash
./cfsp cluster post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --node_ip=10.12.2.100
```

![cfsp-cluster-post](doc/img/6.png)


> **_NOTE:_** By using the option `--node_id` after every `--image_id` and `--node_ip`, you can define the specific rank that this CPU node or FPGA node is associated with. If no such (an) option(s) (is)are provided, then incremental `node_id`s will be assigned, as shown in the figure above. Please note that if you provide `--node_id`s, it is mandatory to firstly define those of CPU(s) and secondly of FPGA(s).

> **_NOTE:_** You may want to create many clusters of the previous type. For such cases, there is an extra option `--repeat=<num>`, which specifies how many times the command should be issued. Please note that this applies to all supported commands of `cfsp`, e.g. :

```bash
./cfsp cluster post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --node_id 0 --node_ip=10.12.2.100 --node_id 1 --repeat=2

```

![cfsp-cluster-post-repeat](doc/img/6a.png)


### Create a multi-node cluster

You can add to a cluster an arbitrary number of
  * CPU nodes from ZYC2, by using the `--node_ip=` identifier
  * FPGA nodes from cloudFPGA, by using the `--image_id=` identifier

```bash
./cfsp cluster post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --image_id=d031b5a9-c3d8-4775-98db-e3de936a63e3  --node_ip=10.12.2.100 --node_ip=10.12.2.101 --node_ip=10.12.2.103 --node_ip=10.12.2.104 --node_ip=10.12.2.105
```

![cfsp-cluster-post-many](doc/img/6b.png)


### Update the nodes of a cluster

You can update:
* the images of some or all of the FPGA nodes of a cluster.
* the IPs of some or all CPU nodes of a cluster

For example to update only the image of the `node_id=0`, of the previously created cluster with id `257`, to the `image_id=3f0427af-d37a-453d-b8c4-a813c4573d12`, you may use:

```bash
/cfsp cluster update --cluster_id=257 --node_id=0 --image_id=3f0427af-d37a-453d-b8c4-a813c4573d12
```

![cfsp-cluster-post-many](doc/img/6c.png)

And to update only the IP of one of the CPU nodes, e.g. from `10.12.2.103` to `10.12.2.109`, you may use:

```bash
/cfsp cluster update --cluster_id=257 --node_id=4 --node_ip=10.12.2.109
```

> **_NOTE:_** You may use the option `--node_id` as many times as you want to specify the CPU or FPGA nodes of the cluster to update. Depending on the type of the node_id which will be provided, either FPGA or CPU node(s), will be updated. If no `--node_id` argument will be provided, the tool will search for any available FPGA or CPU nodes in the specified `cluster_id`, and it will attempt to update all of them to the specified `image_id` (for FPGA nodes) or `node_ip` (for CPU nodes). Currently there is no option to simultanously update FPGA and CPU nodes of a cluster and an exception will be raised in such an attempt.

### Get a cluster

Assuming you want to get the details of a cluster with id `259`

```bash
./cfsp cluster get 259
```

![cfsp-cluster-get](doc/img/7.png)


### Extend a cluster

Assuming you want to extend the previously created cluster with id `259`, with one more FPGA with image id `d031b5a9-c3d8-4775-98db-e3de936a63e3`, and one more CPU node from ZYC2 with ip=`10.12.2.106`.

```bash
./cfsp cluster extend --cluster_id 259 --image_id=d031b5a9-c3d8-4775-98db-e3de936a63e3  --node_id 7 --node_ip=10.12.2.106 --node_id 8
```

![cfsp-cluster-extend](doc/img/7a.png)

> **_NOTE:_** You may extend a cluster with numerous FPGA and CPU nodes by using the `--image_id` and `--node_ip` options. For these nodes you must also provide the rank id through `--node_id` option.


### Reduce a cluster

Assuming you want to reduce the previously extended cluster with id `259`, with the two extra nodes, the FPGA node with `node_id=7` and the CPU node with `node_id=8`.

```bash
./cfsp cluster reduce --cluster_id=259 --node_id 7 --node_id 8
```

![cfsp-cluster-reduce](doc/img/7b.png)


### Restart a cluster

Assuming you want to restart a cluster with id `383`

```bash
./cfsp cluster restart 383
```

or


```bash
./cfsp cluster restart --cluster_id=383
```

![cfsp-cluster-delete](doc/img/6d.png)


### Delete a cluster

Assuming you want to delete the previously created cluster with id `259`

```bash
./cfsp cluster delete 259
```

![cfsp-cluster-delete](doc/img/8.png)

> **_NOTE:_** You may delete all uploaded clusters of a user by not providing a specific cluster id, e.g.

```bash
./cfsp cluster delete
```

![cfsp-cluster-delete-all](doc/img/9.png)




### Create an instance

Assuming you want to create an instance with:
  * one FPGA from cloudFPGA platform with the previously uloaded FPGA image with id `74462cd5-20e3-4228-a47d-258b7e5e583a`

```bash
./cfsp instance post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a
```

![cfsp-instance-post](doc/img/10.png)


> **_NOTE:_** You may want to create many instances of the previous type. For such cases, there is an extra option `--repeat=<num>`, which specifies how many times the command should be issued. Please note that this applies to all supported commands of `cfsp`, e.g. :

```bash
./cfsp instance post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --repeat=2
```

![cfsp-instance-post-many](doc/img/10a.png)


### Get an instance

Assuming you want to get the details of the previously created instance with id `5`

```bash
./cfsp instance get 5
```

![cfsp-instance-get](doc/img/11.png)

### Restart an instance

Assuming you want to restart an instance with id `84`

```bash
./cfsp instance restart 84
```

![cfsp-instance-delete](doc/img/13a.png)

### Delete an instance

Assuming you want to delete the previously created instance with id `5`

```bash
./cfsp instance delete 5
```

![cfsp-instance-delete](doc/img/12.png)

> **_NOTE:_** You may delete all uploaded instances of a user by not providing a specific cluster id, e.g.

```bash
./cfsp instance delete
```

![cfsp-instance-delete-all](doc/img/13.png)


### Use cFSP as a Python module

cFSP is both a standalone command-line tool as well as a Python module that can be imported to a 
Python file. This allows the integration of cFSP into programming or CI/CD flows.

To use cFSP as a Python module you need to import the `cFSP` module from the 
`cFSPlib` library, like below:

```
import sys

# make sure cFSPlib's folder is in the PYTHONPATH, or add a line as below
sys.path.append("../")

from cFSPlib import cFSP
```

Then you can use the `main` function of the `cFSP` module for all the supported cFSP capabilities.
The option arguments and commands are inherinted from `args=docopt(cFSP.__doc__)`. Then the desired 
arguments and command can be provided through the folllowing:

```
args['<command>'] = 'put_a_command_here'
args['<put_an_option>'] = ['put_the_value_of_that_option']
```



## Update of the python Python API

In case that a new yaml swagger file is available (e.g. when new fields/features are added in the 
swagger yaml), then a new Python API client needs to be generated. This will replace the existing one. 
To generate a new Python API Client you need the `swagger-codegen` tool which can be downloade at 
https://swagger.io/tools/swagger-codegen/. Then you may use this command:

```
swagger-codegen generate -i http://10.12.0.132:8080/swagger.json -l python -o python_api_client
```

Afterwads the generated folder `python_api_client` can replace the existing one in 
https://github.com/cloudFPGA/cFSP/tree/master/cFSPlib/python_api_client 
(e.g. `cp -r ./python_api_client/* cFSP/cFSPlib/python_api_client/`).



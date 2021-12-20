[![Build Status](https://jenkins.cloudfpga.zc2.ibm.com/buildStatus/icon?job=cFSP)](https://jenkins.cloudfpga.zc2.ibm.com/job/cFSP/)

# cFSP

The **cloudFPGA Support Package (cFSP)** for the cloudFPGA project.

Currently, the cFSP includes a library for the control plane of cloudFPGA.

The cFSP control plane includes a [Python package](cFSPlib/python_api_client/README.md) which is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- OpenAPI version: 0.8
- Package version: 1.0.0

## Requirements.

Python 3.6+

## Installation & Usage

Setting up python virtual environment:

```bash
git clone git@github.com:cloudFPGA/cFSP.git
cd cFSP/
which python3.8
/usr/bin/python3.8
virtualenv -p /usr/bin/python3.8 cfenv
source cfenv/bin/activate
pip install -r requirements.txt
```


## Getting Started

### Getting help

Please follow the [installation procedure](#installation--usage) and then run the following:


```bash
./cfsp --help
```

![cfsp-help](doc/img/1.png)

### Setting up the credentials file for a user

Load the credentials for a user. If no credentials file exists, a template will be created.

```bash
./cfsp user load
```

![cfsp-user-load](doc/img/2.png)

You may edit this file with your ZYC2 username and password.

![cfsp-user-json](doc/img/3.png)

> **_NOTE:_** You may provide a spcific configuration file instead the default (user.json), by using the option `-c my_custom_file` (or `--config my_custom_file`), e.g.

```bash
./cfsp user load /home/user/user.json
```

### Uploading an image

Assuming you want to upload the FPGA image which is stored at `/tmp/4_topFMKU60_impl_monolithic.bit`

```bash
./cfsp image post --image_file=4_topFMKU60_impl_monolithic.bit

```

![cfsp-image-post](doc/img/4.png)


### Get an image

Assuming you want to get the details of the previously uloaded FPGA image with id `74462cd5-20e3-4228-a47d-258b7e5e583a`

```bash
./cfsp image get 74462cd5-20e3-4228-a47d-258b7e5e583a
```

![cfsp-image-post](doc/img/5.png)


### Create a cluster

Assuming you want to create with
  * one CPU node from ZYC2 with ip=`10.12.2.100`
  * one FPGA from cloudFPGA platform with the previously uloaded FPGA image with id `74462cd5-20e3-4228-a47d-258b7e5e583a`

```bash
./cfsp cluster post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --node_ip=10.12.2.100
```

![cfsp-image-post](doc/img/6.png)


### Get a cluster

Assuming you want to get the details of the previously created cluster with id `259`

```bash
/cfsp cluster get 259
```

![cfsp-image-post](doc/img/7.png)


### Delete a cluster

Assuming you want to delete the previously created cluster with id `259`

```bash
/cfsp cluster delete 259
```

![cfsp-image-post](doc/img/8.png)


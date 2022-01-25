[![Build Status](https://jenkins.cloudfpga.zc2.ibm.com/buildStatus/icon?job=cFSP)](https://jenkins.cloudfpga.zc2.ibm.com/job/cFSP/)

# cFSP

The **cloudFPGA Support Package (cFSP)** for the cloudFPGA project.

Currently, the cFSP includes a library for the control plane of cloudFPGA.

The cFSP control plane includes a [Python package](cFSPlib/python_api_client/README.md) which is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.8
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
* [Get a cluster](#get-a-cluster).
* [Delete a cluster](#delete-a-cluster).
* [Create an instance](#create-an-instance).
* [Get an instance](#get-an-instance).
* [Delete an instance](#delete-an-instance).


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

You may edit this file with your ZYC2 username and password. Please remember also to provide a valid project you are member of.

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


> **_NOTE:_** You may want to create many clusters of the previous type. For such cases, there is an extra option `--repeat=<num>`, which specifies how many times the command should be issued. Please note that this applies to all supported commands of `cfsp`, e.g. :

```bash
./cfsp cluster post --image_id=74462cd5-20e3-4228-a47d-258b7e5e583a --node_ip=10.12.2.100 --repeat=2
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


### Get a cluster

Assuming you want to get the details of the previously created cluster with id `259`

```bash
./cfsp cluster get 259
```

![cfsp-cluster-get](doc/img/7.png)


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

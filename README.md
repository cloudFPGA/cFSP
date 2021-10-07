[![Build Status](https://jenkins.cloudfpga.zc2.ibm.com/buildStatus/icon?job=cFSP)](https://jenkins.cloudfpga.zc2.ibm.com/job/cFSP/)

# cFSP

The **cloudFPGA Support Package (cFSP)** for the cloudFPGA project.

Currently, the cFSP includes a library for the control path of cloudFPGA.

## Supported functions

### Control path

Module `cFPy.mngmt`:

#### user
- [x] load_user_credentials(filedir)
- [x] show_user_credentials(filedir)
#### clusters
- [x] post_cluster(number_of_FPGA_nodes, role_image_id, host_address)
- [x] get_cluster_data(cluster_id)
- [x] get_clusters_data()
- [x] delete_cluster_data(cluster_id)
- [x] restart_cluster_apps(cluster_id)
#### instances
- [x] get_instances_data()
- [ ] create_instance(image_id)
- [x] get_instance_data(instance_id)
- [ ] reprogram_instance(instance_id, image_id, dont_verify_memory)
- [ ] api_request_instance(instance_id, custom_request_method, custom_request_uri, custom_request_payload)
- [x] restart_instance_app(instance_id)
- [x] delete_instance(instance_id)
#### images
- [ ] get_images()
- [ ] get_image(image_id)
- [ ] post_image(image_id)
- [ ] delete_image(image_id)

### Data path

Module `cFPy.comm`:

*(to be implemented)*

## Setting up python virtual environment 
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Example usage

Store your credentials in `test/user_example.json`, afterwards:

```bash
cd test
python test.py
```

## Enable OpenVPN in travis
```bash
sudo gem install travis
travis endpoint --set-default --api-endpoint https://travis.ibm.com/api
travis login --github-token <token>
travis encrypt-file zyc2-vpn-user.ovpn --add
travis encrypt-file up-user --add
git add up-user.enc zyc2-vpn-user.ovpn.enc
```




[![Build Status](https://travis.ibm.com/cloudFPGA/cFSP.svg?token=8sgWzx3xuqu53CzFUy8K&branch=master)](https://travis.ibm.com/cloudFPGA/cFSP)

# cFSP

The **cloudFPGA Support Packages (cFSP)** for the cloudFPGA project.

Currently, the cFSP includes a library for the control path of cloudFPGA.

## Supported functions

### user
- [x] load_user_credentials(filedir)
- [x] show_user_credentials(filedir)
### clusters
- [x] post_cluster(number_of_FPGA_nodes, role_image_id, host_address)
- [x] get_cluster_data(cluster_id)
- [x] get_clusters_data()
- [x] delete_cluster_data(cluster_id)
- [x] restart_cluster_apps(cluster_id)
### instances
- [ ] get_instances_data()
- [ ] create_instance(image_id)
- [ ] get_instance_data(instance_id)
- [ ] reprogram_instance(instance_id, image_id, dont_verify_memory)
- [ ] api_request_instance(instance_id, custom_request_method, custom_request_uri, custom_request_payload)
- [x] restart_instance_app(instance_id)
- [x] delete_instance(resource_id)
### images
- [ ] get_images()
- [ ] get_image(image_id)
- [ ] post_image(image_id)
- [ ] delete_image(image_id)


## Example usage
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

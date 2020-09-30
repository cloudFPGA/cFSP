# cFpy
A python library for the control path of cloudFPGA


## Supported functions

- [x] load_user_credentials(filedir)
- [x] show_user_credentials(filedir)
- [x] post_cluster(number_of_FPGA_nodes, role_image_id, host_address)
- [x] get_cluster_data(cluster_id)
- [x] get_clusters_data()
- [x] delete_cluster_data(cluster_id)
- [x] restart_cluster_apps(cluster_id)

- [ ] get_instances_data()
- [ ] create_instance(image_id)
- [ ] get_instance_data(instance_id)
- [ ] reprogram_instance(instance_id, image_id, dont_verify_memory)
- [ ] api_request_instance(instance_id, custom_request_method, custom_request_uri, custom_request_payload)
- [x] restart_instance_app(instance_id)
- [x] delete_instance(resource_id)

- [ ] get_images()
- [ ] get_image(image_id)
- [ ] post_image(image_id)
- [ ] delete_image(image_id)


## Example usage
```bash
cd test
python test.py
```

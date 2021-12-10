# ImagesAppLogicBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_details** | **str** | Must be a valid &#x60;image_detail&#x60; dict-representation. Example: &#x60;&#x60;&#x60;json  {    \&quot;cl_id\&quot;: \&quot;42\&quot;,    \&quot;fpga_board\&quot;: \&quot;FMKU60\&quot;,    \&quot;shell_type\&quot;: \&quot;Themisto\&quot;,    \&quot;comment\&quot; : \&quot;Some valuable               information for humans (optional)\&quot;  }  &#x60;&#x60;&#x60;  | 
**image_file** | **str** | FPGA binfile to be programmed | 
**sig_file** | **str** | The corresponding .sig file of the binfile | 
**pr_verify_rpt** | **str** | Result of the &#x60;pr_verify&#x60; command | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


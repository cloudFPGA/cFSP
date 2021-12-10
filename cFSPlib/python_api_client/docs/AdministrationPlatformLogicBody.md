# AdministrationPlatformLogicBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_details** | **str** | Must be a valid &#x60;image_detail&#x60; dict-representation. Example: &#x60;&#x60;&#x60;json  {    \&quot;fpga_board\&quot;: \&quot;FMKU60\&quot;,    \&quot;shell_type\&quot;: \&quot;Themisto\&quot;,    \&quot;version\&quot;:    \&quot;0.9.42\&quot;,    \&quot;needs_mantle\&quot;: false,    \&quot;has_fmc_tcp\&quot;: true,    \&quot;comment\&quot; : \&quot;Some valuable               information for humans (optional)\&quot;  }  &#x60;&#x60;&#x60;  | 
**dcp_file** | **str** | the STATIC dcp checkpoint to be used by users | 
**bit_file** | **str** | The corresponding static bitfile, to write to the FPGA | 
**mcs_file** | **str** | The corresponding mcs file, to write to the board flash | 
**sig_file** | **str** | The corresponding .sig file of the binfile | 
**pr_verify_rpt** | **str** | Result of the &#x60;pr_verify&#x60; command | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


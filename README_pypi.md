# cFSP

This is the **cloudFPGA Support Package (cFSP)** for the [cloudFPGA project](https://www.zurich.ibm.com/cci/cloudFPGA/).

## Requirements

Python 3.6+


## Installation

You can install `cfsp` system-wide through `pip install cfsp`, or user-wide through `pip install -u cfsp`.

It is advised though to do it in an isolated Python environment, e.g. through [virtualenv](https://virtualenv.pypa.io/):

```
virtualenv -p /usr/bin/python3.6 cfenv
source cfenv/bin/activate
pip install cfsp
```

## Usage

Please check the [online documentation](https://cloudfpga.github.io/Doc/pages/CFSPHERE/cfsp.html).

## Development
```bash
git clone git@github.com:cloudFPGA/cFSP.git
cd cFSP
make env
source venv/bin/activate
<add your changes>  (do not forget to increase the `version="x.y.z"` in `setup.py`)
git commit -am "My changes for version x.y.z"
git push
make dist
make upload
```

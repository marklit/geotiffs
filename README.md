# GeoTIFFs

Extract Stack / Pyramid and other metadata from GeoTIFFs as JSON.

## Installation

The following should work on Ubuntu and Ubuntu for Windows.

```bash
$ sudo apt update
$ sudo apt install \
    gdal-bin \
    jq \
    libimage-exiftool-perl \
    libtiff-tools \
    python3-pip \
    python3-virtualenv

$ virtualenv ~/.geotiffs
$ source ~/.geotiffs/bin/activate

$ git clone https://github.com/marklit/geotiffs ~/geotiffs
$ python -m pip install -r ~/geotiffs/requirements.txt
```

If you're using a Mac, install [Homebrew](https://brew.sh/) and then run the following.

```bash
$ brew install \
    gdal \
    git \
    jq \
    libtiff \
    virtualenv

$ virtualenv ~/.geotiffs
$ source ~/.geotiffs/bin/activate

$ git clone https://github.com/marklit/geotiffs ~/geotiffs
$ python -m pip install -r ~/geotiffs/requirements.txt
```

## Usage Example

```bash
$ wget https://umbra-open-data-catalog.s3.amazonaws.com/sar-data/tasks/Suvarnabhumi%20International%20Airport,%20Thailand/79a1d617-8ca7-460a-9327-7f5e3b2f2ba4/2024-05-19-02-50-10_UMBRA-05/2024-05-19-02-50-10_UMBRA-05_GEC.tif

$ python main.py stack 2024-05-19-02-50-10_UMBRA-05_GEC.tif
```

```json
[
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "stack_num": 1,
        "width": 16001
    },
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "Subfile Type": "reduced-resolution image (1 = 0x1)",
        "stack_num": 2,
        "width": 8000
    },
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "Subfile Type": "reduced-resolution image (1 = 0x1)",
        "stack_num": 3,
        "width": 4000
    },
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "Subfile Type": "reduced-resolution image (1 = 0x1)",
        "stack_num": 4,
        "width": 2000
    },
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "Subfile Type": "reduced-resolution image (1 = 0x1)",
        "stack_num": 5,
        "width": 1000
    },
    {
        "Compression Scheme": "LZW",
        "Photometric Interpretation": "min-is-black",
        "Planar Configuration": "single image plane",
        "Predictor": "none 1 (0x1)",
        "Sample Format": "unsigned integer",
        "Subfile Type": "reduced-resolution image (1 = 0x1)",
        "stack_num": 6,
        "width": 500
    }
]
```

```bash
$ python main.py gdal 2024-05-19-02-50-10_UMBRA-05_GEC.tif \
    | jq -S .metadata.RPC
```

```json
{
  "ERR_BIAS": "-1",
  "ERR_RAND": "-1",
  "HEIGHT_OFF": "-30.6818097811395",
  "HEIGHT_SCALE": "1414.21349937646",
  "LAT_OFF": "13.6906792091218",
  "LAT_SCALE": "0.0138548308976396",
  "LINE_DEN_COEFF": "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
  "LINE_NUM_COEFF": "2.61534695853621e-06 0.263132800223868 -0.538642943205665 -0.800117562077938 -1.47036998375427e-05 0.00571980869423115 -0.00119222667629573 8.66752004926049e-05 0.000104518913615887 -0.00532577353969337 1.5155630971275e-05 -7.19242365120972e-07 -7.47120091794499e-07 0.000126862904847366 1.22257299441621e-07 1.45553396081263e-07 -2.46746735713754e-05 -3.77075506029703e-05 -1.13882636497056e-07 -8.36213204065099e-05",
  "LINE_OFF": "8000",
  "LINE_SCALE": "8182.26460167601",
  "LONG_OFF": "100.750015998877",
  "LONG_SCALE": "0.0141698426830041",
  "SAMP_DEN_COEFF": "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
  "SAMP_NUM_COEFF": "2.75289226493849e-06 0.438695382055751 0.21430748317349 -0.872422240127794 -2.49432547473934e-05 0.00605647395335434 -0.00108062581688253 0.000118034972675139 0.000114413101413169 -0.00560586367490182 1.59505756268075e-05 -7.58716939369546e-07 -7.91115881815321e-07 0.000133534808544429 1.27118203863633e-07 1.45733335820918e-07 -2.59723503474079e-05 -3.96847036982472e-05 -1.18988204048819e-07 -8.80190866125779e-05",
  "SAMP_OFF": "8000",
  "SAMP_SCALE": "10046.4207057698"
}
```

## Upgrading Dependencies

If you already have a virtual environment installed then every few weeks, run the following to update the dependencies.

```bash
$ pip install -Ur requirements.txt
```

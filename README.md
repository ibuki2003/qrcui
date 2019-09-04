# QRCode tool on CUI
## Usage
**will be installable with pip and ran without `python main.py`**
**
**Coming soon!**

### Decode
- pass image file with an arg
  - `python main.py -i /path/to/image.png`
- pass image data through pipe
  - `python main.py < /path/to/image.png`
  - `python main.py -i - < /path/to/image.png`

### Encode
- pass text file with an arg
  - `python main.py -i /path/to/document.txt`
- pass string with args
  - `python main.py 'Hello QR'`
  - `python main.py Hello QR`
- pass text data through pipe
  - `echo 'Hi' | python main.py`
  - `echo 'Hi' | python main.py -i -`

## Requirements
- Python3
  - OpenCV
  - pyzbar
  - python-magic
    - python-magic-bin (For only windows)
  - NumPy

## LICENSE
Released under the MIT license.
Please refer to `LICENSE` file for more details.

##

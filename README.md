# About
Simple Python script designed to convert an image file into a VHDL module (.vhd file) containing a ROM with the RGB values of the image.
# Usage
Execute the script and pass the image as an argument:
`./imageToVHDLmodule.py image.jpg`
or
`python3 imageToVHDLmodule.py image.jpg`
or simply execute the script and wait for the prompt to enter the path of the desired image.
# Requirements
Just Pillow. Run:
`pip install requirements.txt`
or simply:
```
python -m pip install --upgrade pip
python -m pip install --upgrade Pillow
```
# Limitations
* At the moment, it does not check the size of the image. If the image is too big, either the script will not work, or the image will be too big for the VGA standard (640x480).
* Colours have to be converted to 12bit, losing lots of colour depth
# Recommendations
* I designed the code for my needs, double check the code and what you need **your** VHDL module to do before you try to synthesize the project.
* Use a python virtual enviroment to avoid any dependency trouble.
# TODO
1. Check image size before execution.
2. Downscale images that are too big.
3. More options when creating the module (component name, architecture name, output options...)
4. Help and examples

# ela-image-forensics
Quick ELA check on an image to help determine if it's real or "photoshopped".  Will produce an ELA and overlay that on the original image to help determine if there are janky bits worth looking closer at.


TO SETUP/ REQUIREMENTS:
 - Python 3
 - Pillow
 
 `pip install -r requirements.txt`
 
 `python3 ela.py 'path\to\image.jpg'`
 
 
 You can alter the ALPHA and SCALE settings to change up the ELA levels/intensity.

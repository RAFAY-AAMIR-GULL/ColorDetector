# ColorDetector
This simple and easy-to-run code will show you the top K or the K most frequently used colors in an image.
It uses Kmean clustering to classify similar colors and will only show you the top K most frequent colors in the image.

<img src='IMG_3758.jpg' width=400>
<img src='Figure_2.png' width=1000>


Please install the following required libraries:  
  
  * [OpenCV-Python](https://pypi.org/project/opencv-python/)
  * [sklearn](https://pypi.org/project/scikit-learn/)
  * [Matplotlib](https://pypi.org/project/matplotlib/)
  
You are all set to use it:)

The value of **"K"** can be changed as per your desire, by default it's a value of 8. Set the path to the image you want the prediction on. By default, the system will pick this [IMG_3758](IMG_3758.jpg)

  After installing all the required libraries, please open up the terminal and run the following command:

```bash
git clone https://github.com/RAFAY-AAMIR-GULL/ColorDetector.git
cd ColorDetector
pip install opencv-python
pip install scikit-learn
pip install matplotlib
python main.py
```

It will take a few seconds to run:)

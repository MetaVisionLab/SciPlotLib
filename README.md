# SciPlotLib

A toolbox for drawing figures commonly found in journal or conference papers.

URL: https://github.com/MetaVisionLab/SciPlotLib

# Install

## Install Package

```shell script
git clone https://github.com/MetaVisionLab/SciPlotLib.git
cd SciPlotLib
python setup.py install
```

## Install Font

If you don't have the Times-New-Roman font in your system, you need to install it manually. For example, in Ubuntu 18.04, you can use the following command:

```shell script
curl https://dl.freefontsfamily.com/download/Times-New-Roman-Font/ -o Times-New-roman.zip
unzip Times-New-roman.zip
cp "Times New Roman"/* /path/to/your/python/site-packages/matplotlib/mpl-data/fonts/ttf/
```

And then, remove the cache of matplotlib.

```shell script
rm ~/.cache/matplotlib -rf
```

# Usage

All sample images are generated by the test function with the same name in the test folder. Users can refer to the corresponding code to prepare their own data and then call the corresponding function.

Due to the lack of compatibility of the SVG format, we do not generate SVG directly but generate PDF. The image can be inserted directly into LaTeX documents. If you want to insert the image into Word or PowerPoint, you can use Illustrator to extract the SVG from the PDF.
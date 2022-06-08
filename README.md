
# GBIF Image Dataset Downloader

A simple script used to download images from gbif.org




## Pre-requisites

Create a python virtual environment using:
```bash
python -m venv /path/to/new/virtual/environment
```

Then, fork the code and place it in the root folder.

Next, activate the virtual environment using (Windows):
```bash
Scripts/activate
```

Check https://docs.python.org/3/library/venv.html for more details.

After the virtual environment is activated, install the dependencies needed using:

```bash
pip install -r requirements.txt
```
    
## How to start

Firstly, head to www.gbif.org and look up a species you would like to use for your dataset. Next, download the darwin archive and extract the files. Lastly, move the **multimedia.txt** file to the root folder containing these python scripts.



## Usage

Run the CsvWriter.py using:
```bash
python CsvWriter.py
```
This will create a new CSV file, containing the URLS to every image in the dataset.

Next, create a folder named "**DownloadedImages**" and Run:
```bash
python Downloader.py
```
The script will then start downloading the images and saving it to the "**DownloadedImages**" folder.

## Disclaimer

Images saved will be in .jpg format.


Some of the images downloaded may be corrupt or broken and I recommend using Bad Peggy to check for these broken images.

Bad Peggy can be found here: 

https://www.majorgeeks.com/files/details/bad_peggy.html
https://github.com/coderslagoon/BadPeggy

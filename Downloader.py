import pandas as pd
import urllib.request
import ssl

# Function to download and save image
def url_to_jpg(i, url, file_path):

    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    ssl._create_default_https_context = ssl._create_unverified_context

    try:
        urllib.request.urlretrieve(url, full_path)
    except Exception:
        print("URL Error")
        pass

    print('{} saved.'.format(filename))

    return None

# Name of the CSV file
FILENAME = 'Urls.csv'

# Folder to save the images
FILE_PATH = 'DownloadedImages/'

# Reads the CSV file
urls = pd.read_csv(FILENAME, encoding='utf-8')

# Calls the download function
for i, url in enumerate(urls):
    url_to_jpg(i, url, FILE_PATH)

# Image Processing and Metadata Analysis

This repository contains a Python script that allows you to download an image from a URL, display its metadata, and check for malicious metadata. It utilizes the following libraries:

- `os`: Provides a way to interact with the operating system.
- `requests`: Enables sending HTTP requests to download the image.
- `PIL` (Python Imaging Library): Allows image processing and extraction of metadata.
- `magic`: Provides a way to determine the file type and analyze its metadata.
- `colorama`: Enables colored output in the terminal.

## Installation

To use this script, follow these steps:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/WarrenMu/image-meta.git
Navigate to the repository's directory:

shell
Copy code
cd repository-name
Install the required dependencies. You can use pip to install them:

shell
Copy code
pip install -r requirements.txt
Usage
To use the script, you need to provide a URL to an image and specify a directory where the image will be saved. Here's an example of how to use the provided functions:

python
Copy code
import os
import requests
from PIL import Image
from PIL.ExifTags import TAGS
import magic
from colorama import init, Fore


# Example usage
url = 'https://example.com/'

License
This project is licensed under the MIT License. Feel free to modify and use the code according to your needs.


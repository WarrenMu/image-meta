import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
from PIL import Image
from PIL.ExifTags import TAGS
import magic
import base64
from colorama import Fore, init

# Initialize colorama
init()

# Set the URL of the website you want to scrape images from
url = input("Enter URL: ")

# Make a request to the URL and get the HTML content
response = requests.get(url)
html_content = response.text

# Use BeautifulSoup to parse the HTML and extract image URLs
soup = BeautifulSoup(html_content, 'html.parser')
img_tags = soup.find_all('img')
img_urls = []

# Get the absolute URLs of the images
for img in img_tags:
    img_src = img.get('src')
    abs_img_url = urljoin(url, img_src)
    img_urls.append(abs_img_url)

# Create a directory to store downloaded images
directory = 'image_directory'
os.makedirs(directory, exist_ok=True)

# Download each image from the extracted URLs
for img_url in img_urls:
    if img_url.startswith('data:image'):
        # Handle Base64 encoded images
        image_data = img_url.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        image_path = os.path.join(directory, 'image.png')
        image.save(image_path)
        print(f'{Fore.GREEN}[+] Image downloaded successfully.{Fore.RESET}')
    else:
        # Handle regular image URLs
        response = requests.get(img_url)
        if response.status_code == 200:
            image_path = os.path.join(directory, img_url.split('/')[-1])
            with open(image_path, 'wb') as f:
                f.write(response.content)
            print(f'{Fore.GREEN}[+] Image downloaded successfully.{Fore.RESET}')
        else:
            print(f'{Fore.RED}[-] Failed to download image.{Fore.RESET}')
        
        # Display metadata for the downloaded image
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            if exif_data is not None:
                print(f'{Fore.CYAN}Image Metadata:')
                for tag, value in exif_data.items():
                    tag_name = TAGS.get(tag, tag)
                    print(f'{tag_name}: {value}')
                    
                    
                # Check for malicious metadata
                mime = magic.from_file(image_path, mime=True)
                if mime.startswith('image'):
                    metadata = magic.from_file(image_path)
                    if 'malicious' in metadata:
                        print(f'{Fore.RED}Malicious metadata detected.')
                    else:
                        print(f'{Fore.GREEN}No malicious metadata found.')
                else:
                    print(f'{Fore.RED}Invalid image file.')
            else:
                print(f'{Fore.YELLOW}No metadata found.')
        except Exception as e:
            print(f'{Fore.RED}Error: {str(e)}{Fore.RESET}')
            
        print()
    else:
        print(f'{Fore.RED}[-] Failed to download image.{Fore.RESET}')

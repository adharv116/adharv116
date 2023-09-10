import os
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.gettyimages.in/photos/aamir-khan-actor'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    os.makedirs('images', exist_ok=True)
    img_tags = soup.find_all('img')

    image_count = 0

    for img_tag in img_tags:
        img_url = img_tag.get('src')

        if img_url and '/id/' in img_url:
            print(img_url)
            image_id = re.search(r'/([^/?]+)(?:\?.*)?$', img_url).group(1)

            filename = f'{image_id}'

            response = requests.get(img_url)
            if response.status_code == 200:
                with open(os.path.join('images', filename), 'wb') as img_file:
                    img_file.write(response.content)
                image_count += 1

    print(f'{image_count} images downloaded successfully.')

else:
    print('Failed to fetch the webpage.')


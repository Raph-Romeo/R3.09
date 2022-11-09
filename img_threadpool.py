import time
import requests
import concurrent.futures
from validators import url # Ce module me permettra de verifier que les liens dans notre liste sont bel et bien des liens.

img_urls = ['https://weareliferuiner.com/wp-content/uploads/2016/10/Google_1476335860616.jpeg.jpg',
            'https://senseient.com/wp-content/uploads/Fastcase.jpg',
        ]


def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    try:
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
    except:
        print(f'An error occured while trying to download {img_name} from {img_url}')
    else:
        print(f"{img_name} was downloaded")


if '__main__' == __name__:
    start = time.perf_counter()
    urls = []
    for i in range(len(img_urls)):
        if url(img_urls[i]):
            urls.append(img_urls[i])
        else:
            print(f'{img_urls[i]} is not a valid URL!')
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

import time
import requests
import threading
from validators import url # Ce module me permettra de verifier que les liens dans notre liste sont bel et bien des liens.

urls = ['https://weareliferuiner.com/wp-content/uploads/2016/10/Google_1476335860616.jpeg.jpg',
            'https://senseient.com/wp-content/uploads/Fastcase.jpg',
    ]


def download_image(img_url, n):
    #print(f'Thread {n} started!')
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    try:
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
    except:
        print(f'An error occured while trying to download {img_name} from {img_url}')
    else:
        print(f"{img_name} was downloaded")
    #finally:
        #print(f'Thread {n} ended')


if '__main__' == __name__:
    start = time.perf_counter()
    threads = []
    for i in range(len(urls)):
        if url(urls[i]):
            thread = threading.Thread(target=download_image, args=[urls[i], i+1])
            threads.append(thread)
        else:
            print(f'{urls[i]} is not a valid URL! (At position {i} in list)')
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")

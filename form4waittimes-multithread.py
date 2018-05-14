# Execution time ~33 seconds for 512 pages of content
import requests
import time
from bs4 import BeautifulSoup
import multiprocessing

PATH = 'C:/Users/Dillon/Desktop/Projects/NFA Wait Times Python/'
BASE_URL = 'https://www.mdshooters.com/showthread.php?s=821a92c041513cf593bad50dd234319f&t=23516'
NUM_PAGES = 512
POOL_SIZE = 32

# get/generate links to parse
def get_links(base_url, n):
    links = []
    for i in range(0,n):
        links.append(BASE_URL + '&page=' + str(i))
    return links

# get list of posts via text
def get_posts(url):
    r = requests.get(url)
    bsoup = BeautifulSoup(r.text, "html.parser")
    posts = bsoup.find_all("div", {"class":"postbitcontrol2"})
    posts_list = []
    for item in posts:
        posts_list.append(item.getText())

    return posts_list

def main():
    start_time = time.time()
    # generate links to process
    links = get_links(BASE_URL, NUM_PAGES)

    # split into pool of threads to process
    with multiprocessing.Pool(POOL_SIZE) as p:
        all_posts = p.map(get_posts, links)
        with open(PATH + "wait_times.txt", "w", encoding="utf-8") as f:
                try:
                    f.write(" ".join(str(post) for post in all_posts))
                    f.close()
                except UnicodeEncodeError:
                    pass
        p.terminate()
        p.join()
    print("--- Finished processing in %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()

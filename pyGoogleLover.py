from icrawler.builtin import GoogleImageCrawler
import shutil, os

keyword = input("Enter keyword/phrase: ")
user_directory = input("Enter name for directory: ")

google_crawler = GoogleImageCrawler(
    feeder_threads=1,
    parser_threads=2,
    downloader_threads=4,
    storage={'root_dir': user_directory})
google_crawler.crawl(keyword=keyword,  max_num=1000, file_idx_offset=0)
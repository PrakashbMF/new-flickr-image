import os
from pathlib import Path

import requests
import environ
from rest_framework.response import Response

env = environ.Env()
BASE_PATH = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_PATH, '.env'))


class FlickrData:
    def __init__(self):
        pass

    def search_image_data(self, page=1, search_text=None):
        method = env("METHOD")
        flickr_source_api = env("FLICKR_SOURCE_API")
        flickr_image_api = env("FLICKR_IMAGE_API")
        flickr_key = env("FLICKR_KEY")

        try:
            search_image_link = flickr_source_api + "?method={}&api_key={}&text={}&nojsoncallback=1&format=json&extras=url_o&page={}&per_page=10".format(
                method, flickr_key, search_text, page)
            response = requests.get(search_image_link)
            response = response.json()
            if response.get("photos").get("photo") is not None:
                page = response.get("photos").get("page")
                total_pages = response.get("photos").get("pages")
                photos = response.get("photos").get("photo")
                urls = []
                for photo in photos:
                    server_id = photo.get("server")
                    id = photo.get("id")
                    secret = photo.get("secret")
                    url = [flickr_image_api + "{}/{}_{}.jpg".format(server_id, id, secret)]
                    urls.append(url)
                return urls, page, total_pages
        except Exception as e:
            return Response({"Error": str(e)})

# print(FlickrData().search_image_data())

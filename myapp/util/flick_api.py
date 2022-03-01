import requests


class FlickrData:
    def __init__(self):
        self.flickr_key = "84efc552dbda8addb5f88014ea8416bd"
        self.flickr_secret = "4bb5c141c3081ae3"
        self.oauth_verifier = "e6ddbc2a62386f27"
        self.flickr_source_api = "https://www.flickr.com/services/rest/"

    def searchImageData(self, page=1, search_text=None):
        method = "flickr.photos.search"
        flickr_key = self.flickr_key
        search_image_link = self.flickr_source_api + "?method={}&api_key={}&text={}&nojsoncallback=1&format=json&extras=url_o&page={}&per_page=5".format(
            method, flickr_key, search_text, page)
        # response = self.getFlickrApiCall(search_image_link)
        response = requests.get(search_image_link)
        response = response.json()

        page = response.get("photos").get("page")
        total_pages = response.get("photos").get("pages")
        photos = response.get("photos").get("photo")
        urls = []
        for x in photos:
            server_id = x.get("server")
            id = x.get("id")
            secret = x.get("secret")
            url = "https://live.staticflickr.com/{}/{}_{}.jpg".format(server_id, id, secret)
            urls.append(url)
        return urls, page, total_pages

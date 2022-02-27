import requests


class FlickrData:
    def __init__(self):
        self.flickr_key = "84efc552dbda8addb5f88014ea8416bd"
        self.flickr_secret = "4bb5c141c3081ae3"
        self.oauth_verifier = "e6ddbc2a62386f27"
        self.flickr_source_api = "https://www.flickr.com/services/rest/"

    def getHeader(self, access_token):
        headers = {
        }
        return headers

    def getFlickrApiCall(self, url):
        response = requests.get(url)
        response = response.json()
        return response

    def getFlickrRecentImage(self):
        method = "flickr.photos.getRecent"
        flickr_key = self.flickr_key
        page = 1
        recent_image_link = self.flickr_source_api + "?method={}&api_key={}&nojsoncallback=1&format=json&page={}&per_page=12".format(
            method, flickr_key, page)
        # print("link ", recent_image_link)
        response = self.getFlickrApiCall(recent_image_link)

        # print(response.get("photos").get("photo")[0].get("id"))
        photos = response.get("photos").get("photo")
        id_list = [x.get("id") for x in photos]
        # print(id_list)

        return id_list

    def getFlickerImageInfo(self, photo_id):
        method = "flickr.photos.getInfo"
        flickr_key = self.flickr_key
        image_info_link = self.flickr_source_api + "?method={}&api_key={}&photo_id={}&nojsoncallback=1&format=json".format(
            method, flickr_key, photo_id)
        response = self.getFlickrApiCall(image_info_link)

        return response

    def imageData(self):
        id_list = self.getFlickrRecentImage()
        response = []
        for x in id_list:
            data = self.getFlickerImageInfo(x)
            # https://live.staticflickr.com/{server-id}/{id}_{secret}.jpg
            server_id = data.get("photo").get("server")
            id = x
            secret = data.get("photo").get("secret")
            url = "https://live.staticflickr.com/{}/{}_{}.jpg".format(server_id, id, secret)
            response.append(url)

        return response

    def searchImageData(self, page=1, searchText=None):
        print("flickr api", page, searchText)
        method = "flickr.photos.search"
        flickr_key = self.flickr_key
        # print(flickr_key)
        # reffered_link = """https://api.flickr.com/services/rest/?method=flickr.photos.search
        #                 &api_key=5f30f8877a137f7cb500122bc7c7a89e
        #                 &format=json
        #                 &nojsoncallback=1
        #                 &text=dogs
        #                 &extras=url_o
        #                 &per_page=5&page=1"""
        search_image_link = self.flickr_source_api + "?method={}&api_key={}&text={}&nojsoncallback=1&format=json&extras=url_o&page={}&per_page=5".format(
            method, flickr_key, searchText, page)
        # print("link ", search_image_link)
        response = self.getFlickrApiCall(search_image_link)

        page = response.get("photos").get("page")
        total_pages = response.get("photos").get("pages")
        # print(page)
        # print(total_pages)
        # print(response.get("photos").get("photo")[0].get("id"))
        photos = response.get("photos").get("photo")
        # id_list = [x.get("id") for x in photos]
        urls = []
        for x in photos:
            # if x.get("url_o") is not None:
            #     urls.append(x.get("url_o"))
            server_id = x.get("server")
            id = x.get("id")
            secret = x.get("secret")
            url = "https://live.staticflickr.com/{}/{}_{}.jpg".format(server_id, id, secret)
            urls.append(url)
        # print("urls ", urls)
        return urls, page, total_pages

    def searchImageDataResponse(self, searchText=None, page=1):
        method = "flickr.photos.search"
        flickr_key = self.flickr_key
        reffered_link = """https://api.flickr.com/services/rest/?method=flickr.photos.search
                        &api_key=5f30f8877a137f7cb500122bc7c7a89e
                        &format=json
                        &nojsoncallback=1
                        &text=dogs
                        &extras=url_o
                        &per_page=5&page=1"""
        search_image_link = self.flickr_source_api + "?method={}&api_key={}&text={}&nojsoncallback=1&format=json&extras=url_o&page={}&per_page=12".format(
            method, flickr_key, searchText, page)
        # print("link ", search_image_link)
        response = self.getFlickrApiCall(search_image_link)

        page = response.get("photos").get("page")
        total_pages = response.get("photos").get("pages")
        # print(page)
        # print(total_pages)
        # print(response.get("photos").get("photo")[0].get("id"))
        photos = response.get("photos").get("photo")
        # id_list = [x.get("id") for x in photos]
        urls = []
        for x in photos:
            if x.get("url_o") is not None:
                urls.append(x)
        print("urls ", urls)
        return urls, page, total_pages


# link = FlickrData().getFlickrRecentImage()
# print(link)

# data = FlickrData().searchImageData()
# print(data)

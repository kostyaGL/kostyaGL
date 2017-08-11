import cStringIO
import json
import math
import operator
import urllib
from PIL import Image, ImageChops

import requests

from config import NASA_API_KEY
from wrappers.base_page import BasePage


class NasaWrapper(BasePage):
    @staticmethod
    def get_curiosity_response_by_sol(sol=1000):
        r = requests.get(
            "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol={sol}&api_key={api_key}"
                .format(sol=sol, api_key=NASA_API_KEY))
        return json.loads(r.text)

    @staticmethod
    def get_curiosity_response_by_earth_date(earth_date):
        r = requests.get(
            "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={earth_date}&api_key={api_key}"
                .format(earth_date=earth_date, api_key=NASA_API_KEY))
        return json.loads(r.text)

    def compare_images(self, im1, im2):
        file1 = self.open_image(im1)
        file2 = self.open_image(im2)
        image = Image.open(file1)
        image2 = Image.open(file2)
        h = ImageChops.difference(image, image2).histogram()
        # calculate rms
        return math.sqrt(reduce(operator.add, map(lambda h, i: h * (i ** 2), h, range(256))
                                ) / (float(image.size[0]) * image2.size[1])) != 0.0

    def sum_of_photos_per_camera(self, by_sol=True):
        res = {}
        if by_sol:
            resp = self.get_curiosity_response_by_sol()
            for i in resp.get('photos'):
                name_camera = i.get('camera').get('name')
                number_of_photos = i.get('rover').get('total_photos')
                res[name_camera] = res.get(name_camera, 0) + number_of_photos
        return res

    @staticmethod
    def open_image(pth):
        return cStringIO.StringIO(urllib.urlopen(pth).read())

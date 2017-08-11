from tests.base_test import BaseTest
from wrappers.nasa_wrapper.wrapper import NasaWrapper


class TestNasaAPI(BaseTest):
    def test_compare_photos_filtered_by_sol_with_by_earth_date(self):
        inst = NasaWrapper()
        # get ten photos made sorted by sol
        first_ten_by_sol = inst.get_curiosity_response_by_sol(sol=1000).get('photos')[:10]
        # get ten photos made sorted by earth_date
        first_ten_by_earth_date = \
            inst.get_curiosity_response_by_earth_date(
                earth_date=first_ten_by_sol[0].get('earth_date')).get('photos')[:10]
        # compare photos by rms
        compared_photos = self.get_result_of_comparing(inst, first_ten_by_sol, first_ten_by_earth_date)
        # compared dict data
        compared_data = self.compare_response_data(first_ten_by_sol, first_ten_by_earth_date)
        assert compared_data
        assert compared_photos is not [], 'res: {}'.format(compared_photos)

    def test_number_not_bigger_than_10_times(self):
        inst = NasaWrapper()
        photos = inst.get_curiosity_response_by_sol(sol=1000).get('photos')
        a = inst.sum_of_photos_per_camera(photos)
        assert all(i >= (max(a.values()) // 10) for i in a.values() if not i == max(a.values())), \
            u"camera: {} has in 10 times bigger number of photos".format(max(a, key=a.get))

    @staticmethod
    def get_result_of_comparing(instance, sorted_by_sol, sorted_by_erth_date):
        return [(value, sorted_by_erth_date[key])
                for key, value in enumerate(sorted_by_sol) if instance.compare_images(value.get('img_src'),
                                                                                      sorted_by_erth_date[key].get(
                                                                                          'img_src'))]

    @staticmethod
    def compare_response_data(sorted_by_sol, sorted_by_erth_date):
        return all([(value == sorted_by_erth_date[key])
                    for key, value in enumerate(sorted_by_sol)])

import json
import appdirs
import os

_version = 'Version 1.0'
_author = 'Sergio Pereira'


class CacheHelper(object):
    def __init__(self, appname):
        self.appname = appname
        self.cache_dir = self.create_cache()

    def create_cache(self):
        """
        Method to create cache directory
        :return:
        """
        _ad = appdirs.AppDirs(appname=self.appname, appauthor=None, version=None, roaming=True, multipath=False)
        cache_dir = _ad.user_cache_dir
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            print("Caching directory {} was created ".format(cache_dir))
        else:
            print("Caching directory {} already exists".format(cache_dir))
        return cache_dir

    def cache_dump(self, data_object, cache_name, indent=None):
        """
        Method serialize to  object as a JSON formatted stream. More information: https://docs.python.org/3/library/json.html#py-to-json-table
        :param data_object: dictionary, list, tuple, str, into, float boolean
        :param cache_name: file name
        :param indent: integer to pretty print JSON formart
        :return:
        """
        file = os.path.join(self.cache_dir, cache_name)
        try:
            with open(file, "w") as output_file:
                json.dump(data_object, output_file, indent)
            print("data object was dumped into {}".format(file))
        except json.JSONDecodeError as e:
            print(e)
        return file

    def cache_load(self, cache_name):
        """
        Method to load serialized object from a binary file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        with open(file, "rb") as input_file:
            try:
                return json.load(input_file)
            except ValueError as e:
                print(e)
        return

    def update_cache(self, data_object, cache_name):
        """
        Method to update existing binary serialized file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        if os.path.exists(file):
            os.remove(file)
        self.cache_dump(data_object, cache_name)

    def delete_cache(self, cache_name):
        """
        Method to delete  binary serialized file.
        :param cache_name: file name
        :return:
        """
        file = '{}/{}'.format(self.cache_dir, cache_name)
        if os.path.exists(file):
            os.remove(file)
        return

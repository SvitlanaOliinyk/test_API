import requests


class PulseRestAPI:
    def __init__(self, resourse):
        self.host = 'pulse-rest-testing.herokuapp.com/'
        self.base_url = 'http://{}/'.format(self.host)
        self.url = self.base_url + resourse + '/'

    def create_obj(self, obj_resourse):
        obj_data = obj_resourse.get_dict_without_id()
        new_book = requests.post(self.url, data=obj_data)
        if new_book.status_code == 201:
            obj_resourse.set_id(new_book.json()['id'])
        return new_book

    def get_list_obj(self):
        list_obj = requests.get(self.url).json()
        return list_obj

    def get_obj(self, obj):
        ob = requests.get(self.url + str(obj['id']) + '/')
        return ob

    def modify_obj(self, obj, obj_mod):
        mod_data = obj_mod.get_dict()
        requests.put(self.url + str(obj['id']) + "/", data=mod_data)
        get_obj = requests.get(self.url + str(obj['id']) + '/')
        return get_obj

    def delete_obj(self, obj):
        del_book = requests.delete(self.url + str(obj.id) + '/')
        return del_book

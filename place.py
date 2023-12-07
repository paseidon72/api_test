import requests


class Test_new_location():

    def test_create_new_location(self):
# Создание базовой ссилки
        base_url = "https://rahulshettyacademy.com"
        key = "?key=qaclick123"
        post_resuorce = "/maps/api/place/add/json"
        post_url = base_url + post_resuorce + key
        print(post_url)
        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }
# Cоздание локации
        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print(str(result_post.status_code) + " : status code")
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print("Very good!!!")
        else:
            print("Bag?????????")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Status is : " + check_info_post)
        assert check_info_post == "OK"
        print("Ensue fine!!!")
        place_id = check_post.get("place_id")
        print("Place_id : " + place_id)
# Проверка создания локации
        get_resuorce = "/maps/api/place/get/json"
        get_url = base_url + get_resuorce + key + "&place_id=" + place_id
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)
        print(str(result_get.status_code) + " : status code")
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Very good!!!")
        else:
            print("Bag?????????")
# Изменение локации
        put_resuorce = "/maps/api/place/update/json"
        put_url = base_url + put_resuorce + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = requests.put(put_url, json=json_for_update_new_location)
        print(result_put.text)
        print(str(result_put.status_code) + " : status code")
        assert 200 == result_put.status_code
        if result_put.status_code == 200:
            print("Very good!!!")
        else:
            print("Bag?????????")
        check_put = result_put.json()
        check_put_info = check_put.get("msg")
        print("Ok : " + check_put_info)
        assert check_put_info == "Address successfully updated"
        print("Very good!!!!!!!")
# Проверка изменения локации
        result_get = requests.get(get_url)
        print(result_get.text)
        print(str(result_get.status_code) + " : status code")
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print("Very good!!!")
        else:
            print("Bag?????????")


        check_address = result_get.json()
        check_address_info = check_address.get("address")
        print("Ok : " + check_address_info)
        assert check_address_info == "100 Lenina street, RU"
        print("Very good!!!!!!!")


new_place = Test_new_location()
new_place.test_create_new_location()



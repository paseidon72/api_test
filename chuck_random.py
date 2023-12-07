import requests

class Test_new_joke():

    def __init__(self):
        pass

    # def test_create_new_random_joke(self):
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print(str(result.status_code) + " : status code")
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print("Very good!!!")
    #     else:
    #         print("Bag?????????")
    #     result.encoding = "utf-8"
    #     print(result.text)
    #     check = result.json()
    #     check_info = check.get("categories")
    #     print(check_info)
    #     assert check_info == []
    #     print("categories very good!!!")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Very good Chuck")
    #     else:
    #         print("Chuck is not result")


    def test_create_new_random_categories_joke(self):
        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print(str(result.status_code) + " : status code")
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Very good!!!")
        else:
            print("Bag?????????")
        result.encoding = "utf-8"
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("categories very good!!!")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Very good Chuck")
        # else:
        #     print("Chuck is not result")


# random_joke = Test_new_joke()
# random_joke.test_create_new_random_joke()
sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()





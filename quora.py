import time
from selenium import webdriver


def find(query):
    driver = webdriver.Chrome()
    quora_url = "https://www.quora.com/"
    driver.get(quora_url + query)
    try:
        time.sleep(5)
        print(driver.title)
        pods = driver.find_element_by_class_name("u-serif-font-main--regular")
        result = ""
        for pod in pods:
            result += pod.text + "\n"
        # db00000000000000000000000
        driver.close()
        if len(result) > 15:
            print(result)
            return result
        else:
            return None
    except Exception as e:
        driver.close()
        return e


if __name__ == "__main__":
    print('quora search code')
    q=input('what do you want to search')
    find(q)
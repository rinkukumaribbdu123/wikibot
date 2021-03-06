import time
from selenium import webdriver


def find(query):
    driver = webdriver.Chrome()
    stackoverflow_url = "https://stackoverflow.com/search?q="
    driver.get(stackoverflow_url + query)
    try:
        time.sleep(5)
        print(driver.title)
        answers = driver.find_element_by_id("answers")
        pods = answers.find_element_by_class_name("pod")
        result = ""
        for pod in pods:
            result += pod.text + "\n"
        # db
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
    print('Stack overflow search code')
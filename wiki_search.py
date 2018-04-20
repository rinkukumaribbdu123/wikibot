import time
from selenium import webdriver


def find(query):
    driver = webdriver.Chrome()
    wiki_url = "https://en.wikipedia.org/wiki/"
    driver.get(wiki_url + query)
    try:
        time.sleep(5)
        print(driver.title)
        answers = driver.find_element_by_id("content")
        pods = answers.find_element_by_xpath("mw-content-text")
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
    print('wikipedia search code')
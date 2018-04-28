import time
from selenium import webdriver


def find(query):
    driver = webdriver.Chrome()
    quora_url = "https://www.quora.com/search?q="
    driver.get(quora_url + query)
    try:
        time.sleep(5)
        print(driver.title)
        pods = driver.find_elements_by_css_selector('div.pagedlist_item')
        result = ""
        print(len(pods))
        time.sleep(2)
        for pod in pods:
            try:
                answerSnippet = pod.find_element_by_class_name('SearchResultSnippet')
                try:
                    link = answerSnippet.find_element_by_class_name('more_link')
                    link.click()
                    time.sleep(1)
                    qText = answerSnippet.find_element_by_class_name('ui_qtext_rendered_qtext')
                    text = qText.text
                    break
                except:
                    answer = answerSnippet.find_element_by_class_name('rendered_qtext')
                    text = answer.text
            except Exception as e:
                answerSnippet = None
                print(e)
        # driver.close()
        if len(result) > 15:
            print(result)
        else:
            return('No result')
    except Exception as e:
        driver.close()
        return 'error'


if __name__ == "__main__":
    print('quora search code')
    q = input('what do you want to search')
    find(q)

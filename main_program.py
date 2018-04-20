from selenium import webdriver
import wolfram_search
import wiki_search
import microphone
import text_to_speech
import quora
query = microphone.speech_to_text()
# Create a new instance of the Firefox driver
result_quora=quora.search.find(query)
result_w = wolfram_search.find(query)
result_wiki = wiki_search.find(query)

try:
    if len(result_w) > 10:
        print(result_w)
        text_to_speech.speak_content(result_w)
    elif len(result_wiki) >10:
        print(result_wiki)
except:
    print(result_w)
    print(result_wiki)


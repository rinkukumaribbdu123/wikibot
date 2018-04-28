from selenium import webdriver
import wolfram_search
import wiki_search
import microphone
import text_to_speech
import quora_search

def main_program(self):
    query = microphone.speech_to_text()
    # Create a new instance of the Firefox driver
    result_wiki = wiki_search.find(query)
    answer = wolfram_search.find(query)


    if answer and len(answer) >= 10:
        print(answer)
        text_to_speech.speak_content(answer)
    elif result_wiki and len(result_wiki) > 10:
        print(result_wiki)
        text_to_speech.speak_content(result_wiki)
    else:
        print("Sorry , this is way above my understanding")


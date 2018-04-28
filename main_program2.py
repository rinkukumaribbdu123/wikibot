import wolfram_search
import wiki_search
import microphone
import text_to_speech


def runit(self):
    query = microphone.speech_to_text()
    # Create a new instance of the Firefox driver
    result_wiki = wiki_search.find(query)
    answer = wolfram_search.find(query)

    if answer and len(answer) >= 10:
        text_to_speech.speak_content(answer)
        self.ans = answer
        self.label_4.setText(self.ans)
        return
    elif result_wiki and len(result_wiki) > 10:
        text_to_speech.speak_content(result_wiki)
        self.ans = result_wiki
        self.label_4.setText(self.ans)
        return
    else:
        self.ans = None
        self.label_4.setText("No Search Result Found.")
        return



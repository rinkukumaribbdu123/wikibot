import time
import wikipedia


def find(query):
    try:
        summary = wikipedia.summary(query)
    except:
        summary = "could you be more specific"
    return summary


if __name__ == "__main__":
    print('wikipedia search code')
    result = find(query='stock market')
    print(result)

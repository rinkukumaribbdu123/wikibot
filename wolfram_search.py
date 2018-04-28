import time
import wolframalpha

'''
{
'@title': 'Definitions',
'@scanner': 'Data',
'@id': 'Definition:WordData',
'@position': '200',
'@error': 'false',
'@numsubpods': '1',
'@primary': 'true',
'subpod': {
    '@title': '',
    'img': {
        '@src': 'https://www4f.wolframalpha.com/Calculate/MSP/MSP53781bcebicfe31140e8000020b148d903f5d53f?MSPStoreType=image/gif&s=28',
        '@alt': '1 | verb | put or set (seeds, seedlings, or plants) into the ground 2 | verb | fix or set securely or deeply 3 | verb | set up or lay the groundwork for 4 | verb | place into a river 5 | verb | place something or someone in a certain position in order to secretly observe or deceive 6 | verb | put firmly in the mind 7 | noun | buildings for carrying on industrial labor 8 | noun | (botany) a living organism lacking the power of locomotion (10 meanings)', '@title': '1 | verb | put or set (seeds, seedlings, or plants) into the ground 2 | verb | fix or set securely or deeply 3 | verb | set up or lay the groundwork for 4 | verb | place into a river 5 | verb | place something or someone in a certain position in order to secretly observe or deceive 6 | verb | put firmly in the mind 7 | noun | buildings for carrying on industrial labor 8 | noun | (botany) a living organism lacking the power of locomotion (10 meanings)', '@width': '546', '@height': '253'}, 'plaintext': '1 | verb | put or set (seeds, seedlings, or plants) into the ground\n2 | verb | fix or set securely or deeply\n3 | verb | set up or lay the groundwork for\n4 | verb | place into a river\n5 | verb | place something or someone in a certain position in order to secretly observe or deceive\n6 | verb | put firmly in the mind\n7 | noun | buildings for carrying on industrial labor\n8 | noun | (botany) a living organism lacking the power of locomotion\n(10 meanings)'}, 'states': {'@count': '2', 'state': [{'@name': 'Show all', '@input': 'Definition:WordData__Show all'}, {'@name': 'More', '@input': 'Definition:WordData__More'}]}}
'''

'''
{'@title': 'Basic information', '@scanner': 'Data', '@id': 'BasicInformation:PeopleData', '@position': '200', '@error': 'false', '@numsubpods': '1', 'subpod': {'@title': '', 'img': {'@src': 'https://www5a.wolframalpha.com/Calculate/MSP/MSP15141464h1g79g1b494c0000353a5ee2f4a37959?MSPStoreType=image/gif&s=44', '@alt': 'full name | Albert Einstein date of birth | Friday, March 14, 1879 (139 years ago) place of birth | Ulm, Baden-Wurttemberg, Germany date of death | Monday, April 18, 1955 (age: 76 years)   (63 years ago) place of death | Princeton, New Jersey, United States', '@title': 'full name | Albert Einstein date of birth | Friday, March 14, 1879 (139 years ago) place of birth | Ulm, Baden-Wurttemberg, Germany date of death | Monday, April 18, 1955 (age: 76 years)   (63 years ago) place of death | Princeton, New Jersey, United States', '@width': '397', '@height': '181'}, 'plaintext': 'full name | Albert Einstein\ndate of birth | Friday, March 14, 1879 (139 years ago)\nplace of birth | Ulm, Baden-Wurttemberg, Germany\ndate of death | Monday, April 18, 1955 (age: 76 years) \n (63 years ago)\nplace of death | Princeton, New Jersey, United States'}}


'''


def find(query):
    answer_text = None
    app_id = "VR3V3L-3LQ39KPVJA"
    client = wolframalpha.Client(app_id)
    res = client.query(query)
    for data in res.pods:
        if data.get('@title') == 'Definitions':
            if data.get('subpod').get('img').get('@alt'):
                answer_text = (data.get('subpod').get('img').get('@alt'))
            break
        elif data.get('@title') == 'Basic information':
            if data.get('subpod').get('img').get('@alt'):
                answer_text = (data.get('subpod').get('img').get('@alt'))
            break
    return answer_text


if __name__ == "__main__":
    print('wolfram search code')
    answer = find("Albert Einstien")
    print(answer)

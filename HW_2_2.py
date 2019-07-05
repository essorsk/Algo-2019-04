#В приложении парсинга википедии получить первую ссылку на соседнюю страницу
#и вывести все значимые слова из неё. Результат записать в файл в форматированном виде
#2.* Научить приложение определять количество ссылок в статье.
#Спарсить каждую ссылку и результаты записать в отдельные файлы.

from requests import get
import json
import pprint
import re


def get_link(topic):
    link = "https://ru.wikipedia.org/wiki/" + topic.capitalize()
    return link

def get_topic_page(topic):
    link = get_link(topic)
    html = get(link).text
    return html

def get_relink(topic):
    html_content = get_topic_page(topic)
    relink = re.findall(r'<li><a rel="nofollow" class="external text" href=[\'"]?([^\'" >]+)', html_content)
    #print( '\n'.join(relink))
    return relink

def file_data(topic):
    new_link = get_relink(topic)
    #считаем строки
    i =0
    for line in new_link:
        i+=1
        new_html = get(line).text
        file = open(topic + str(i) +'.txt','w', encoding='UTF-8')
        file.write(new_html)
        file.close()
    print(f'По запросу {topic} найдено {i} дополнительных ссылок')
    
 

topic = 'ром'
lists = file_data(topic)
#pprint.pprint(lists)

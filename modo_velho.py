from bs4 import BeautifulSoup
import requests
import emoji

def web():

  headers = requests.utils.default_headers()
  headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'})

  data = requests.get('https://br.investing.com/economic-calendar/', headers=headers)
  resultados = []
  result = str()
  if data.status_code == requests.codes.ok:
    info =  BeautifulSoup(data.text, 'html.parser')
    blocos = ((info.find('table', {'id': 'economicCalendarData'})).find('tbody')).findAll('tr', {'class': 'js-event-item'})
    
    for blocos2 in blocos:
          impacto = str((blocos2.find('td',{'class': 'sentiment'})).get('data-img_key')).replace('bull', '')
          if(impacto=="1"):
            impacto = (emoji.emojize(':star:'))
          if(impacto=="2"):
            impacto = (emoji.emojize(':star::star:'))
          if(impacto=="3"):
            impacto = (emoji.emojize(':star::star::star:'))
          hora = str(blocos2.get('data-event-datetime')).replace('/', '-')
          moeda = (blocos2.find('td', {'class': 'left flagCur noWrap'})).text.strip()
          horas = (hora[10:16])

          resultados.append({'par': moeda,'horas': horas, 'impacto': impacto}) 
        
  for info in resultados:
    result+=str("{0} {1} {2} {3} {4} {5} {6}".format('PARIDADE: ', info['par'],'\nHORA: ', info['horas'], '\nIMPACTO: ', info['impacto'], '\n------------\n'))
  return result
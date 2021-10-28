from bs4 import BeautifulSoup
import requests
import emoji

def webscraping():

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
          if(moeda=="USD"):
            moeda=(emoji.emojize('\U0001F1FA\U0001F1F8USD'))
          if(moeda=="GBP"):
            moeda=(emoji.emojize('\U0001F1EC\U0001F1E7GBP'))
          if(moeda=="EUR"):
            moeda=(emoji.emojize('\U0001F1E9\U0001F1EAEUR'))
          if(moeda=="MXN"):
            moeda=(emoji.emojize('\U0001F1F2\U0001F1FDMXN'))
          if(moeda=="IDR"):
            moeda=(emoji.emojize('\U0001F1EE\U0001F1E9IDR'))
          if(moeda=="SGD"):
            moeda=(emoji.emojize('\U0001F1F8\U0001F1ECSGD'))
          if(moeda=="INR"):
            moeda=(emoji.emojize('\U0001F1EE\U0001F1F3INR'))
          if(moeda=="CAD"):
            moeda=(emoji.emojize('\U0001F1E8\U0001F1E6CAD'))
          if(moeda=="AUD"):
            moeda=(emoji.emojize('\U0001F1E6\U0001F1FAAUD'))
          if(moeda=="HKD"):
            moeda=(emoji.emojize('\U0001F1ED\U0001F1F0HKD'))
          if(moeda=="JPY"):
            moeda=(emoji.emojize('\U0001F1EF\U0001F1F5JPY'))
          if(moeda=="NZD"):
            moeda=(emoji.emojize('\U0001F1F3\U0001F1FFNZD'))
          if(moeda=="CHF"):
            moeda=(emoji.emojize('\U0001F1E8\U0001F1EDCHF'))
          if(moeda=="BRL"):
            moeda=(emoji.emojize('\U0001F1E7\U0001F1F7BRL'))
          if(moeda=="CNY"):
            moeda=(emoji.emojize('\U0001F1E8\U0001F1F3CNY'))
          if(moeda=="ZAR"):
            moeda=(emoji.emojize('\U0001F1FF\U0001F1E6ZAR'))
          #Hora
          horas = (hora[10:16])

          resultados.append({'moeda':moeda,'horas':horas,'impacto':impacto}) 
        
  for info in resultados:
    result+=str("{0} {1} {2} {3}".format(info['horas'],info['moeda'],info['impacto'],"\n"))
  return result
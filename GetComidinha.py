from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
import unicodedata
import urllib

def GetComidinha():
    try:
        chrome_options = Options()
        # chrome_options.headless = True
        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://aluno.cefsa.edu.br/')
        
        sleep(4)

        driver.find_element("xpath", '//*[@id="Usuario"]').send_keys('082190024')
        driver.find_element("xpath", '//*[@id="senhaAluno"]').send_keys('Nestruta3')
        
        driver.find_element("xpath", '//*[@id="alunos"]/button').click()
        
        sleep(5)
        
        cardapio = driver.find_element("id", 'colapseCardapioSemanal').get_attribute('innerText')
        
        cardapio = cardapio.split('\n')
        
        newCardapio = []
        
        for line in cardapio:
            line = unicodedata.normalize('NFKC', line)
            line = line.strip()
            if line != '' and line != ' ': newCardapio.append(line)
            
        counter = ''
        result = { 
            'Segunda-Feira': '',
            'Terça-feira': '',
            'Quarta-feira': '',
            'Quinta-feira': '',
            'Sexta-feira': ''
        }
        
        tempString = ''
            
        for line in newCardapio:
            if 'Segunda-Feira' in line: 
                counter = 'Segunda-Feira'
            elif 'Terça-feira' in line:
                result[counter] = tempString
                tempString = ''
                counter = 'Terça-feira'
            elif 'Quarta-feira' in line:
                result[counter] = tempString
                tempString = ''
                counter = 'Quarta-feira'
            elif 'Quinta-feira' in line:
                result[counter] = tempString
                tempString = ''
                counter = 'Quinta-feira'
            elif 'Sexta-feira' in line:
                result[counter] = tempString
                tempString = ''
                counter = 'Sexta-feira'
            elif 'sujeito a alterações' in line:
                result[counter] = tempString
                break
            if counter != '':
                tempString += line + '\n'
                
        return result
    
    except:
        return 'Deu erro, consulte  o administrador do BOT'
    
    finally:
        driver.close()

if __name__ == '__main__':

    print(GetComidinha())

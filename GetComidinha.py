from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from time import sleep
import unicodedata

def GetComidinha():
    
    edge_options = Options()
    edge_options.headless = True
    driver = webdriver.Edge(options=edge_options)
    try:
        driver.get('https://aluno.cefsa.edu.br/')
        
        sleep(4)
        
        driver.find_element("xpath", '//*[@id="fechar"]').click()
        
        sleep(1)

        driver.find_element("xpath", '//*[@id="Usuario"]').send_keys('082190024')
        
        sleep(1)
        
        driver.find_element("xpath", '//*[@id="senhaAluno"]').send_keys('Nestruta3')
        
        sleep(1)
        
        driver.find_element("xpath", '//*[@id="alunos"]/button').click()
        
        sleep(8)
        
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
    print(GetComidinha()['Quinta-feira'])
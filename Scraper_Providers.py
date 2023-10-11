
############################################################################
#Finding all Game Providers,their respective Links,
#Games of each provider and Casino games in Market
###########################################################################3


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #(html mas lento)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

import pandas as pd ##It will be used later

##OPTIONS#
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


   ##DRIVER
driver_path="F:\chromedriver.exe"

    ##WEB
driver=webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get("https://slotcatalog.com/en")

time.sleep(3)

    ##Close spam 
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/button")))\
    .click()
time.sleep(3)
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[10]/div/div[1]")))\
    .click()
time.sleep(3)

    ##Providers
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/div/div[7]/nav/ul/li[3]/a')))\
        .click()
time.sleep(5)


####### PRELOAD ALL SHEETS OF PROVIDERS####

for i in range(23):   ##24 sheets in total
    WebDriverWait(driver, 10)\
        .until(EC.element_to_be_clickable((By.XPATH, '//div/div[@class="providerCard loadMore"]')))\
            .click()
    time.sleep(60)
    
#####Lists: Provider Name , Provider Name , Games of each Provider and Casino Games in Market  
  

        ###Providers NAME#####
        
Provides_Name=driver.find_elements(By.XPATH,'//div/div/div/h3/a[@title]')

List_Providers_Name=list()

for Provides_Name in Provides_Name:
    
    Provides_Name=Provides_Name.text

    List_Providers_Name.append(Provides_Name)
    
print(len(List_Providers_Name))

time.sleep(100)


        ###PROVIDERS WEB#####     

        
Providers_Web=driver.find_elements(By.XPATH,'//div/div/div/div/div/div/h3/a')
         
List_Providers_Web=list()

for Providers_Web in Providers_Web:
    
    Providers_Web=Providers_Web.get_attribute('href')  
      
    List_Providers_Web.append(Providers_Web)

time.sleep(100)

   
#Data Frame with Providers and Links
      
df_Links_Provider=pd.DataFrame({"Provider":List_Providers_Name,"Links provider":List_Providers_Web})  
print(df_Links_Provider)

df_Links_Provider.to_csv("Providers and Links.csv")  #Save-csv
df_Links_Provider.to_csv("Providers and Links")  #Save-notebook



        ###GAMES OF EACH PROVIDER####
        

Providers_Games=driver.find_elements(By.XPATH,'//div/div/div/div/div/div/div/div/div/div/a[contains(@href,"BrandGames") and contains(@title,"See")]')
        
List_Providers_Games=list()

for Providers_Games in Providers_Games:
    
    Providers_Games=Providers_Games.get_attribute('title') 
        
    List_Providers_Games.append(Providers_Games)
    


        ###CASINO GAMES IN MARKET###

        
Providers_Casinos=driver.find_elements(By.XPATH,'//div/div/div/div/div/div/div/div/div/div/a[contains(@href,"BrandCasino")and contains(@title,"See")]')
         
List_Providers_Casinos=list()

for Providers_Casinos in Providers_Casinos:
    
    Providers_Casinos=Providers_Casinos.get_attribute('title') 
    
    List_Providers_Casinos.append(Providers_Casinos)
 


#####Filter games####

       ####Not all providers have information about number of games
       #####List Name and List Provider Games
          ###Filtering data
     
List_intersecction_1=list()
List_intersecction_2=list()

for i in range(0,len(List_Providers_Games)):
    
    if List_Providers_Name[i] in List_Providers_Games[i]: 
        
        
        import re
        List_Providers_Games[i]=re.sub("[^0-9]","",List_Providers_Games[i])  #Remove all string characters                                           
        List_intersecction_1.append(List_Providers_Games[i])
    
        List_intersecction_2.append(List_Providers_Name[i])
        


       
#Data Frame with Providers and Games for Provider
      
df_Provider_Games=pd.DataFrame({"Provider":List_intersecction_2,"Games for Provider":List_intersecction_1})  
print(df_Provider_Games)


df_Provider_Games.to_csv("Providers and Game for Provider.csv")   #Save-csv
df_Provider_Games.to_csv("Providers and Game for Provider")  #Save-notebook


      
       ####Not all providers have information about casinos games in the market
       ####List Name and List Casino in the market
          ###Filtering data            

   
List_intersecction_3=list()
List_intersecction_4=list()

for i in range(0,len(List_Providers_Casinos)):
    
    if List_Providers_Name[i] in List_Providers_Casinos[i]: 
        
        import re
        List_Providers_Casinos[i]=re.sub("[^0-9]","",List_Providers_Casinos[i])  #Remove all string characters                                           
        List_intersecction_3.append(List_Providers_Casinos[i])
        List_intersecction_4.append(List_Providers_Name[i])
        

        
        
#Data Frame with Providers and Casinos games in the market
        
df_Provider_Casino=pd.DataFrame({"Provider":List_intersecction_4,"Casinos games in the mark":List_intersecction_3})  
print(df_Provider_Casino)

df_Provider_Games.to_csv("Providers and Casinos games in the market.csv")   #Save-csv
df_Provider_Games.to_csv("Providers and Casinos games in the market")  #Save-notebook

driver.quit()
                



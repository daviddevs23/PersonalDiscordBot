import discord, os, requests, re, random
from discord.ext import commands
from bs4 import BeautifulSoup


def scrape_word(link):
    response = requests.get(url=link)

    soup = BeautifulSoup(response.content, "html.parser")
    html = soup.find_all('div', class_='wordlist-item')
    words = []
    
    for word in html:
        words.append(word.text)

    return random.choice(words)


class Roast(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roast(self, ctx, user=""):

        adj_list    =   [
                            "https://www.enchantedlearning.com/wordlist/adjectives.shtml",
                            "https://www.enchantedlearning.com/wordlist/negativewords.shtml"
                        ]                                                       
                                                                             
        noun_list   =   [                                                       
                            "https://www.enchantedlearning.com/wordlist/householddevices.shtml",
                            "https://www.enchantedlearning.com/wordlist/cookingtools.shtml",
                            "https://www.enchantedlearning.com/wordlist/farm.shtml",
                        ]  
        adj = scrape_word(random.choice(adj_list))                              
                                                                                  
        adj2 = scrape_word(random.choice(adj_list))                             
                                                                                
        noun = scrape_word(random.choice(noun_list))                            
                                                                                
        noun2 = scrape_word(random.choice(noun_list))                           
                                                                                
        return_string1 = ""                                                     
                                                                                
        return_string2 = ""                                                     
                                                                                
        return_string3 = ""                                                     
                                                                                
        if user:                                                                
            return_string1 = user + ", you are a " + adj + " " + noun + "."     
        else:                                                                   
            return_string1 = "You are a " + adj + " " + noun + "."              
                                                                                
        if user:                                                                
            return_string2 = user + ", you are as useless as a " + noun + " on a " + noun2 + "."
        else:                                                                   
            return_string2 = "You are as useless as a " + noun + " on a " + noun2 + "."
                                                                                
        if user:                                                                
            return_string3 = user + ", you " + adj + " " + adj2 + " " + noun + "."
        else:                                                                   
            return_string3 = "You " + adj + " " + adj2 + " " + noun + "."       
                                                                                
                                                                                
                                                                                
        strings = []                                                            
                                                                                
        strings.append(return_string1)                                          
        strings.append(return_string2)                                          
        strings.append(return_string3)                                          
                                                                                
        await ctx.send(random.choice(strings)) 

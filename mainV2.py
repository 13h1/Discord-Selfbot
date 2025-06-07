#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
#Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind #Don't skid because its bad and not kind
import discord
import asyncio
import threading
import os
import time
import random  
from colorama import Fore, Style, init
init(autoreset=True)

PACKING = False
USER_BALANCES = {}  # Dictionnaire pour stocker les soldes des utilisateurs

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def splash():
    clear()
    print(f"""{Fore.RED}
██   ██ ██    ██ ███    ███ ██ ██      ██  █████  ████████ ███████ ██    ██ ██████  
██   ██ ██    ██ ████  ████ ██ ██      ██ ██   ██    ██    ██      ██    ██ ██   ██ 
███████ ██    ██ ██ ████ ██ ██ ██      ██ ███████    ██    █████   ██    ██ ██████  
██   ██ ██    ██ ██  ██  ██ ██ ██      ██ ██   ██    ██    ██      ██    ██ ██   ██ 
██   ██  ██████  ██      ██ ██ ███████ ██ ██   ██    ██    ███████  ██████  ██   ██ {Style.RESET_ALL}
{Fore.MAGENTA}                  {Style.RESET_ALL}

{Fore.CYAN}    Select an option:{Style.RESET_ALL}
{Fore.YELLOW}    [1]{Style.RESET_ALL} un tokens
{Fore.YELLOW}    [2]{Style.RESET_ALL} Multi Tokens
{Fore.YELLOW}    [3]{Style.RESET_ALL} Credits
{Fore.YELLOW}    [4]{Style.RESET_ALL} Exit
""")

def read_lines(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[ERROR] {file} not found.")
        return []

def to_ladder_format(text):
    return '\n'.join(word.upper() for word in text.split())

def get_balance(user_id):
    return USER_BALANCES.get(user_id, 1000)  

def update_balance(user_id, amount):
    if user_id not in USER_BALANCES:
        USER_BALANCES[user_id] = 1000
    USER_BALANCES[user_id] += amount
    return USER_BALANCES[user_id]

def run_client(token):
    client = discord.Client()
    REACT_USER_ID = None
    REACT_EMOJI = None
    global PACKING
    ROTATE_STATUS = True  

    async def status_rotator():
        await client.wait_until_ready()
        while ROTATE_STATUS:
            statuses = read_lines("status.txt")
            if not statuses:
                await asyncio.sleep(10)
                continue
            status_text = random.choice(statuses)
            status_type = random.choice(["playing", "watching", "listening"])

            if status_type == "playing":
                activity = discord.Game(name=status_text)
            elif status_type == "watching":
                activity = discord.Activity(type=discord.ActivityType.watching, name=status_text)
            else:
                activity = discord.Activity(type=discord.ActivityType.listening, name=status_text)

            try:
                await client.change_presence(activity=activity)
            except Exception as e:
                print(f"[Status Rotation Error] {e}")
            await asyncio.sleep(10)

    async def start_packing(channel, user_mention, lines, ladder=False):
        global PACKING
        PACKING = True
        for line in lines:
            if not PACKING:
                break
            msg = f"{user_mention}\n{to_ladder_format(line)}" if ladder else f"{user_mention} {line}"
            await channel.send(msg)
            await asyncio.sleep(0.4)
        PACKING = False

    @client.event
    async def on_ready():
        print(f"\n[🟢] co en tant que: {client.user}")
        print("\n╔═══════════════════════════════════════╗")
        print("║         humiliateur2keh                 ║")
        print("╠═══════════════════════════════════════  ╣")
        print("║ >debite       >long         >packend    ║")
        print("║ >nul          >honte        >peur       ║")
        print("║ >react        >menu         >stream     ║")
        print("║ >playing      >watching     >listening  ║")
        print("║ >clearstatus  >dm           >purge      ║")
        print("║ >spam        >coinflip     >casino     ║")
        print("╚═══════════════════════════════════════  ╝\n")
        client.loop.create_task(status_rotator())

    @client.event
    async def on_message(message):
        YOUR_USER_ID = 1331352861619257345
        
        if message.author.id != YOUR_USER_ID:
            return
            
        nonlocal REACT_USER_ID, REACT_EMOJI
        global PACKING

        if REACT_USER_ID and REACT_EMOJI:
            if message.author.id == REACT_USER_ID or message.author.id == client.user.id:
                try:
                    await message.add_reaction(REACT_EMOJI)
                except Exception as e:
                    print(f"[React Error] {e}")

        if not message.content.startswith(">"):
            return

        args = message.content.split()
        cmd = args[0].lower()
 
        if cmd == ">fin":
            PACKING = False
            await message.channel.send("[🪽] fin de l'humiliation.")
            
        elif cmd == ">debite" and len(args) >= 2:
            lines = read_lines("debit.txt")
            await start_packing(message.channel, args[1], lines)
        elif cmd == ">long" and len(args) >= 2:
            lines = read_lines("debit.txt")
            await start_packing(message.channel, args[1], lines, ladder=True)
        elif cmd == ">nul" and len(args) >= 2:
            lines = read_lines("nul.txt")
            await start_packing(message.channel, args[1], lines, ladder=True)
        elif cmd == ">honte" and len(args) >= 2:
            lines = read_lines("humiliation.txt")
            await start_packing(message.channel, args[1], lines, ladder=True)
        elif cmd == ">peur" and len(args) >= 2:
            lines = read_lines("crie.txt")
            await start_packing(message.channel, args[1], lines, ladder=False)
            
        elif cmd == ">react" and len(args) >= 3:
            mention = args[1]
            emoji = args[2]
            if mention.startswith("<@") and mention.endswith(">"):
                try:
                    user_id = int(mention.replace("<@", "").replace("!", "").replace(">", ""))
                    REACT_USER_ID = user_id
                    REACT_EMOJI = emoji
                    await message.channel.send(f" React a {mention} et toi avec {emoji}")
                except:
                    await message.channel.send("  format invalide.")
            else:
                await message.channel.send(" Invalid @mention format.")
                
        elif cmd == ">stopr":
            REACT_USER_ID = None
            REACT_EMOJI = None
            await message.channel.send(" arrêt...")
            
        elif cmd == ">coinflip":
            if len(args) < 3:
                await message.channel.send("Usage: >coinflip <pile/face> <mise>")
                return
                
            choice = args[1].lower()
            if choice not in ["pile", "face"]:
                await message.channel.send("Choisissez 'pile' ou 'face'")
                return
                
            try:
                bet = int(args[2])
                if bet <= 0:
                    await message.channel.send("La mise doit être positive")
                    return
                    
                user_id = message.author.id
                balance = get_balance(user_id)
                
                if bet > balance:
                    await message.channel.send(f"Solde insuffisant! Votre solde: {balance}")
                    return
                    
                result = random.choice(["pile", "face"])
                
                if result == choice:
                    win_amount = bet * 2
                    new_balance = update_balance(user_id, win_amount)
                    await message.channel.send(f"🎉 C'est {result}! Vous gagnez {win_amount}! Nouveau solde: {new_balance}")
                else:
                    new_balance = update_balance(user_id, -bet)
                    await message.channel.send(f"💀 C'est {result}! Vous perdez {bet}. Nouveau solde: {new_balance}")
                    
            except ValueError:
                await message.channel.send("Mise invalide. Utilisez un nombre entier.")
                
        elif cmd == ">casino":
            if len(args) < 3:
                await message.channel.send("Usage: >casino <1-100> <mise>")
                return
                
            try:
                number = int(args[1])
                bet = int(args[2])
                
                if number < 1 or number > 100:
                    await message.channel.send("Choisissez un nombre entre 1 et 100")
                    return
                    
                if bet <= 0:
                    await message.channel.send("La mise doit être positive")
                    return
                    
                user_id = message.author.id
                balance = get_balance(user_id)
                
                if bet > balance:
                    await message.channel.send(f"Solde insuffisant! Votre solde: {balance}")
                    return
                    
                winning_number = random.randint(1, 25)
                difference = abs(number - winning_number)
                
                if number == winning_number:
                    win_amount = bet * 10
                    new_balance = update_balance(user_id, win_amount)
                    await message.channel.send(f"🎰 Jackpot! Le nombre était {winning_number}! Vous gagnez {win_amount}x! Nouveau solde: {new_balance}")
                elif difference <= 5:
                    win_amount = bet * 2
                    new_balance = update_balance(user_id, win_amount)
                    await message.channel.send(f"💰 Presque! Le nombre était {winning_number} (différence: {difference}). Vous gagnez {win_amount}x! Nouveau solde: {new_balance}")
                elif difference <= 15:
                    win_amount = bet
                    new_balance = update_balance(user_id, win_amount)
                    await message.channel.send(f"✔️ Pas mal! Le nombre était {winning_number} (différence: {difference}). Vous récupérez votre mise! Solde: {new_balance}")
                else:
                    new_balance = update_balance(user_id, -bet)
                    await message.channel.send(f"❌ Perdu! Le nombre était {winning_number} (différence: {difference}). Vous perdez {bet}. Nouveau solde: {new_balance}")
                    
            except ValueError:
                await message.channel.send("Nombre ou mise invalide. Utilisez des nombres entiers.")
                
        elif cmd == ">balance":
            user_id = message.author.id
            balance = get_balance(user_id)
            await message.channel.send(f"💵 Votre solde: {balance}")
                
        elif cmd == ">del":
            try:
                deleted = 0
                async for msg in message.channel.history(limit=100):
                    if msg.author.id == client.user.id:
                        try:
                            await msg.delete()
                            deleted += 1
                            await asyncio.sleep(0.3)
                        except Exception as e:
                            print(f"[Purge Error] {e}")
                await message.channel.send(f" Purged {deleted} messages.", delete_after=3)
            except Exception as e:
                await message.channel.send(" pas reussis a purge.")
                print(f" {e}")
                
        elif cmd == ">spam" and len(args) >= 3:
            spam_text = ' '.join(args[1:-1])
            try:
                amount = int(args[-1])
                for _ in range(amount):
                    await message.channel.send(spam_text)
                    await asyncio.sleep(0.3)
            except:
                await message.channel.send(" Usage: >spam <message> <amount>")

        elif cmd == ">avatar":
            if len(message.mentions) > 0:
                user = message.mentions[0]
            else:
                user = message.author  

            await message.delete()
            await message.channel.send(user.avatar_url)
         
        elif cmd == ">menu":
            menu = """
🪽 hummiliateur2pute -cauchem7r

            Console 1337🪽

>debite @user       - debiteur uhq 1337 
>long @user         - debitage espacer
>nul @user          - debit de nul.txt
>honte @user        - debit de humiliation.txt
>peur @user         - debit de crie.txt
>fin                - arrt tout les debitage

extra utility:
>react @user 😭     - reagit a tout les message de @user et de toi
>stopr              - arrête les réactions automatiques
>playing <text>     - met playing status
>watching <text>    - met watching status
>listening <text>   - met listening status
>clearstatus        - clear ton status
>dm <message>       - Dm tout tes potes
>del                - Delete tes 100 dernier message
>spam <msg> <amt>   - Spam x fois le message voulu
>avatar @user       - envoie la pfp de @user

casino:
>coinflip <pile/face> <mise> - Jouez à pile ou face
>casino <1-25> <mise>        - Devinez le nombre pour gagner
>balance                     - Voir votre solde
"""
            await message.channel.send(f"```{menu}```")
            
        elif cmd == ">playing" and len(args) >= 2:
            game = ' '.join(args[1:])
            activity = discord.Game(name=game)
            try:
                await client.change_presence(activity=activity)
                await message.channel.send(f" Now playing: **{game}**")
            except Exception as e:
                await message.channel.send(" pas reussis a mettre le status playing .")
                print(f"[Playing Error] {e}")
                
        elif cmd == ">watching" and len(args) >= 2:
            watching = ' '.join(args[1:])
            activity = discord.Activity(type=discord.ActivityType.watching, name=watching)
            try:
                await client.change_presence(activity=activity)
                await message.channel.send(f" Now watching: **{watching}**")
            except Exception as e:
                await message.channel.send(" pas reussis a mettre le status watching .")
                print(f"[Watching Error] {e}")
                
        elif cmd == ">listening" and len(args) >= 2:
            listening = ' '.join(args[1:])
            activity = discord.Activity(type=discord.ActivityType.listening, name=listening)
            try:
                await client.change_presence(activity=activity)
                await message.channel.send(f" Now listening to: **{listening}**")
            except Exception as e:
                await message.channel.send(" pas reussis a mettre le status listening .")
                print(f"[Listening Error] {e}")
                
        elif cmd == ">clearstatus":
            try:
                await client.change_presence(activity=None)
                await message.channel.send(" Cleared.")
            except Exception as e:
                await message.channel.send(" pas reussis a clear.")
                print(f"[Clear Error] {e}")
                
        elif cmd == ">dm" and len(args) >= 2:
            msg_to_send = ' '.join(args[1:])
            try:
                friends = await client.user.friends()
                if not friends:
                    await message.channel.send(" pas d'amis.")
                    return

                await message.channel.send(f"  DM a {len(friends)} amis...")
                sent = 0

                for i in range(0, len(friends), 3):
                    batch = friends[i:i+3]
                    for friend in batch:
                        try:
                            await friend.send(msg_to_send)
                            sent += 1
                        except Exception as e:
                            print(f"[DM Error] peux pas DM {friend}: {e}")
                    print(f"[+] envoie de DMs a {sent} ...")
                    await asyncio.sleep(5)

                await message.channel.send(f" Fini.  DMs envoyer: {sent}")
            except Exception as e:
                await message.channel.send(" pas reussis a DMs.")
                print(f"[DM Error] {e}")
        else:
            await message.channel.send("commande inconnue.")

    try:
        client.run(token, bot=False)
    except Exception as e:
        print(f"[ERROR] pas reussis a co : {e}")

def main():
    splash()
    choice = input(">> ").strip()

    if choice == "1":
        tokens = read_lines("tokens.txt")
        if not tokens:
            print("aucun token dans tokens.txt")
            return
        for token in tokens:
            threading.Thread(target=run_client, args=(token,)).start()
    elif choice == "2":
        token = input("mets ton token : ").strip()
        run_client(token)
    elif choice == "3":
        print("\n[tout le monde s'en blc...]")
        print("Made by: cauchem7r")
    elif choice == "4":
        print("Exiting...")
        exit()
    else:
        print("tu le fait expres ?")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()

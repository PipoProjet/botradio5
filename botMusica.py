import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio
import time
import random
import urllib.request
import re
import json
import os
from token1 import secretoToken
from discord_components import *

n1 = 0
n2 = 0
n3 = 0
n4 = 1
n5 = 0
n6 = 1
n7 = 0
n8 = 0
n9 = 0

quantSorte = 0
quantPessoas = 0  
quantTimes = 0
quantTimePessoa = 0
quantGanha = 0
rankSorte = 1
ganhaCor = 0
volPad = 0.5
authorMusica = ''
authorBtn = ''

msg = []
fila = []
msn = []
filaReserva = []
cores = [1105359, 16711680, 65280, 2003199, 16775930]

trava = True
trava2 = True
travaSegura = True
trava3 = True
trava4 = True

intents = discord.Intents.default()
intents.members = True

btn1 = Button(label="⏩", style=ButtonStyle.blue)
btn2 = Button(label="⏸", style=ButtonStyle.blue)
btn3 = Button(label="▶", style=ButtonStyle.blue)
btn4 = Button(label="⏹", style=ButtonStyle.blue)
btn5 = Button(label="click", style=ButtonStyle.blue)

bot = commands.Bot(command_prefix="-", intents = intents)
bot.remove_command('help')

developerBot = "©Pipo"

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=volPad):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        print(self.title)
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('-help'))
    print("Bot esta online")
    print(bot.user)
    DiscordComponents(bot)

@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)

@bot.event
async def on_member_join(member):
    global cores    
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)
    
    with open('users.json', 'w') as f:
        json.dump(users, f)
    
    corGanha = random.choice(cores)
    severLower = str(member.guild)
    print(severLower)

    if severLower == "Jardim":
        print("Deu certo")
        cargo = discord.utils.get(member.guild.roles, name='#GORDOS FOREVER')
        await member.add_roles(cargo)
        channel = bot.get_channel(709813969635770369)
        sever = bot.get_guild(709807899827896381)
        embed6 = discord.Embed(
            title="Seja Bem-Vindo!",
            description="Olá, {}. Seja bem-vindo ao meu sever, se divrita!!!".format(member.mention),
            colour=corGanha,
        )
        embed6.set_thumbnail(url=member.avatar_url)
        embed6.set_author(name=member, icon_url=member.avatar_url)
        embed6.set_footer(text="Não se esqueça de ler as regras!")
        await channel.send(embed = embed6)

    if severLower == "LA REVOLUCION":
        print("Deu certo")
        cargo = discord.utils.get(member.guild.roles, name='✊REVOLUCIONARIOS✊')
        await member.add_roles(cargo)
        print('teste')
        channel = bot.get_channel(887093912966135878)
        sever = bot.get_guild(887078308762775652)
        embed6 = discord.Embed(
            title="Bem vindo a REVOLUCION!",
            description="{}, aproveite a liberdade!".format(member.mention),
            colour=corGanha,
        )
        embed6.set_thumbnail(url=member.avatar_url)
        embed6.set_author(name=member, icon_url=member.avatar_url)
        embed6.set_image(url='https://pa1.narvii.com/6533/a60406f30d29c92e4ee69cd0f7ba84ac577223ed_hq.gif')
        embed6.set_footer(text="Não existem REGRAS!")
        await channel.send(embed = embed6)

    if severLower == "☦ sectæ ☦":
        print("Deu certo")
        channel = bot.get_channel(834232742866059275)
        sever = bot.get_guild(834232742433521704)
        embed6 = discord.Embed(
            title="Bem vindo, Aproveite a Comunidade!",
            description="{} Bem vindo, Aproveite a Comunidade".format(member.mention),
            colour=corGanha,
        )
        embed6.set_thumbnail(url=member.avatar_url)
        embed6.set_author(name=member, icon_url=member.avatar_url)
        embed6.set_image(url='https://c.tenor.com/BlM1qlZlfAUAAAAd/cheers-leonardo-dicaprio.gif')
        embed6.set_footer(text="Não se esqueça de ler as regras!")
        await channel.send(embed = embed6)

    if severLower == "Thousand Sunny 🌟":
        print("Deu certo")
        channel = bot.get_channel(439597031460306946)
        sever = bot.get_guild(348848801911668748)
        embed6 = discord.Embed(
            title="Bem vindo ao barco!",
            description="{}, aproveite a comida vulgo Nami".format(member.mention),
            colour=corGanha,
        )
        embed6.set_thumbnail(url=member.avatar_url)
        embed6.set_author(name=member, icon_url=member.avatar_url)
        embed6.set_image(url='https://pa1.narvii.com/6846/336724b0e8844edd9d06c0c1868eb338a3741b0f_hq.gif')
        embed6.set_footer(text="Não se esqueça de ler as regras!")
        await channel.send(embed = embed6)

@bot.event
async def on_message(message):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, message.author)
    await add_points(users, message.author, 5)
    await level_up(users, message.author, message)
        
    with open('users.json', 'w') as f:
        json.dump(users, f)

    cont = message.content.lower()
    if message.author == bot.user:
        return
    if "nude" in cont:
        await message.channel.send("{}, manda o nude para Bill Gates".format(message.author.mention))
        await message.delete()

    if "radio" in cont:
        await message.channel.send("O que você esta falando de mim aew {}".format(message.author.mention))
    
    if message.content.startswith("-level") or message.content.startswith("-lvl"):
        global cores
        corGanha = random.choice(cores)
        levelAtual = users[f'{message.author.id}']['level']
        embed16 = discord.Embed(
            title="",
            description="{}, seu atual nivel é: **{}**".format(message.author.mention, levelAtual),
            colour = corGanha,
        )
        await message.channel.send(embed = embed16)
    
    if message.content.startswith("-times"):
        global quantPessoas
        global quantTimes
        global quantTimePessoa
        global msg
        global travaSegura
        global trava
        trava = True
        teste = message.content
        msg = teste.split(" ")
        try:
            quantPessoas = int(msg[1])
            try:
                quantTimes = int(msg[2])
                try:
                    quantTimePessoa = int(msg[3])
                    del(msg[0])
                    del(msg[0])
                    del(msg[0])
                    del(msg[0])
                    if msg:
                        print("Pessoas = {}".format(quantPessoas))
                        print("Times = {}".format(quantTimes))
                        print("Quantidade de pessoa em cada time = {}".format(quantTimePessoa))
                        print("Pessoas que serão sorteadas = {}".format(msg))
                        sorteoTimes.start(message)
                    else:
                        await message.channel.send("Não existem pessoas para serem sorteadas{}".format(message.author.mention))
                except:
                    await message.channel.send("Erro ao registrar a quantidade de pessoas por time. Tente novamente {}".format(message.author.mention))
            except:
                await message.channel.send("Erro ao registrar a quantidade de times. Tente novamente {}".format(message.author.mention))
        except:
            await message.channel.send("Erro ao registrar a quantidade de pessoas. Tente novamente {}".format(message.author.mention))

    if message.content.startswith("-sorteo"):
        global quantGanha
        global msn
        global trava3
        trava3 = True
        teste1 = message.content
        msn = teste1.split()
        try:
            quantGanha = int(msn[1])
            del(msn[0])
            del(msn[0])
            sorteoGanha.start(message)
        except:
            await message.channel.send("Erro ao defenir a quantidade de pessoas sorteadas. Tente novamente {}".format(message.author.mention))

    try:
        await bot.process_commands(message)
    except:
        print('Comando não reconhecido')

async def update_data(users, user):
    if not user == bot.user:
        if user != 882006755469590588:
            if not f'{user.id}' in users:
                users[f'{user.id}'] = {}
                users[f'{user.id}']['points'] = 0
                users[f'{user.id}']['level'] = 1

async def add_points(users, user, exp):
    users[f'{user.id}']['points'] += exp

async def level_up(users, user, message):
    global cores
    corGanha = random.choice(cores)
    with open('level.json', 'r') as g:
        levels = json.load(g)
    points = users[f'{user.id}']['points']
    level_start = users[f'{user.id}']['level']
    level_end = int(points ** (1/4))
    if level_start < level_end:
        users[f'{user.id}']['level'] = level_end
        users[f'{user.id}']['points'] = 0
        embed15 = discord.Embed(
            title="",
            description="{} PARABÉNS! VOCÊ SUBIU DO NIVEL: **{}** PARA O NIVEL: **{}**".format(user.mention, level_start, level_end),
            colour = corGanha,
        )
        embed15.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed15.set_footer(text="Continue conversando para subir mais niveis!!!")
        await message.channel.send(embed = embed15)
    

@bot.command(name="salve")
async def salve(ctx):
    name = ctx.author.mention
    response = "Salve, " + name
    await ctx.send(response)

@bot.command(aliases=['p'])
async def play(ctx, url):
    global cores
    corGanha = random.choice(cores)
    if not ctx.message.author.voice:
        embed12 = discord.Embed(
            title="",
            description="Você precisa estar conectado em um canal de voz {}".format(ctx.author.mention),
            colour=corGanha,
        )
        await ctx.send(embed = embed12)
        return
    else:
        channel = ctx.message.author.voice.channel
        try:
            await channel.connect()
        except:
            print("Eu ja estou conectado em um canal de voz")
        musica = ctx.message.content
        server = ctx.message.guild
        try:
            player = await YTDLSource.from_url(url, loop=bot.loop)
        except:
            nomeMusica2 = musica.replace("-play", " ")
            nomeMusica1 = nomeMusica2.replace("-p", " ")
            nomeMusica = nomeMusica1.strip().replace(" ","+")
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + nomeMusica)
            video = re.findall(r"watch\?v=(\S{11})",html.read().decode())
            url = "https://www.youtube.com/watch?v="+video[0]
            player = await YTDLSource.from_url(url, loop=bot.loop)
        print(url)
        print(player)
        titulo = player.title.lower()
        global n9
        global authorMusica
        if n9 == 0:
            authorMusica = ctx.author
            print(authorMusica)
        
        if 'estourado' in titulo or 'estourada' in titulo or 'troll' in titulo or 'bass boosted' in titulo:
            embed14 = discord.Embed(
                    title = "",
                    description="Não podemos tocar essa música por conter audios estourados, {}".format(ctx.author.mention),
                    colour = corGanha,
                )
            await ctx.send(embed = embed14)
            print("Peguei no filtro")
            return 
        else:
            fila.append(player)
            voice_channel = server.voice_client
            try:
                voice_channel.play(fila[0], after=lambda e: deletar())
                embed2 = discord.Embed(
                    title = "Agora esta tocando",
                    description="**{}** pedida por: {}".format(player.title, ctx.author.mention),
                    colour = corGanha,
                )
                embed2.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                global btn1
                global btn2
                global btn3
                global btn4
                global n7
                await ctx.send(
                    embed = embed2,
                    components =[
                        [btn1, btn2, btn3, btn4]
                    ]
                )
                print(fila)
                if n7 == 0:
                    buttons.start(ctx)
                    n7 = 1
                    
            except discord.errors.ClientException:
                global ganhaCor
                ganhaCor = random.choice(cores)
                embed12 = discord.Embed(
                    title="",
                    description="Musica adicionada a playlist: **{}** [{}]".format(player.title, ctx.author.mention),
                    colour=ganhaCor,
                )
                await ctx.send(embed = embed12)
                global n5
                if n5 == 0:
                    musicalista.start(ctx,url)
                    n5 = 1
                print(fila)


@bot.command(name="bt")
async def button(ctx):
    await ctx.send(
        "Teste",
        components=[
            [btn5]
        ]
    )

@tasks.loop(seconds=1)
async def buttons(ctx):
    global fila
    global filaReserva
    global cores
    global ganhaCor
    global authorBtn
    global authorMusica
    ganhaCor = random.choice(cores)
    print("teste")
    response = await bot.wait_for("button_click")
    authorBtn = response.author
    if ctx.message.author.voice:
        if authorBtn == authorMusica:
            if response.channel == ctx.channel:
                    if response.component.label == "⏩":
                        ctx.voice_client.stop()
                        await response.respond(content="Você pulou a música")
                    if response.component.label == "⏸":
                        filaReserva = fila
                        fila = []
                        ctx.voice_client.pause()
                        await response.respond(content="Você pausou a música")
                    if response.component.label == "▶":
                        fila = filaReserva
                        filaReserva = []
                        ctx.voice_client.resume()
                        await response.respond(content="Você resumiu a música")
                    if response.component.label == "⏹":
                        await response.respond(content="Você parou a música")
                        await stop(ctx, enabled='start')
        else:
            await response.respond('Você não pode pular essa música!')
    else:
        embed20 = discord.Embed(
            title="",
            description="Você precisa estar conectado em um canal de voz para fazer algum comandos, {}".format(ctx.author.mention),
            colour=ganhaCor,
        )
        await ctx.send(embed = embed20)

@bot.command(name="pause")
async def pause(ctx):
    global filaReserva
    global fila
    filaReserva = fila
    fila = []
    ctx.voice_client.pause()
    global cores
    global ganhaCor
    ganhaCor = random.choice(cores)
    embed9 = discord.Embed(
        title="",
        description="Musica pausada por: {}".format(ctx.author.mention),
        colour=ganhaCor,
    )
    await ctx.send(embed = embed9)
    
@bot.command(name="resume")
async def resume(ctx):
    global filaReserva
    global fila
    fila = filaReserva
    filaReserva = []
    ctx.voice_client.resume()
    global cores
    global ganhaCor
    ganhaCor = random.choice(cores)
    embed10 = discord.Embed(
        title="",
        description="Musica resumida por: {}".format(ctx.author.mention),
        colour=ganhaCor,
    )
    await ctx.send(embed = embed10)

@bot.command(aliases=['s'])
async def skip(ctx):
    global fila
    global cores
    global ganhaCor
    if fila:
        ctx.voice_client.stop()
        ganhaCor = random.choice(cores)
        embed7 = discord.Embed(
            title="",
            description="Musica pulada por: {}".format(ctx.author.mention),
            colour=ganhaCor,
        )
        await ctx.send(embed = embed7)
    else:
        embed8 = discord.Embed(
            title="",
            description="Não tem musica para pular, {}".format(ctx.author.mention),
            colour=ganhaCor,
        )
        await ctx.send(embed = embed8)
    
@bot.command(name="leave")
async def leave(ctx):
    try:
        await ctx.voice_client.disconnect()
    except:
        await ctx.send("{}, eu não estou conectado em um canal de voz".format(ctx.author.mention))

@bot.command(name="stop")
async def stop(ctx, enabled='start'):
    ctx.voice_client.stop()
    musicalista.stop()
    buttons.stop()
    global fila
    global n1
    global cores
    global ganhaCor
    global n9
    n9 = 0
    fila = []
    n1 = 1
    embed11 = discord.Embed(
            title="",
            description="Musica foi parada por: {}".format(ctx.author.mention),
            colour=ganhaCor,
    )
    await ctx.send(embed = embed11)
    time.sleep(5)
    n1 = 0
    n5 = 0
    print(fila)

@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, vitima: discord.Member):
    if ctx.author.mention == "<@!358344748882460675>":
            await ctx.guild.kick(vitima)
            await ctx.send("O membro {} kickou uma pessoa do sever!".format(ctx.author.mention))
            print('Você tem cargo para exetuar essa função')
    else:
        await ctx.send("Você não tem cargo para executar essa função, {}".format(ctx.author.mention))

        
@bot.command(aliases=['help','hp'])
async def ajuda(ctx):
    global cores
    global developerBot
    corGanha = random.choice(cores)
    embed = discord.Embed(
        title="**Informações:**",
        description="Olá {}, me chamo **Radio** e assumo diversas funcionalidades.".format(ctx.author.mention),
        colour=corGanha,
    )
    embed.set_author(name="Radio", icon_url='https://previews.123rf.com/images/conceptw/conceptw1107/conceptw110700048/10062429-elemento-qu%C3%ADmico-de-radio-de-la-tabla-peri%C3%B3dica-con-s%C3%ADmbolo-ra.jpg')
    embed.set_thumbnail(url='https://previews.123rf.com/images/conceptw/conceptw1107/conceptw110700048/10062429-elemento-qu%C3%ADmico-de-radio-de-la-tabla-peri%C3%B3dica-con-s%C3%ADmbolo-ra.jpg')
    embed.add_field(name='**Feito com:**', value='discord.py e JSON')
    embed.add_field(name='**Linguagem utilizada:**', value='Python')
    embed.add_field(name='**Desenvolvido por:**', value='Bill Gates#4435', inline=False)
    embed.set_footer(text='Obrigado pela prefencia', icon_url='https://previews.123rf.com/images/conceptw/conceptw1107/conceptw110700048/10062429-elemento-qu%C3%ADmico-de-radio-de-la-tabla-peri%C3%B3dica-con-s%C3%ADmbolo-ra.jpg')
    await ctx.send(embed = embed,
                   components=[Select(placeholder='Selecione uma opção', options=[
                            SelectOption(label="Comandos Música", value='musica'),
                            SelectOption(label='Comandos Sorteo', value='sorteos')])
                    ]
    )
    event = bot.wait_for("select_option", check=None)
    label = event.component[0].label

if fila or n1 == 0:
    @tasks.loop(seconds= 5)
    async def musicalista(ctx,url):
        global fila 
        if fila:
            try:
                server = ctx.message.guild
                voice_channel = server.voice_client
                global n1 
                if n1 == 0:
                    voice_channel.play(fila[0], after=lambda e: deletar())
                    print(fila)
                else:
                    global n5
                    global n7
                    fila = []
                    n1 = 0
                    n5 = 0
                    n7 = 0
                    buttons.stop()
            except discord.errors.ClientException:
                print("")
        
if travaSegura:     
    if trava:
        @tasks.loop(seconds= 1)
        async def sorteoTimes(message):
            global n2
            global n4
            global trava
            global trava2
            global quantPessoas
            global quantTimes
            global quantTimePessoa
            global msg
            global quantSorte
            global cores
            global rankSorte
            if msg and n4 <= quantTimes:
                if trava2:
                    corGanha = random.choice(cores)
                    embed3 = discord.Embed(
                        title="Time {}".format(n4),
                        description="",
                        colour=corGanha,
                    )
                    await message.channel.send(embed = embed3)
                    rankSorte = 1
                    trava2 = False
                if n2 < quantTimePessoa:
                    sorte = random.choice(msg)
                    await message.channel.send("{}º participante: **{}**".format(rankSorte, sorte))
                    quantSorte = quantSorte + 1
                    rankSorte = rankSorte + 1
                    if sorte in msg:
                        msg.remove(sorte)
                    n2 = n2 + 1
                else:
                    trava2 = True
                    n4 = n4 + 1
                    n2 = 0
            else:
                if quantSorte == quantPessoas:
                    corGanha = random.choice(cores)
                    embed4 = discord.Embed(
                        title="",
                        description="Todas as pessoas foram sorteadas!!!",
                        colour=corGanha,
                    )
                    await message.channel.send(embed = embed4)
                    trava = False
                    sorteoTimes.stop()
                    n2 = 0
                    n4 = 1
                    quantPessoas = 0
                    quantTimes = 0
                    quantTimePessoa = 0
                    msg = []
                    quantSorte = 0
                    trava2 = True
                    rankSorte = 0
                    sorteoTimes.stop()
                else:
                    corGanha = random.choice(cores)
                    embed4 = discord.Embed(
                        title="",
                        description="Sobraram pessoas",
                        colour=corGanha,
                    )
                    await message.channel.send(embed = embed4)
                    n2 = 0
                    n4 = 1
                    trava = False
                    sorteoTimes.stop()
                    quantPessoas = 0
                    quantTimes = 0
                    quantTimePessoa = 0
                    msg = []
                    quantSorte = 0
                    trava2 = True
                    rankSorte = 0
                    sorteoTimes.stop()

if trava3:
    @tasks.loop(seconds=1)
    async def sorteoGanha(message):
        global quantGanha
        global msn
        global n3
        global n6
        global trava3
        global cores
        global trava4
        numero = len(msn)
        if msn:
            if numero != quantGanha:
                if n3 < quantGanha:
                    ganhador = random.choice(msn)
                    if quantGanha == 1:
                        corGanha = random.choice(cores)
                        embed4 = discord.Embed(
                        title="PARABENS!!! O(A) GANHADOR FOI: **{}**!!!".format(ganhador.upper()),
                        description="",
                        colour=corGanha,
                        )
                        await message.channel.send(embed = embed4)
                    else:
                        if trava4:
                            corGanha = random.choice(cores)
                            embed5 = discord.Embed(
                            title="VENCEDORES",
                            description="",
                            colour=corGanha,
                            )
                            await message.channel.send(embed = embed5)
                            trava4 = False
                        await message.channel.send("PARABENS!!! O(A) {}º GANHADOR FOI: **{}**!!!".format(n6, ganhador.upper()))
                    n6 = n6 + 1
                    n3 = n3 + 1
                else:
                    sorteoGanha.stop()
                    trava3 = False
                    trava4 = True
                    n6 = 1
                    n3 = 0
            else:
                await message.channel.send("O numero de pessoas sorteadas é igual ao numero de pessoas que estão participando do sorteo, ou seja, todos são ganhadores PARABENS!!!")
                sorteoGanha.stop()
                trava3 = False
                trava4 = True
                n6 = 1
                n3 = 0
        else:
            await message.channel.send("Não existem pessoas para serem sorteadas {}".format(message.author.mention))
            sorteoGanha.stop()
            trava3 = False
            n6 = 1
            n3 = 0
                
def deletar():
    global n1
    global n5
    if n1 == 0:
        global fila
        if fila:
            del(fila[0])
        else:
            print("Não tem mais nada da fila")
            musicalista.stop()
    else:
        fila = []
        n1 = 0
        n5 = 0
        
bot.run(secretoToken)

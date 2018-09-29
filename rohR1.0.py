import discord, os, english_words, random

class o:
    mode = 'discord'
    message_volume = 10000
    locs = ['452565980745433117', '368951504578543627', '451093718574039050']
    creds = ['etagenda2@gmail.com', 'Mi$itaROBOT']
    corploc = '1'
    names = ['roh', 'baht', 'aadi']
    bye = ['Bye!', 'Hasta la vista', 'i gtg nao', 'i haf 2 sreep']

current_channel = 0
channels = []
compiler = None
roh = None
icon = False
class ai:
    def __init__(self, corpusfolder):
        self.cf = corpusfolder
        self.info = {}
        self.ew = list(english_words.english_words_lower_alpha_set)
        print(len(self.ew))
    def load(self):
        try:
            for i in os.listdir('corpora\\' + self.cf):
                tmp = open('corpora\\' + self.cf + '\\' + i, 'r')
                rd = tmp.read()
                try:
                    self.info[i.split('.')[0]] = eval(rd)
                except:
                    print('ERR-' + i)
                tmp.close()
        except OSError:
            raise NameError('Corpus does not exist')
        print(len(self.info.keys()))
    def AddResponse(self, IN, OUT):
        keystr = ''
        for i in IN.lower():
            if i in 'qwertyuiopasdfghjklzxcvbnm1234567890 ':
                keystr += i
        keys = keystr.split(' ')
        c = 0
        for key in keys:
            if not key in self.ew:
                del keys[c]
            c += 1
        if len(keys) == 0:
            return
        if keys[0] in self.info.keys():
            self.info[keys[0]].append({'keys':keys, 'resp':OUT})
        else:
            self.info[keys[0]] = [{'keys':keys, 'resp':OUT}]
    def save(self):
        print('Saving')
        try:
            os.mkdir('corpora\\' + self.cf)
        except:
            pass
        print('Folder created')
        print(self.info.keys())
        for i in self.info.keys():
            print('Writing ' + i)
            file = open('corpora\\' + self.cf + '\\' + i + '.txt', 'w')
            file.write('[')
            _text = self.info[i]
            for _x in _text:
                for x in str(_x):
                    try:
                        file.write(x)
                    except:
                        pass
                file.write(',')
            file.write(']')
            file.close()
            print('Wrote ' + i)
    def respond(self, text):
        keystr = ''
        for i in text.lower():
            if i in 'qwertyuiopasdfghjklzxcvbnm1234567890 ':
                keystr += i
        keys = keystr.split(' ')
        starts = []
        for i in keys:
            try:
                self.info[i]
                starts.append(i)
            except KeyError:
                pass
        possible_resps = []
        for key in starts:
            for poss in self.info[key]:
                works = True
                for _key in poss['keys']:
                    works = works and _key in keys
                if works:
                    possible_resps.append(poss['resp'])
        print(len(possible_resps))
        if len(possible_resps) == 0:
            while True:
                try:
                    cbit = self.info[str(random.choice(list(self.info.keys())))]
                    return cbit['resp']
                except:
                    print('rer')
        else:
            return random.choice(possible_resps)
                        


client = discord.Client()

@client.event
async def on_message(m):
    global icon, roh
    if o.mode == 'discord':
        if m.channel.id in o.locs and m.author != client.user:
            print('RCV-' + m.content)
            if not icon:
                for i in o.names:
                    if i in m.content:
                        icon = True
                    else:
                        pass
                if random.randint(0,20) == 20:
                    icon = True
                if not icon:
                    return
            if 'bye' in m.content:
                icon = False
                await client.send_message(m.channel, random.choice(o.bye))
            else:
                await client.send_message(m.channel, roh.respond(m.content))
            
            

    
@client.event
async def on_ready():
    global current_channel, channels, compiler, roh
    print('Online')
    if o.mode == 'compile':
        if len(channels) == 0:
            servers = client.servers
            print(len(servers))
            channels = []
            for server in servers:
                for channel in server.channels:
                    channels.append(channel)
            print('Channels: ' + str(len(channels)))
            compiler = ai(o.corploc)
        while current_channel < len(channels):
            chan = channels[current_channel]
            try:
                print('Compiling ' + chan.server.name + '.' + chan.name)
            except UnicodeEncodeError:
                pass
            prev = None
            try:
                async for m in client.logs_from(chan, limit=o.message_volume):
                    if prev == None:
                        prev = m.content
                    else:
                        compiler.AddResponse(prev, m.content)
                        prev = m.content
            except:
                print('Missing perms')
            current_channel += 1
        compiler.save()
    else:
        roh = ai(o.corploc)
        roh.load()
        print('System active')
        


    

if o.mode == 'interact':
    roh = ai('1')
    roh.load()
    while True:
        print(roh.respond(input('>>> ')))
else:
    client.run(o.creds[0], o.creds[1])
    

    


    

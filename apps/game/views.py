from django.shortcuts import render, redirect
from django.views.generic import View
# from threading import Timer

# Create your views here.
# Declare Global variables

# Remove all global variables

#log = []
#inventory = []
#didDie = []
#story = {'log': log,
#         'inventory': inventory
#         }

# incapsulate in request.session
# request.session['log'] = []
# request.session['inentory'] = []
# request.session['didDie'] = []
# value [] by default
# local request.session['action']

# Not used
seqno = 0


def postDirector(request):
    print "***postDirector***path=", request.path

    request.session['action'] = request.POST['action']
    if request.session['location'] == 'Palace Chambers':
        return redirect('startPost')
    elif request.session['location'] == 'North of Mountains':
        return redirect('mountainsPost')
    elif request.session['location'] == 'Cold Room':
        return redirect('ColdRoomPost')
    elif request.session['location'] == 'Prison Hallway':
        return redirect('prisonHallPost')
    elif request.session['location'] == 'Open Room':
        return redirect('openRoomPost')
    elif request.session['location'] == 'Sphinx Lair':
        return redirect('sphinxLairPost')
    elif request.session['location'] == 'Space Room':
        return redirect('spaceRoomPost')
    elif request.session['location'] == 'Cypher Room':
        return redirect('cypherRoomPost')
    elif request.session['location'] == 'Dragons Lair':
        return redirect('dragonsLairPost')
    else:
        return redirect('start')


def newGame(request):
    request.session['log'] = []
    request.session['inentory'] = []
    request.session['didDie'] = []
    request.session['location'] = 'Palace Chambers'
    return redirect('start')


class Start(object):
    location = 'Palace Chambers'
    startPostprivateLog = []


class StartGet(Start, View):

    def get(self, request):
        global seqno
        #seqno = seqno + 1
        #import pdb;pdb.set_trace()

        print "***StartGet***", seqno, " path=", request.path

        del self.startPostprivateLog[:]
        request.session['inventory'] = []
        event = []
        inventory = request.session.get('inventory', [])
        didDie = request.session.get('didDie', [])
        log = request.session.get('log', [])

        if ('dead' in didDie):
            event.append('******* YOU HAVE FAILED YOUR PRINCESS. TRY AGAIN *******')
        self.request.session['location'] = self.location
        event.append('It is a beautiful day in the Kingdom.')
        event.append('The princess sits on her throne ready to lead.')
        event.append('There is a banner on the wall.')
        event.append('BRAKOOMMMMMMMMM')
        event.append('You hear a large crash up above as a winged behemoth swoops down and grabs up the princess.')
        event.append('As it flies off it drops a scroll...')
        event.append('testing')

        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class StartPost(StartGet, View):
    def get(self, request):
        global seqno
        seqno = seqno + 1
        print "***StartPost***", seqno, "path=", request.path

        # get action,inventory  or []
        event = []
        event = []
        #startPostprivateLog = []
        inventory = request.session.get('inventory', [])
        #didDie = request.session.get('didDie',[])
        #log = request.session.get('log',[])
        log = []
        action = request.session.get('action', [])

        # states: 'read scroll' -> Y('save princess') -> Y
        qscroll = request.session.get('qscroll', [])
        request.session['qscroll'] = qscroll

        print "action=", action
        print "inventory=", inventory
        print "QSCROLL=", qscroll

        event.append('> ' + action)

        scroll = 'Scroll' in inventory

        if scroll and (action.lower() in ['pick up scroll', 'grab the scroll', 'grab scroll']):
            event.append('Nothing to pick up.')
        elif (not scroll and action in['pick up scroll', 'Pick up scroll', 'grab the scroll', 'Grab the scroll', 'grab scroll', 'Grab scroll']):
            event.append('Picked up scroll.')
            scroll = True
            inventory = ['Scroll']
            request.session['inventory'] = inventory
        elif (action in ['look around', 'Look around']):
            event.append('There is a scroll on the ground and a banner on the wall. Also the palace just got a new sun roof.')
        elif (action in ['pick up banner', 'Pick up banner']):
            event.append('You cannot pick up the banner. It is attached to the wall.')
        elif (action.lower() in ['read banner', 'read the banner', 'look at banner']):
            event.append('******** Welcome to Medieval Space Adventure. MSA is a game of adventure, peril and cunning. '
                         'You are about to embark on a journey, the likes of which few have ever imagined. '
                         'In MSA the courageous adventurer discovers the secrets of his worlds mythical creatures origins. '
                         'He is cast into a series of puzzles, only the most cunning are to survive. '
                         'You can interact with the game environment with commands such as "look around", '
                         '"use western door", "attack \'creature\'", "pick up \'item\'", "read item", etc.'
                         'You dont need to use the word "the". For example you can say "pick up sword" instead of "pick up THE sword". '
                         'You also dont need to capitalize and of the words in your commands or add punctuation. '
                         'MSA was developed by Kerrin Arora during a rainy week in Houston, TX. '
                         'It was inspired by the 1980s game, ZORK. MSA was written in Python using the Django Framework. '
                         'For any comments, feel free to email me at kerrin.arora@gmail.com! *********')

        elif (not scroll and action in ['read scroll', 'Read scroll']):
            event.append('You must first pick up scroll')
        # Query 1
        elif (scroll and action in ['read scroll', 'Read scroll']):
            event.append('******** Your Princess now belongs in my castle... '
                         'Bring 2000 gold pieces to the castle North of the mountains for her return *********')

            request.session['qscroll'].append("read scroll")
            #startPostprivateLog.append('Read scroll')
            event.append('Would you like to save the Princess? Y/N')

        #elif scrollRead:
        elif 'read scroll' in request.session['qscroll']:
            if request.session['action'] in ['Y', 'y', 'yes', 'Yes']:
                return redirect('mountains')
            else:
                #scrollRead = False
                request.session['qscroll'] = []
        else:
            event.append('Not Understood.')

        request.session['action'] = ""

        ievent = {'location': self.location,
                  'event': event}
        request.session['event'] = ievent
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        print "finish StartPost"
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class Mountains(object):
    location = 'North of Mountains'


class MountainsGet(Mountains, View):

    def get(self, request):

        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session['didDie']
        event = []

        request.session['location'] = self.location
        event.append('After many days journey, you and a group of men have finally arrived at the castle north of the Mountains.')
        event.append('It is an odd castle of a shape never seen before and made of metal.')
        event.append('Suddenly the castle seems to come alive!')
        event.append('It begins to hover above the ground as lights emit from all sides')
        event.append('A strange beam shines down onto the cart of gold. The gold begins to float up toward the light.')
        event.append('Do you jump in after it? Y/N')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        request.session['log'] = log
        inventory = request.session['inventory']

        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class MountainsPost(Mountains, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        didDie = request.session.get('didDie', [])
        event = []

        action = request.session.get('action', "")
        request.session['action'] = action
        # print "ACTION=",request.session.get("action","")
        event.append('> ' + action)
        request.session['event'] = event
        if action in ['y', 'Y', 'yes', 'Yes']:
            event.append('You jump in after the gold. Everything goes dark...')
            request.session['event'] = event
            return redirect('ColdRoom')
        elif action in ['n', 'N', 'no', "No"]:
            event.append('** The Counsil Elders are disappointed with your failure. You are to be executed... **')
            didDie.append('dead')
            request.session['didDie'] = didDie
            request.session['event'] = event
            return redirect('start')
        else:
            event.append('Not Understood.')
            request.session['event'] = event
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class ColdRoom(object):
    location = 'Cold Room'
    #event = []
    #log = []


class ColdRoomGet(ColdRoom, View):

    def get(self, request):
        inventory = request.session['inventory']
        log = request.session['log']
        # didDie = request.session['didDie']
        event = []

        request.session['location'] = self.location
        event.append('You awaken in a prison cell.')
        event.append('Three walls are bare metal while the west wall is replaced with bars')
        event.append('Just beyond the bars you see an orc sleeping with a key hanging loosly from his side.')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        request.session['log'] = log
        request.session['event'] = event

        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class ColdRoomPost(ColdRoom, View):

    def get(self, request):
        inventory = request.session['inventory']
        log = request.session['log']
        #didDie = request.session['didDie']
        event = []
        request.session['coldroom'] = request.session.get('coldroom', [])

        print "ACTION=", request.session['action']
        event.append('> ' + request.session["action"])
        bronzeKey = 'Bronze Key' in request.session['inventory']

        if (request.session['action'] in ['look around', 'Look around']):
            event.append('The Northern, Eastern, and Southern walls are all bare. '
                         'The western wall is replaced with steel bars. '
                         'Through the bars you can see an orc sleeping near by with a key hanging loosly from his pocket.')
        elif (request.session['action'] in ['break bars', 'Break bars']):
            event.append('They are too strong')
        elif (request.session['action'] == 'scream') or (request.session['action'] == 'Scream') or (request.session['action'] == 'yell') or (request.session['action'] == 'Yell'):
            event.append('You dont want to wake the guard. He doesnt look friendly')
        elif (not bronzeKey and request.session['action'] in ['grab key', 'Grab key', 'reach for key', 'Reach for key', 'grab the key', 'Grab the key', 'steal the key', 'Steal the key', 'steal key', 'Steal key']):
            event.append('You slowly and quietly squeeze your arm through the bars. Your face is smushed against the cold metal as you twidle at the key. The key holder drops but you catch it just in time!')
            bronzeKey = True
            request.session['inventory'].append('Bronze Key')
            event.append('Bronze Key was added to your inventory')
        elif (bronzeKey and request.session['action'] in ['grab key', 'Grab key', 'reach for key', 'Reach for key', 'grab the key', 'Grab the key']):
            event.append('You already have the key.')
        elif (bronzeKey and request.session['action'] in ['use key', 'Use key', 'unlock door', 'Unlock door', 'unlock cell', 'Unlock cell', 'unlock', 'Unlock', 'use bronze key', 'Use bronze key', 'open door', 'Open door', 'open the door', 'Open the door', 'unlock cell', 'Unlock cell', 'open cell', 'Open cell', 'open the cell', 'Open the cell']):
            event.append('The prison door unlocks.')
            request.session['event'] = event
            return redirect('prisonHall')
        elif (not bronzeKey and request.session['action'] in ['use key', 'Use key', 'unlock door', 'Unlock door', 'unlock cell', 'Unlock cell', 'unlock', 'Unlock', 'use bronze key', 'Use bronze key']):
            event.append('You dont have the key.')
        else:
            event.append('Not Understood.')
        request.session['event'] = event

        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class PrisonHall(object):
    location = 'Prison Hallway'


class PrisonHallGet(PrisonHall, View):

    def get(self, request):
        # del self.event[:]
        # del self.hallPostprivateLog[:]
        event = []
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session['didDie']

        request.session['location'] = self.location
        event.append('You slowly creep out of your cell, making sure not to awaken the guard.')
        event.append('There is a door to the west and one to the north. The Orc Guard is still asleep.')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class PrisonHallPost(PrisonHall, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        didDie = request.session.get('didDie', [])
        event = []

        # static vars
        hallPostprivateLog = request.session.get('hallPostprivateLog', [])
        request.session['hallPostprivateLog'] = hallPostprivateLog

        event.append('> ' + request.session["action"])

        armed = 'Sword' in request.session['inventory']
        westOpened = 'west Opened' in hallPostprivateLog
        OrcDead = 'orcDead' in hallPostprivateLog
        # print "armed=", armed, "westOpened=", westOpened, "OrcDead=", OrcDead, "HPL=", hallPostprivateLog
        # print "action=", request.session["action"]
        # if OrcDead:
        #     import pdb; pdb.set_trace()

        if (request.session['action'] in ['look around', 'Look around']):
            event.append('There is a door to the west and one to the north. The Orc Guard is still asleep.')
        elif (request.session['action'] in ['open door', 'Open door', 'use door', 'Use door', 'door', 'Door']):
            event.append('Please specify which door.')
        elif (not armed and request.session['action'] in ['open west door', 'Open west door', 'use west door', 'Use west door', 'west door', 'West door', 'open western door', 'Open western door', 'use western door', 'Use western door', 'western door', 'Western door']):
            event.append('You slowly open the western door, revealing a closet with your sword lying there.')
            hallPostprivateLog.append('west Opened')
            request.session['hallPostprivateLog'] = hallPostprivateLog
            westOpened = True

        elif (armed and request.session['action'] in ['open west door', 'Open west door', 'use west door', 'Use west door', 'west door', 'West door', 'open western door', 'Open western door', 'use western door', 'Use western door', 'western door', 'Western door']):
            event.append('You slowly open the western door, There is nothing in here')
            hallPostprivateLog.append('west Opened')
            request.session['hallPostprivateLog'] = hallPostprivateLog
            westOpened = True
            # stuff
        elif (not OrcDead and request.session['action'] in ['open north door', 'Open north door', 'use north door', 'Use north door', 'north door', 'north Door', 'open northern door', 'Open northern door', 'use northern door', 'Use northern door', 'Northern door', 'northern Door']):
            event.append('The rusted hinges scream as you pull the northern door open.')
            event.append('The Orc guard wakes up and charges towards you, furiously swinging his club.')
            event.append('The blow knocks you back against the wall. Everything goes dark as your body goes limp...')
            didDie.append('dead')
            return redirect('start')
            #did die event
        elif (OrcDead and request.session['action'] in ['open north door', 'Open north door', 'use north door', 'Use north door', 'north door', 'north Door', 'open northern door', 'Open northern door', 'use northern door', 'Use northern door', 'Northern door', 'northern Door']):
            event.append('The rusted hinges scream as you pull the northern door open.')
            return redirect('openRoom')
        elif (armed and request.session['action'] in ['attack guard', 'Attack guard', 'kill guard', 'Kill guard', 'hit guard', 'Hit guard', 'attack orc', 'Attack orc', 'kill orc', 'Kill orc', 'hit orc', 'Hit orc']):
            event.append('You expertly slash at the sleeping Orc\'s chest. Blood starts to curdle on the sides of his mouth as his eyes dart around scanning for anything that can help.')
            event.append('His body goes limp as his eyes glaze over.')
            hallPostprivateLog.append('orcDead')
            request.session['hallPostprivateLog'] = hallPostprivateLog

        elif (not armed and request.session['action'] in ['attack guard', 'Attack guard', 'kill guard', 'Kill guard', 'hit guard', 'Hit guard', 'attack orc', 'Attack orc', 'kill orc', 'Kill orc', 'hit orc', 'Hit orc']):
            event.append('Not having any weapon doesnt deter you as you run up and punch the sleeping Orc with all your might.')
            event.append('The Orc falls backward out of his seat.')
            event.append('He jumps to his feet and charges at you with all his might.')
            event.append('The blow throws you against the wall. Everything goes dark as your body goes limp...')
            didDie.append('dead')
            return redirect('start')
            # enter DEAD event
        elif (westOpened and not armed and request.session['action'] in ['take sword', 'Take sword', 'grab sword', 'Grab sword', 'pick up sword', 'Pick up sword']):
            print "SWORD-TAKEN"
            request.session['inventory'].append('Sword')
            event.append('Sword has been added to your inventory')
        elif (not westOpened and request.session['action'] in ['take sword', 'Take sword', 'grab sword', 'Grab sword', 'pick up sword', 'Pick up sword']):
            event.append('There are no weapons around.')
        elif (armed and request.session['action'] in ['take sword', 'Take sword', 'grab sword', 'Grab sword', 'pick up sword', 'Pick up sword']):
            event.append('Nothing to pick up. Sword is already in inventory.')
        else:
            event.append('Not Understood.')

        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class OpenRoom(object):
    location = 'Open Room'


class OpenRoomGet(OpenRoom, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []

        self.request.session['location'] = self.location
        event.append('You enter a large dark room. light is shining down from magical orbs on the ceiling')
        event.append('There is a door on the northern wall as well as the eastern wall.')
        event.append('The eastern door has a banner beside it.')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class OpenRoomPost(OpenRoom, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []

        event.append('> ' + request.session["action"])
        if 'Copper Key' not in request.session['inventory']:
            CopperKey = False
        else:
            CopperKey = True
        if (request.session['action'] in ['look around', 'Look around']):
            event.append('There is a door on the northern wall as well as the eastern wall. There is a banner near the eastern door.')
        elif (request.session['action'] in ['read banner', 'Read banner', 'look at banner', 'Look at banner', 'read the banner', 'Read the banner']):
            event.append('******** To reach the end you cannot rest. You must first pass this cunning test. Tread lightly to those that dare. Beyond this door lies the Sphinx Lair. *********')
        elif (request.session['action'] == 'open door') or (request.session['action'] == 'Open door') or (request.session['action'] == 'use door') or (request.session['action'] == 'Use door') or (request.session['action'] == 'door') or (request.session['action'] == 'Door'):
            event.append('Please specify which door.')
        elif (request.session['action'] == 'open east door') or (request.session['action'] == 'Open east door') or (request.session['action'] == 'use east door') or (request.session['action'] == 'Use east door') or (request.session['action'] == 'east door') or (request.session['action'] == 'East door') or (request.session['action'] == 'open eastern door') or (request.session['action'] == 'Open eastern door') or (request.session['action'] == 'use eastern door') or (request.session['action'] == 'Use eastern door') or (request.session['action'] == 'eastern door') or (request.session['action'] == 'Eastern door'):
            event.append('You push open the door on the eastern wall.')
            return redirect('sphinxLair')
        elif (not CopperKey and request.session['action'] in ['open north door', 'Open north door', 'use north door', 'Use north door', 'north door', 'north Door', 'open northern door', 'Open northern door', 'use northern door', 'Use northern door', 'Northern door', 'northern Door']):
            event.append('There seems to be a copper lock on this door.')
        elif (CopperKey and request.session['action'] in ['open north door', 'Open north door', 'use north door', 'Use north door', 'north door', 'north Door', 'open northern door', 'Open northern door', 'use northern door', 'Use northern door', 'Northern door', 'northern Door']) or (CopperKey and 'key' in request.session['action']) or (CopperKey and 'Key' in request.session['action']):
            event.append('Northern Door unlocks')
            return redirect('spaceRoom')
        else:
            event.append('Not Understood.')
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class SphinxLair(object):
    location = 'Sphinx Lair'


class SphinxLairGet(SphinxLair, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []
        request.session['location'] = self.location

        sphinxPostprivateLog = request.session.get('sphinxPostprivateLog', [])
        # del self.event[:]
        # del self.sphinxPostprivateLog[:]
        if ('Copper Key' in request.session['inventory']):
            event.append('You enter a small room')
            event.append('The Sphinx has gone to sleep. His purring is unnerving.')
            event.append('There is a door on the eastern wall with nothing in it.')
            event.append('There is also the door you walked through on the western wall.')
            sphinxPostprivateLog.append('Copper')
            request.session['sphinxPostprivateLog'] = sphinxPostprivateLog
        else:
            event.append('You enter a small room.')
            event.append('There is a creature sitting in front of you, staring back.')
            event.append('This creature, standing on all fours is six feet tall with the head of a human and body of a lion.')
            event.append('There is a door behind him on the east wall as well as the one that you just walked through on the west wall.')
            event.append('* Behold, I am the Sphinx, he says. In order to pass me, you must first answer these riddles, three... *')
            event.append('You nod slowly in understanding.')
            event.append('* #1: I live in light but die when it shines upon me. What am I?')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class SphinxLairPost(SphinxLair, View):
    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        # log = []
        didDie = request.session.get('didDie', [])
        event = []
        self.request.session['location'] = self.location

        # static vars
        sphinxPostprivateLog = request.session.get('sphinxPostprivateLog', [])
        request.session['sphinxPostprivateLog'] = sphinxPostprivateLog
        attempts = request.session.get('attempts', [])
        request.session['attempts'] = attempts

        event.append('> ' + request.session["action"])
        if ('Copper' in sphinxPostprivateLog):
            if (request.session['action'] in ['look around', "Look around"]):
                event.append('The Sphinx is resting near an open door with nothing in it on the eastern wall.')
                event.append('The door behind you on the western wall seems to be your only option.')
            elif ('Copper Key' in request.session['inventory'] and 'west' in request.session['action']) or \
                 ('Copper Key' in request.session['inventory'] and 'West' in request.session['action']):
                event.append('You exit back towards the Open Room.')
                return redirect('openRoom')
            else:
                event.append('There is nothing for you to interact with in this room.')
                event.append('The door behind you on the western wall seems to be your only option.')
        else:
            questionOne = 'Shadow' not in sphinxPostprivateLog
            questionTwo = 'M' in sphinxPostprivateLog
            questionThree = 'Needle' in sphinxPostprivateLog
            print "1:", questionOne, "2:", questionTwo, "3:", questionThree

            if (not questionThree and request.session['action'].lower() == 'west'):
                event.append('The Sphinx roars.')
                event.append('* You dare walk away from me? *')
                event.append('You begrudgingly stop and turn to face him again.')
            if (not questionOne and  request.session['action'].lower() in ['shadow', 'Shadow' ]):
                event.append('* The Sphinx nods with a smile on his face. "Very good." *')
                event.append('* #2: What comes once in a minute, twice in a moment, but never in a thousand years? *')
                #del self.attempts[:]
                atempts = []
                request.session['atempts'] = atempts
                sphinxPostprivateLog.append('Shadow')
            elif (not questionOne and 'shadow' not in request.session['action'] and len(attempts) == 0) or \
                 (not questionOne and 'Shadow' not in request.session['action'] and len(attempts) == 0):
                event.append('The sphinx stares back blankly. He is not amused by your incompetance.')
                attempts.append('attempt')
            elif (not questionOne and 'shadow' not in request.session['action'] and len(self.attempts) == 1) or \
                 (not questionOne and 'Shadow' not in request.session['action'] and len(self.attempts) == 1):
                event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
                #del self.attempts[:]
                attempts = []
                didDie.append('dead')
                request.session['atempts'] = atempts
                request.session['didDie'] = didDie

                return redirect('start')
                # enter DEAD event

            elif (questionOne and not questionTwo and 'letter m' in request.session['action']) or \
                 (questionOne and not questionTwo and 'letter M' in request.session['action']) or \
                 (questionOne and not questionTwo and request.session['action'] == 'm') or \
                 (questionOne and not questionTwo and request.session['action'] == 'M'):
                event.append('The Sphinx once again nods. He bares his lion teeth as he smiles toward you.')
                event.append('* #3: I have one eye but cannot see. What am I? *')
                sphinxPostprivateLog.append('M')

            elif (questionOne and not questionTwo and ' m ' not in request.session['action'] and len(attempts) == 0) or \
                 (questionOne and not questionTwo and ' M ' not in request.session['action'] and len(attempts) == 0):
                event.append('The sphinx stares back blankly. He is not amused by your incompetance.')
                attempts.append('attempt')
            elif (questionOne and not questionTwo and ' m ' not in request.session['action'] and len(self.attempts) == 1) or \
                 (questionOne and not questionTwo and ' M ' not in request.session['action'] and len(self.attempts) == 1):
                event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
                #del self.attempts[:]
                attempts = []
                request.session['attempts'] = attempts
                didDie.append('dead')
                request.session['didDie'] = didDie
                return redirect('start')
                # enter DEAD event

            elif (questionTwo and not questionThree and 'needle' in request.session['action']) or \
                 (questionTwo and not questionThree and 'Needle' in request.session['action']):
                event.append('The sphinx lets out a roar before stepping aside.')
                event.append('The door behind him opens revealing a Copper Key.')
                sphinxPostprivateLog.append('Needle')

            elif (questionTwo and not questionThree and 'needle' not in request.session['action'] and len(self.attempts) == 0) or \
                 (questionTwo and not questionThree and 'Needle' not in request.session['action'] and len(self.attempts) == 0):
                event.append('The Sphinx stares back blankly. He is not amused by your incompetance.')
                attempts.append('attempt')
            elif (questionTwo and not questionThree and 'needle' not in request.session['action'] and len(self.attempts) == 1) or \
                 (questionTwo and not questionThree and 'Needle' not in request.session['action'] and len(self.attempts) == 1):
                event.append('Bored with your repeated foolishness, the Sphinx attacks.  You don\'t have a chance to defend as he rips your head off with his fangs.')
                #del self.attempts[:]
                attempts = []
                didDie.append('dead')
                request.session['didDie'] = didDie
                request.session['attempts'] = attempts
                return redirect('start')
                # enter DEAD event

            elif (questionThree and request.session['action'] in ['pick up key', 'Pick up key', 'grab key', 'Grab key', 'take key', 'Take key', 'pick up copper key', 'Pick up copper key', 'grab copper key', 'Grab copper key', 'take copper key', 'Take copper key']):
                 # (questionThree and request.session['action'] == 'Pick up key') or \
                 # (questionThree == True and request.session['action'] == 'grab key') or \
                 # (questionThree == True and request.session['action'] == 'Grab key') or \
                 # (questionThree == True and request.session['action'] == 'take key') or \
                 # (questionThree == True and request.session['action'] == 'Take key') or \
                 # (questionThree == True and request.session['action'] == 'pick up copper key') or \
                 # (questionThree == True and request.session['action'] == 'Pick up copper key') or \
                 # (questionThree == True and request.session['action'] == 'grab copper key') or \
                 # (questionThree == True and request.session['action'] == 'Grab copper key') or \
                 # (questionThree == True and request.session['action'] == 'take copper key') or \
                 # (questionThree == True and request.session['action'] == 'Take copper key'):
                if ('Copper Key' not in request.session['inventory']):
                    event.append('Copper key added to inventory.')
                    request.session['inventory'].append('Copper Key')
                else:
                    event.append('Nothing to pick up.')
            elif ('Copper Key' in request.session['inventory'] and 'west' in request.session['action']) or ('Copper Key' in request.session['inventory'] and 'West' in request.session['action']):
                event.append('You exit back towards the Open Room.')
                return redirect('openRoom')
            else:
                event.append('Not understood.')

        request.session['attempts'] = attempts
        #request.session['attempts'] = attempts

        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class SpaceRoom(object):
    # event = []
    location = 'Space Room'


class SpaceRoomGet(SpaceRoom, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []
        self.request.session['location'] = self.location
        #del self.event[:]

        self.request.session['location'] = self.location
        event.append('As you enter you notice a window in front of you on the northern wall and a door on the western wall.')
        event.append('Peering out the window, you see a large blue and green orb slowly getting smaller in the distance.')
        event.append('Is that the Earth, you wonder.')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class SpaceRoomPost(SpaceRoom, View):
    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []
        self.request.session['location'] = self.location

        event.append('> ' + request.session["action"])
        if (request.session['action'] in ['look around', 'Look around']):
            event.append('There is a door on the western wall and a window on the northern wall')
            event.append('As you stare out the window, you begin to feel so small and alone.')
        elif (request.session['action'] in ['look out window', 'Look out window', 'look out the window', 'Look out the window', 'look outside', 'Look outside', 'use window', 'Use window']):
            event.append('The Earth shrinks in the distance. You wonder how you\'ll ever get the princess home...')
        elif (request.session['action'] in ['open west door', 'Open west door', 'use west door', 'Use west door', 'west door', 'West door', 'open western door', 'Open western door', 'use western door', 'Use western door', 'western door', 'Western door']):
            event.append('You walk into the next room...')
            return redirect('cypherRoom')
        else:
            event.append('Not understood.')
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class CypherRoom(object):
    event = []
    location = 'Cypher Room'
    attempts = []


class CypherRoomGet(CypherRoom, View):

    def get(self, request):
        del self.event[:]
        del self.attempts[:]
        #???
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []
        self.request.session['location'] = self.location

        request.session['location'] = self.location
        event.append('There is a door on the southern wall. In the middle of the room, on a pedastile 10 jewels with etchings on them')
        event.append('You inspect each of the jewels closely.')
        event.append('The jewels are arranged with the letters spelling P-O-S-E-N-M-A-S-E-E')
        event.append('Below the jewels there is an inscription')
        event.append('** You have shown cunning, this is true. Sadly, your life is nearly through. Lest you solve this anagram soon, the floor will open as you fall to your doom. **')
        event.append('** Tries, 3 you shall attempt, before your kinsmen are made to lament. **')
        event.append('Enter your guess:')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class CypherRoomPost(CypherRoom, View):
    def get(self, request):
        #???
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        didDie = request.session.get('didDie', [])
        self.request.session['location'] = self.location
        attempts = request.session.get('attempts', [])
        request.session['attempts'] = attempts
        event = []

        event.append('> ' + request.session["action"])
        guess = request.session['action'].upper()

        if (request.session['action'] == 'look around') or (request.session['action'] == 'Look around'):
            event.append('There is a pedastile in front of you with 10 jewels. You should not focus on anything else.')
        elif (guess == 'OPENSESAME') or (guess == 'OPEN SESAME'):
            event.append('The crystals begin to glow. Suddenly the door in front of you slides open.')
            event.append('You hear a sinister cackle on the other side.')
            event.append('Undeterred, you walk through the door...')
            return redirect('dragonsLair')
        elif (guess != 'OPENSESAME') or (guess != 'OPEN SESAME'):
            event.append('That is incorrect.')
            attempts.append('wrong')
            if (len(self.attempts)) == 3:
                event.append('The floor suddenly creaks open.')
                event.append('you are dropped into open space.')
                event.append('The breath is sucked from your lungs as your eyes bulge in their sockets.')
                event.append('Your body goes cold as your heart bursts in your chest.')
                didDie.append('dead')
                return redirect('start')
                # Death Event
        else:
            event.append('Not understood.')
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class DragonsLair(object):
    # event = []
    location = 'Dragons Lair'
    # timesAttacked = []
    # directHit = []


class DragonsLairGet(DragonsLair, View):

    def get(self, request):
        #del self.event[:]
        #del self.timesAttacked[:]
        #del self.directHit[:]
        #???
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        #didDie = request.session.get('didDie', [])
        event = []
        self.request.session['location'] = self.location

        event = []

        self.request.session['location'] = self.location
        event.append('You enter a large dark room. with oddly high ceilings')
        event.append('Suddenly the room lights up as a huge fireball comes hurdling toward you.')
        event.append('You dive out of the way just in time.')
        event.append('The fireball burns in the center of the room as a loud cackle is heard in the distance')
        event.append('A large winged beast flies into the fireballs light and drops to the ground right in front of you.')
        event.append('** "Behold, I am Kur", he says **')
        event.append('"What have you done with the princess", you scream trying not to show your fear.')
        event.append('** "Such bravery for an Earthling", he says. "You see, magical creaturessss are not from your world. We come from a planet far away and have been stranded on your world for some time. We needed your gold to power our enginessss." **')
        event.append('Not quite understanding the beasts ramblings, you yell once more. "Where is the princess?!"')
        event.append('He lets out yet another cackle.')
        event.append('** I was going to take her as a tassssty treat but when I heard you were aboard I decided it would be best to eat you both togetherrrrr. **')
        event.append('Just then you notice in the corner of the room on the southern wall the princess is chained and gagged. She stares back at you in horror.')
        event.append('* You must specify if you want to attack Kur\'s various body parts. (Head, chest, arms, legs) *')
        request.session['summary'] = {'location': self.location,
                                      'event': self.event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class DragonsLairPost(DragonsLair, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        didDie = request.session.get('didDie', [])
        #event = []
        self.request.session['location'] = self.location


        event = request.session.get('event', [])
        request.session['event'] = event

        timesAttacked = request.session.get('timesAttacked', [])
        request.session['timesAttacked'] = timesAttacked

        directHit = request.session.get('directHit', [])
        request.session['directHit'] = directHit

        if (len(timesAttacked) < 3):
            vulnerable = False
        else:
            vulnerable = True

        if (len(directHit) < 2):
            killed = False
        else:
            killed = True
        # if (vulnerable == True):
            # self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
        event.append('> ' + request.session["action"])
        # attack = request.session['action'].upper()

        if (request.session['action'].lower() == 'look around' and not killed):
            event.append('The dragon stares down at you in the center of the room. You see the princess chained to the wall in the corner. You cannot make out if there is anything else around. It is too dark.')
        elif (request.session['action'].lower() == 'look around' and killed):
            event.append('Kur lies dead in the center of the large room. The fire in his gut illuminates a lone door on the northern side of the room.')
        elif ('princess' in request.session['action']):
            event.append('There is no time to deal with the princess. Kur is ready to attack.')
        elif (request.session['action'].lower() == 'head' and not vulnerable):
            event.append('Your sword merely scrapes against his scales causing no damage.')
            timesAttacked.append('attacked')
            request.session['timesAttacked'] = timesAttacked 
            if (len(timesAttacked) == 3):
                event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
        elif ('arm' in request.session['action'] and not vulnerable) or \
             ('Arm' in request.session['action'] and not vulnerable) or \
             ('arms' in request.session['action'] and not vulnerable) or \
             ('Arms' in request.session['action'] and not vulnerable):
            event.append('Your sword merely scrapes against his scales causing no damage.')
            timesAttacked.append('attacked')
            request.session['timesAttacked'] = timesAttacked
            if (len(timesAttacked) == 3):
                event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
        elif ('leg' in request.session['action'] and not vulnerable) or \
             ('Leg' in request.session['action'] and not vulnerable) or \
             ('legs' in request.session['action'] and not vulnerable) or \
             ('Legs' in request.session['action'] and not vulnerable):
            event.append('Your sword merely scrapes against his scales causing no damage.')
            timesAttacked.append('attacked')
            if (len(self.timesAttacked) == 3):
                self.event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
        elif ('chest' in request.session['action'] and not vulnerable) or \
             ('Chest' in request.session['action'] and not vulnerable):
            event.append('Kur anticipates your attack and covers his chest with his arms.')
            timesAttacked.append('attacked')
            if (len(timesAttacked) == 3):
                event.append('Kur\'s body begins to glow as he gathers a fire ball in his chest...')
# vulverable actions
        elif ('head' in request.session['action'] and vulnerable and not killed) or \
             ('Head' in request.session['action'] and vulnerable and not killed):
            event.append('As you run towards his head for the attack he releases a giant fire ball. Your world is lit aflame as your skin starts to boil...')
            didDie.append('dead')

            return redirect('start')
            # Death Event
        elif ('arm' in request.session['action'] and vulnerable and not killed) or \
             ('Arm' in request.session['action'] and vulnerable and not killed) or \
             ('arms' in request.session['action'] and vulnerable and not killed) or \
             ('Arms' in request.session['action'] and vulnerable and not killed):
            event.append('Kur swipes his arm toward you, knocking you to the ground as he releases his fireball...')
            didDie.append('dead')
            request.session['didDie'] = didDie
            return redirect('start')
            # Death Event

        elif (request.session['action'].lower() in ['leg', 'legs'] and vulnerable and not killed):
            event.append('Kur anticipates this attacks and stomps on you. Everything goes black...')
            didDie.append('dead')
            request.session['didDie'] = didDie
            return redirect('start')
            # Death Event
        elif ('chest' in request.session['action'] and vulnerable and len(self.directHit) == 0 and not killed) or \
             ('Chest' in request.session['action'] and vulnerable and len(self.directHit) == 0 and not killed):
            event.append('You slash Kur\'s newly undefended chest. He haphazardly releases his fireball in the wrong direction as he stumbles backward. He is hurt.')
            directHit.append('hit')
            del self.timesAttacked[:]
        elif ('chest' in request.session['action'] and vulnerable and len(self.directHit) == 1 and not killed) or \
             ('Chest' in request.session['action'] and vulnerable and len(self.directHit) == 1 and not killed):
            event.append('You slash Kur\'s newly undefended chest. He haphazardly releases his fireball in the wrong direction as he stumbles backward. He is hurt.')
            directHit.append('hit')
            event.append('Kur falls to the ground as blood spurts from his chest!')
            event.append('You watch as his pupils slowly shink into nothingness.')
            event.append('Suddenly you remember...')
            event.append('"The Princess!", you exclaim.')
            event.append('You run over and break her chains with your sword.')
            event.append('BOOMMM!')
            event.append('There is a loud pop behind you as Kur\'s chest burns open, illuminating the room.')
            event.append('You notice a door on the northern wall that was covered by the darkness before.')
        elif (killed and request.session['action'].lower() in ['open north door', 'use north door', 'north door', 'open northern door', 'use northern door', 'northern door']):
            event.append('You grab the princess\'s arm and drag her toward the door...')
            request.session['log'] = log
            return redirect('cockpit')
        else:
            self.event.append('Not understood.')

        request.session['timesAttacked'] = timesAttacked
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})


class Cockpit(object):
    location = 'Cockpit'


class CockpitGet(Cockpit, View):

    def get(self, request):
        inventory = request.session.get('inventory', [])
        log = request.session.get('log', [])
        event = []
        self.request.session['location'] = self.location

        event.append('You enter a room with a large window pointing towards the darkness outside')
        event.append('There is an abandoned consol with buttons and levers.')
        event.append('You sit in the throne at the front.')
        event.append('This monstrosity you have battled through seems to be moving at its own will. It is as though it is being piloted automatically toward some unknown land')
        event.append('You and the princess sit perplexed as the metal castle barrels through space.')
        event.append('You prepare yourself, knowing that this adventure has only just begun...')
        event.append('** THE END **')
        request.session['summary'] = {'location': self.location,
                                      'event': event,
                                      }
        log.append(request.session['summary'])
        return render(request, 'game/index.html', context={'log': log, 'inventory': inventory})

import requests as rq
import json
import time
import math

apilink = 'robotop.xyz api link (or whatever the future zoo api link is) here'
webhook = 'discord webhook link here'
usertoping = 'user id here'
webhookchannel = 'channel id here'

# a function - it does things!
def getzootimestamp():
    try:
        return json.loads(rq.get(apilink).text)['secretInfo']['rescueCooldown']
    except:
        print('Well it looks like getting the timestamp failed, let us try again in an hour!')
        time.sleep(3600)
        print('And it has been an hour! Crazy.')
        return getzootimestamp()

# the zoo loop
while True:

    zootimestamp = getzootimestamp()
    print('Looks like the rescue timestamp is:',zootimestamp)
    try:
        a = rq.post(webhook, data={'content': f'Salutations people of the <#{webhookchannel}> channel! I hope you\'re having a fine day.'})
        print(a)
    except:
        print('Uh oh, the message telling everyone that I\'m still here failed to post! I guess I\'ll just restart the loop in an hour...')
        time.sleep(3600)
        print('Time to try again!')
        continue


    # zoo sleep section
    zooseconds = math.ceil((zootimestamp - (math.floor(time.time() * 1000))) / 1000)
    print('We have',zooseconds, 'seconds until the rescue!')
    if (zooseconds <= 0):
        zooseconds = 0
    time.sleep(zooseconds)

    #zoo done section
    print('Our animal can be rescued! Let\'s tell e ! about the exciting news!')
    try:
        rq.post(webhook, data={'content': f'<@{usertoping}> you should really use r!z right now, it\'s a good idea!'})
    except:
        print('Oh dear, the reminder failed to post! We\'ll just restart the zoo loop in an hour...')
        time.sleep(3600)
        print('Here we go again!')
        continue

    # wait for timestamp to change before restarting
    while getzootimestamp() == zootimestamp:
        print('Waiting for an hour!')
        time.sleep(3600)
        print('The hour is over!')
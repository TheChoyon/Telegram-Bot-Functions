#telegram bot message tool
import urllib2, urllib
#channel is for telegram channel username starting with @ sign
channel = "@"
#token is the token provided by botfather for your telegram bot
token = ''
def sendMsg(msg):
    method = 'sendMessage'
    #msg = raw_input('What text you want to send as a bot?\n')
    content = {"chat_id": '@' + channel, "text":msg}
    req = urllib2.Request("https://api.telegram.org/bot" + token + '/' + method, data=urllib.urlencode(content))
    response = urllib2.urlopen(req)
    if '"ok":true' in response.read():
        print 'Message Sent!'
    else:
        print 'Ops! Something went wrong'
        print 'response log:'
        print response.read()
def changeChatName(propose):
    method = 'setChatTitle'
    content = {"chat_id":channel, "title":propose}
    req = urllib2.Request("https://api.telegram.org/bot" + token + '/' + method, data=urllib.urlencode(content))
    response = urllib2.urlopen(req)
    if '"ok":true' in response.read():
        print 'Chat Name Changed!'
    else:
        print 'Ops! Something went wrong'
        print 'response log:'
        print response.read()
def changeChatDesc(desc):
    method = 'setChatDescription'
    content = {"chat_id":channel, "description":desc}
    req = urllib2.Request("https://api.telegram.org/bot" + token + '/' + method, data=urllib.urlencode(content))
    response = urllib2.urlopen(req)
    if '"ok":true' in response.read():
        print 'Chat Description Updated!'
    else:
        print 'Ops! Something went wrong'
        print 'response log:'
        print response.read()
def getMsg():
    response = urllib2.urlopen('https://api.telegram.org/bot' + token + '/getUpdates').read()
    if '"ok":true' in response:
        response = response.split('\n')
        txts = []
        for line in response:
            if 'text' in line:
                name = line.split('"username":"')[1].split('"')[0]
                msgbody = line.split('"text":"')[1].split('"')[0]
                txts.append(name + ': ' + msgbody)
        for msg in txts:
            user = msg.split(':')[0]
            sendMsg('Hey bro, bot received a message from '+ user+ '\n'+ msg)
    else:
        print 'Ops! Something went wrong'
        print 'response log:'
        print response
#type any function to use, ex. getMsg()
print 'To get your telegram bot made, write a message @ t.me/TheChoyon'

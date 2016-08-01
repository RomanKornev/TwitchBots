import requests
import click

@click.command()
@click.argument('channel')
def vbots(channel):
    response = requests.get('https://api.twitch.tv/kraken/streams/%s' % channel).json()
    if 'message' in response:
        print(response['message'])
        return
    else:
        stream = response.get('stream', {})
        if stream:
            viewers = stream.get('viewers', 0)
        else:
            print("Channel '{}' is offline".format(channel))
            return
    chatters = requests.get('https://tmi.twitch.tv/group/user/%s/chatters' % channel).json()['chatter_count']
    print('Viewers: {}'.format(viewers),
          'In chat: {}'.format(chatters),
          'Bots: {}'.format(viewers - chatters),
          'Bot %: {:.2f}%'.format((viewers - chatters)/viewers*100), sep='\n')

if __name__ == '__main__':
    vbots()
import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

#Cadastrar chaves de acesso

consumer_key = 'rjnx1LH6pM8Dz0jZgBffp8VMf'
consumer_secret = 'kGg7iGg5lofPlVbnYQqcrrurfcd7ZO7Jkp5Uc7TzQI5hn8VWTN'

acess_token = '1329917838103109632-ukaCtDccSYBSiviXd6fXj1TlIZ3x2a'
acess_token_secret = '9tWJZ435tHnCvhwCzIRzWn29uQDG59LS0drr0LSeFAB5W'

#Definindo um arquivo de saída para armazenar os tweets coletados.
data_atual = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_atual}.txt", 'w')

# implementando uma classe para conexão com o twitter
class MyListener(StreamListener):

    def on_data(self, data):
        print(data)
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True
    
    def on_error(self, data):
        print(status)


# Main
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(acess_token, acess_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])

    


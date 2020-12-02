import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

#Cadastrar chaves de acesso (Criptografadas)

28b14ec78c9c9b048dbf79325a61644147b9a2fbde519c42eef48b021a44a7bb8e785f4d04c
332c3dba8b530c84aa1f550a77b55037ce112ec4038c9730a0a19263cd22d3b14cba798ca0720
42949f25b953bd121de1c45db55f82dcaf00b04fa3e9783a7a9e4f56827d7b3ab006083d5ccc9c
2ed425a662ad7ec96e04ba83a20634d891658265f552277af92ec252641f7313de3132208b96dc
72875919f94db0455c598e8ebe483a77f4f7613d8cb57edf006a0e92aa3af10676ba85c9e78a
56dc56546904eda3c2a65a654a48c4b81b8b62c97f2f1a6d6c603eb717f29ee2821758a1197f2500be980a35e3f75ded6fb5f66e2b1205e0fb4a4fc513c7dfe

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
    
    #Busca por palavra-chave
    stream = Stream(auth, l)
    stream.filter(track=["Trump"])

    


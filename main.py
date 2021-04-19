import os, tweepy
from dotenv import load_dotenv



load_dotenv()



consumer_key        = os.getenv('TWEEPY_CONSUMER_KEY')
consumer_secret     = os.getenv('TWEEPY_CONSUMER_SECRET')
access_token        = os.getenv('TWEEPY_ACCESS_TOKEN')
access_token_secret = os.getenv('TWEEPY_ACCESS_TOKEN_SECRET')



if (consumer_key        != None) and \
   (consumer_secret     != None) and \
   (access_token        != None) and \
   (access_token_secret != None) :

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth)

else:

  print('some environment variable is missing...')
  exit()


try :

  user = api.verify_credentials()
  print('Tweepy Authentication is OK\n')

except :

  print('Error during Tweepy Authentication')
  exit()



while True :

  text = input('Digite alguma coisa para enviar (ou \"exit\" para sair do programa), e pressione Enter:\n')

  if text != 'exit' :

    print(f'\nVocê digitou: \"{text}\"')

    try:

      api.update_status(text)
      print(f'Texto tweetado para a timeline de @{user.screen_name}\n')

    except:

      print('Failed to send new tweet')
      exit()

  else :

    break
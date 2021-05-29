import os, tweepy
from dotenv import load_dotenv

load_dotenv()

class TweepyConnect :

  __consumer_key        = os.getenv('TWEEPY_CONSUMER_KEY')
  __consumer_secret     = os.getenv('TWEEPY_CONSUMER_SECRET')
  __access_token        = os.getenv('TWEEPY_ACCESS_TOKEN')
  __access_token_secret = os.getenv('TWEEPY_ACCESS_TOKEN_SECRET')

  api  = None
  user = None

  def __init__ (self) :

    if (self.__consumer_key        != None) and \
       (self.__consumer_secret     != None) and \
       (self.__access_token        != None) and \
       (self.__access_token_secret != None) :

      auth = tweepy.OAuthHandler(self.__consumer_key, self.__consumer_secret)
      auth.set_access_token(self.__access_token, self.__access_token_secret)

      self.api = tweepy.API(auth)

    else :

      print('Está faltando alguma varíavel de ambiente...')
      exit()

    try :

      self.user = self.api.verify_credentials()
      print(f'Autenticação do Tweepy OK! (conta: @{self.user.screen_name})\n')

    except :

      print('Erro durante autenticação do Tweepy')
      exit()

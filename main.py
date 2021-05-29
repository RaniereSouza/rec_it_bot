from tweepy_connect import TweepyConnect

tweepy = TweepyConnect()

if (not tweepy) or (not tweepy.api) or (not tweepy.user) :
  print('problemas na inicialização do Tweepy')
  exit()

while True :

  text = input('Digite alguma coisa para enviar (ou \"exit\" para sair do programa), e pressione Enter:\n')

  if text != 'exit' :

    print(f'\nVocê digitou: \"{text}\"')

    try:

      tweepy.api.update_status(text)
      print(f'Texto tweetado para a timeline de @{tweepy.user.screen_name}\n')

    except:

      print('Falha ao enviar novo tweet')
      exit()

  else :

    break
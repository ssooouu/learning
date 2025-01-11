from pprint import pprint
import requests



r = requests.get('https://centrezotov.ru/events/chto-takoe-memy-i-kak-oni-zhivut-sredi-lyudej/', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
pprint(r.text)
#Я не много что понял, но понял что я могу пользоваться поисковиком в PY ища что-то на сайте

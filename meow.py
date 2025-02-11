from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
meow_key = os.environ['MEOW']
API_BASE_URL = f'http://api.chuckfang.com/{meow_key}/'

def meow_send(title='', message=''):
    encoded_title = quote(title)
    encoded_message = quote(message)
    url = f'{API_BASE_URL}{encoded_title}/{encoded_message}'
    req = Request(url, method='GET')
    try:
        with urlopen(req) as response:
            result = response.read().decode('utf-8')
    except (URLError, HTTPError) as e:
        result = f'Error occurred: {e}'
    return result
  meow_send(title='Github｜TieBaSign', message='所有用户签到结束')

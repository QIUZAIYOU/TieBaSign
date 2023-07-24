import os
import urllib.parse
import urllib.request

server_chan_key = os.environ['SERVERCHAN']
def sc_send(text, desp='', key=server_chan_key):
    try:
        postdata = urllib.parse.urlencode({
            'text': text,
            'desp': desp
        }).encode('utf-8')
        url = f'https://sctapi.ftqq.com/{key}.send'
        req = urllib.request.Request(url, data=postdata, method='POST')
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
        return result
    except Exception as e:
        logger.error(f"server酱发送失败:{e}")

sc_send("Github｜TieBaSign｜所有用户签到结束")

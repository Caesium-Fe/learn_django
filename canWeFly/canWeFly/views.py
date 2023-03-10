from django.http import HttpResponse
from django_redis import get_redis_connection
import json

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

CONN_LIST = []


def index(request):
    return HttpResponse("alkjdslkjaskld")


def login(request):
    print('asd')
    conn = get_redis_connection('default')
    conn.set('xx3', 'oo3')
    s = conn.get('xx3')
    return HttpResponse(s)


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print("Link start....!")
        # 有客户端来向后端发送websocket连接的请求时，自动触发
        # 服务端允许和客户端创建连接（握手）
        self.accept()
        CONN_LIST.append(self)

    def websocket_receive(self, message):
        # 浏览器基于websocket向后端发送数据，自动触发接收消息
        print('接收的消息', message)
        # {'type': 'websocket.receive', 'text': '暗示健'}
        text = message['text']
        print("接收到消息-->", text)
        res = {'result': 'ok'}
        for conn in CONN_LIST:
            conn.send(json.dumps(res))

    def websocket_disconnect(self, message):
        CONN_LIST.remove(self)
        raise StopConsumer()

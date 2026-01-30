from flask import Blueprint, json, request
from .requestparse import push_parser


webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/status', methods=["GET"])
def status():
    return {"message": "ok"}, 200


@webhook.route('/receiver', methods=["POST"])
def receiver():
    # print(request.headers)
    # print(request.json)
    if request.headers['X-Github-Event'] == 'push':
        print(push_parser(request.json))
    elif request.headers['X-Github-Event'] == 'pull_request':
        print(push_parser(request.json))
    return {}, 200

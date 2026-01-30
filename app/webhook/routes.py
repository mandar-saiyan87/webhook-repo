from flask import Blueprint, json, request
from .requestparse import push_parser, pull_parser
from ..extensions import mongo
from datetime import datetime, timezone



webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/status', methods=["GET"])
def status():
    return {"message": "ok"}, 200


@webhook.route('/receiver', methods=["POST"])
def receiver():
    # print(request.headers)
    # print(request.json)

    event = None

    if request.headers['X-Github-Event'] == 'push':
        event = push_parser(request.json)
    elif request.headers['X-Github-Event'] == 'pull_request':
        event = pull_parser(request.json)

    if event:
        try:
            event['created_at'] = datetime.now(timezone.utc)
            mongo.db.events.insert_one(event)
        except Exception as e:
            print('Failed to create event log', e)

    return {}, 200


@webhook.route('/events', methods=["GET"])
def get_events():
    after = request.args.get('after')

    if after:
        events = mongo.db.events.find(
            {'created_at': {"$gt": datetime.fromisoformat(after)}}).sort('created_at', -1)

        events_list = []

        for event in events:
            event['_id'] = str(event['_id'])
            event['created_at'] = event['created_at'].isoformat()
            events_list.append(event)

    return {"events": events_list}, 200

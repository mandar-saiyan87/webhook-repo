def push_parser(eventdata):
    # push data model
    reuqest_id = eventdata['head_commit']['id']
    author = eventdata['head_commit']['author']['name']
    action = "push"
    from_branch = None
    to_branch = eventdata['ref'].split('/')[-1]
    timestamp = eventdata['head_commit']['timestamp'] 
    
    return {
        "request_id": reuqest_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }
    

def pull_parser(eventdata):

    # check if request status is open

    if eventdata['action'] != 'opened':
        return None

    # pull data model
    reuqest_id = eventdata['pull_request']['head']['sha']
    author = eventdata['pull_request']['user']['login']
    action = "pull_request"
    from_branch = eventdata['pull_request']['head']['ref']
    to_branch = eventdata['pull_request']['base']['ref']
    timestamp = eventdata['pull_request']['created_at']

    return {
        "request_id": reuqest_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

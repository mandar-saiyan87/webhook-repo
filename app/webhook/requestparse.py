def push_parser(eventdata):
    # data model
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
    

def filter_emails(messages, criterion="priority"):
    # Example filter implementation
    if criterion == "priority":
        return [msg for msg in messages if "important" in msg['snippet'].lower()]
    return messages

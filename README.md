# djangoMessageSystem

### urls:

`admin/` - opens admin page

`users/` - returns list of all users

`users/<int:pk>/` - returns json for specific user id

`messages/` - returns list of all messages

`messages/<int:pk>/` - returns specific message, according to id

`messages/unread/` - returns list of all unread messages, from all users

`messages/user/<int:pk>/` - returns list of messages pertaining to specific user, according to id.
extra params:
adding the param `sent_or_received` and giving it one of the following values -

1. `sent` - will return only sent messages

2. `received` - will return only received messages

3. `all` - will return all of users messages

e.g.:
`messages/user/2/?sent_or_received=sent`
will return all sent messages for user 2
                                  
`messages/user/unread/<int:pk>/` - returns all unread messages for specific user, according to id

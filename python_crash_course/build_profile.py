def build_profile(first, last, **user_info):
    # double asterisks before the parameter **user_info cause python
    # to create an empty dictionary and pack whatever name-value pairs
    # it receives into this dictionay
    """
    Build a dictionary containing everything we know about a user.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

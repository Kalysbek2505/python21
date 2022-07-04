def login_requered(obj):
    if not obj.is_authenticated:
        raise Exception('Юзер не авторизован')

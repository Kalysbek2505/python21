def generate_id(id_s):
    """
    Принимает список существующих id
    Возвращает новое id в диапозоне от 100 жо 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in id_s:
        id_ = random.randint(100, 1000)
    return id_

def valid_ate_password(p1, p2):
    """
    Принимает 2
    """
    if p1 != p2:
        raise Excetion('Пароли не совпадают')
def validate_id(ids, user_id):
    """
    Принимает список существующих id и id, которые нужно проверить                                                                         
    """
    if user_id not in ids:
        raise Exception('Такого юзера нет')
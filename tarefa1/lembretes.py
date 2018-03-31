from tarefa1.constants import LEMBRETE_KEY


def get_session(key, request):
    if key in request.session:
        return request.session.get(key)
    else:
        return None


def get_user_lembretes(username, request):
    lembrete_list = get_session(LEMBRETE_KEY, request) or {}
    if username in lembrete_list:
        return lembrete_list[username]
    return []


def save_user_lembrete(username, lembrete, request):
    lembrete_list = get_session(LEMBRETE_KEY, request) or {}
    user_lembrete_list = get_user_lembretes(username, request)

    user_lembrete_list.append(lembrete)
    lembrete_list[username] = user_lembrete_list

    request.session[LEMBRETE_KEY] = lembrete_list

from django.shortcuts import render
def get_base_context():
    context = {
        'menu': [
            {'link': '/', 'text': 'Главная'},
            {'link': '/profile_in/', 'text': 'Профиль'},
            {'link': '/register', 'text': 'Регистрация'},
            #
            # {'link': '/voting_list', 'text': 'Голосования'},
            # {'link': '/add_voting', 'text': 'Добавить голосование'},
            # {'link': '/report_in', 'text': 'Жалоба'},
        ],
        'main_header': 'Hockey App',
    }
    return context


def index_page(request):
    context = get_base_context()
    context['title'] = 'Главная страница - Hockey App'
    return render(request, 'index.html', context)
# Create your views here.

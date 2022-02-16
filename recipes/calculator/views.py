from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def home_view(request):
    context = {
        'recipes': {
            'Омлет': 'omlet',
            'Паста': 'pasta',
            'Бутер': 'buter'
        }
    }
    return render(request, 'calculator/home.html', context)

def recipe_view(request, name_path):
    number = int(request.GET.get('amount', 1))
    dict_temp = DATA[f'{name_path}'].copy()
    for key, value in dict_temp.items():
        dict_temp[key] = dict_temp[key] * number

    context = {
        'home': reverse('home'),
        'recipe': dict_temp,
    }

    return render(request, 'calculator/index.html', context)

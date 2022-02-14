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
    path_recipe = reverse('recipe')
    context = {
        'recipes': {
            'Омлет': f"{path_recipe}?rec=1",
            'Паста': f"{path_recipe}?rec=2",
            'Бутер': f"{path_recipe}?rec=3"
        }
    }
    return render(request, 'calculator/home.html', context)

def recipe_view(request):
    param = request.GET.get("rec")
    context = {
        'home': reverse('home'),
    }
    if param == '1':
        context['recipe'] = DATA['omlet']
    elif param == '2':
        context['recipe'] = DATA['pasta']
    elif param == '3':
        context['recipe'] = DATA['buter']
    return render(request, 'calculator/index.html', context)

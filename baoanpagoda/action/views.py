from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from . models import ActionsCategory, Action
# Create your views here.


def action(request, category_slug=None):
    category = get_object_or_404(ActionsCategory, en_slug=category_slug)
    action_list = Action.objects.filter(category=category)
    paginator = Paginator(action_list, 5)
    page = request.GET.get('page')
    action_lists = paginator.get_page(page)

    actions_categories = ActionsCategory.objects.all()
    return render(request, 'actions.html', {'action_lists': action_lists,
                                            'actions_categories': actions_categories,
                                            'category': category})
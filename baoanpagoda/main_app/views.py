from django.shortcuts import render
from . models import ImageLanding, Menu, SubMenu
from collections import defaultdict


# Create your views here.
def index(request):
    imagelanding = ImageLanding.objects.latest('created_at')
    menus = Menu.objects.all()
    submenus = SubMenu.objects.all()

    # Create a list of dictionaries where each dictionary represents a menu and its associated submenus
    menu_data = []
    for menu_item in menus:
        submenu_data = {
            'menu': menu_item,
            'submenus': submenus.filter(menu=menu_item)
        }
        menu_data.append(submenu_data)

    context = {
        'imagelanding': imagelanding,
        'menu_data': menu_data,  # Pass the list of dictionaries to the template
    }
    return render(request, 'main_app/index.html', context=context)

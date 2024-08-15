from django.shortcuts import render

from .models import Goods
from .forms import GoodForm


# Create your views here.



def goods_list(request):
    goods = Goods.objects.all()

    context = {
        'goods': goods,
    }

    return render(request, template_name='goods_index.html', context=context)

def add_goods(request):
    goods = Goods.objects.all()
    context = {
        'goods': goods,
    }
    if request.method == 'POST':
        form = GoodForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            good = form.save(commit=False)
            if request.user.is_authenticated:
                good.user = request.user
            form.save()
            return render(request, template_name='goods_index.html', context=context)
    else:
        form = GoodForm(user=request.user)
    return render(request, 'goods_add.html', {'form': form})


def goods_detail(request, pk):
    good = Goods.objects.get(pk=pk)
    context = {'good': good}
    return render(request, 'goods_detail.html', context=context)

def goods_search(request):
    goods = Goods.objects.all()
    search = request.GET['search']
    context = {
        'goods': goods,
        'search': search
    }
    return render(request, template_name='goods_search.html', context=context)

from django.http import request
from django.shortcuts import render
import random
# Create your views here.
fortuneList=[
    'rumi : the essence of life is dying before death',
    'Al-Quran : I seek refuge of Allah from devil',
    '''My Prophet : best amoung you are those who are best to their families 
    and I am best to my family '''
]

def home(request):
  fortune = random.choice(fortuneList)
  context = {'fortune':fortune}
  return render(request, 'randomfortune\home.html',context )
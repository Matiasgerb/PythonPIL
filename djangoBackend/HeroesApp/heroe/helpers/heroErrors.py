from heroe.models import Hero

def hayHero(pk):

    try:
        heroe = Hero.objects.get(pk=pk)

        return [True,heroe]
    except:
        return [False]

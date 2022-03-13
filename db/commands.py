from asgiref.sync import sync_to_async
from agro.models import Questions, User, ZontImages, Zonts


@sync_to_async
def add_user(user_id, fullname):
    try:
        return User(user_id=user_id, name=fullname).save()

    except Exception as err:
        print(err)


@sync_to_async
def get_user(user_id):
    try:
        return User.objects.get(user_id=user_id)
    except Exception as err:
        print(err)


@sync_to_async
def get_users():
    try:
        return User.objects.all()
    except Exception as err:
        print(err)


@sync_to_async
def get_zont_by_user(user):
    try:
        zont = Zonts.objects.filter(user=user).order_by("-id")[0]
        zont_id = zont.zont_id
        zont_images = ZontImages.objects.get(zont_id=zont_id)
        images = str(zont_images.images).split(",")
        return images

    except Exception as er:
        print(er)
        return None



@sync_to_async
def get_zont_by_id(zont_id):
    try:
        return Zonts.objects.get(id=zont_id)
    except:
        return None


@sync_to_async
def get_question(question_id):
    try:
        return Questions.objects.get(id=question_id)
    except:
        return None



@sync_to_async
def get_questions():
    try:
        return Questions.objects.all()
    except:
        return None
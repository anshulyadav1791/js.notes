from django.http import HttpResponse

def set_cookie(request):
    response = HttpResponse("cookie set successfully")
    response.set_cookie('username', 'anshu', max_age=60*60*24)
    response.set_cookie('course', 'django full course', max_age=60*60*24)
    return response


def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    course = request.COOKIES.get('course', 'no course selected')

    if 'username' in request.COOKIES:
        return HttpResponse(f'Username: {username}, Course: {course}')
    else:
        return HttpResponse('no cookies found')


def delete_cookie(request):
    response = HttpResponse('cookie deleted successfully')
    response.delete_cookie('username')
    response.delete_cookie('course')
    return response

from django.http import HttpResponse


def set_session(request):
    request.session['username'] = 'mohit'
    request.session['course'] = 'Django'
    return HttpResponse('Session data saved successfully.')


def get_session(request):
    username = request.session.get('username', 'Guest')
    course = request.session.get('course', 'Nothing')

    return HttpResponse(f'Welcome: {username}, you are learning {course}')


def delete_session(request):
    request.session.flush()
    return HttpResponse('Session deleted successfully.')

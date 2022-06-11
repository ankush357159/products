from django.urls import path
from bunny.views import home, myPetCreateView, setCookie, getCookie, test_delete, test_session, save_session_data, access_saved_data, delete_session_data, decode_session_data


urlpatterns = [
    path('home/', home, name='home'),
    path('create-pet/', myPetCreateView, name='create-my-pet'),
    path('set-cookie/', setCookie, name='set-cookie'),
    path('get-cookie/', getCookie, name='get-cookie'),
    path('test-delete/', test_delete, name='test_delete'),
    path('test-session/', test_session, name='test-session'),
    path('save-session-data/', save_session_data, name='save-session-data'),
    path('access-saved-session/', access_saved_data, name='access-saved-session'),
    path('delete-session-data/', delete_session_data, name='delete-session-data'),
    path('decode_session_data/', decode_session_data, name='decode_session_data'),
]
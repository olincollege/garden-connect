"""
Establishing URL pathways accessible for sending direct messages
to specific users
"""
from django.urls import path
from direct.views import inbox, user_search, directs, new_conversation, send_direct # pylint: disable=E0401
urlpatterns = [
   	path('', inbox, name='inbox'),
   	path('directs/<username>', directs, name='directs'),
   	path('new/', user_search, name='usersearch'),
   	path('new/<username>', new_conversation, name='newconversation'),
   	path('send/', send_direct, name='send_direct'),
]

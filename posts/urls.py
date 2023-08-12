#from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns=[
#I am using index method
#url(r'^$', views.home, name='home')
#path('',views.)
#path('admin/', admin.site.urls),
path('',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
path('home/',views.home,name='home'),
path('twitterdata/',views.twitterdata,name='twitterdata'),
path('topicmodeling/',views.topicmodeling,name='topicmodeling'),
path('speechrecognition/',views.speechrecognition,name="speechrecognition"),
path('textdata/',views.textdata,name='textdata'),
path('currenttweetsform/',views.currenttweetsform,name='currenttweetsform'),
path('oldtweets/',views.oldtweets,name='oldtweets'),
path('getusertimeline/',views.getusertimeline,name='getusertimeline'),
path('sentiment/',views.sentiment,name='sentiment'),
path('pdfdata', views.pdfdata,name='pdfdata'),
path('csvdata/',views.csvdata,name='csvdata'),
path('sample_upload/',views.sample_upload,name='sample_upload'),
path('date_upload_format/',views.date_upload_format,name='date_upload_format'),
path('current_upload/',views.current_upload,name='current_upload'),

#path('upload/',views.upload,name='upload'),

#path('currenttweetsform/',views.currenttweetsform,name='currenttweetsform'),
path('currenttweetshashtagform/',views.currenttweetshashtagform,name='currenttweetshashtagform'),
path('oldtweets/',views.oldtweets,name='oldtweets'),
path('usertimeline/',views.usertimeline,name='usertimeline'),
path('getfollowerlist/',views.getfollowerlist,name='getfollowerlist'),
path('upload_file_currenttweets/',views.upload_file_currenttweets,name='upload_file_currenttweets'),
path('upload_file_currenttweets_hashtags/',views.upload_file_currenttweets_hashtags,name='upload_file_currenttweets_hashtags'),
path('upload_file_oldtweets/',views.upload_file_oldtweets,name='upload_file_oldtweets'),
path('upload_file_speech/',views.upload_file_speech, name='upload_file_speech'),
path('csv_file_upload/',views.csv_file_upload,name='csv_file_upload'),
path('text_file_upload/',views.text_file_upload,name='text_file_upload'),
path('sentiment_analysis/',views.sentiment_analysis,name='sentiment_analysis'),
path('pdf_lda/',views.pdf_lda,name='pdf_lda'),
path('pdf_dominant_topic_lda/',views.pdf_dominant_topic_lda,name='pdf_dominant_topic_lda'),

path('text_format_sentence/',views.text_format_sentence,name='text_format_sentence'),
path('format_sentence/',views.format_sentence,name='format_sentence'),

]


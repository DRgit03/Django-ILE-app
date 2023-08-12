from django import forms
import datetime


class EmailForm(forms.Form):
	recipient_email_address = forms.EmailField()

class CurrentTweetForm(forms.Form):
	username=forms.CharField(label='Username', max_length=100)
	items=forms.IntegerField(min_value=1, label="maximumtweets")
	recipient_email_address = forms.EmailField()

class CurrentTweetHashtagForm(forms.Form):
	username=forms.CharField(label='Username',max_length=100)
	items=forms.IntegerField(min_value=1, label="maximumtweets")
	recipient_email_address = forms.EmailField()

class OldTweetForm(forms.Form):
	username=forms.CharField(label='Username', max_length=100)
	since=forms.DateField(widget=forms.widgets.DateInput(format="%Y-%m-%d"))
	#until=forms.DateField(label="dateuntil",input_formats='%Y-%m-%d')
	until=forms.DateField(widget=forms.widgets.DateInput(format="%Y-%m-%d"))
	maxtweets=forms.IntegerField(min_value=1, label="maximumtweets")
	recipient_email_address = forms.EmailField()

class GetUserTimelineForm(forms.Form):
    username = forms.CharField(label="username",max_length=100 )
    items=forms.IntegerField(min_value=1, label="maximumtweets")
    recipient_email_address = forms.EmailField()


class GetFollowerslistForm(forms.Form):
    username = forms.CharField(label="username",max_length=100 )
    items=forms.IntegerField(min_value=1, label="maximumtweets")
    recipient_email_address = forms.EmailField()


#class FileFieldForm(forms.Form):
    #file_field = forms.FileField()
#class FileFieldForm(forms.Form):
    #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True})

class lda_mod(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")   

class csv_lda_mod(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")
    recipient_email_address = forms.EmailField()

class text_lda_mod(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")   

class text_lda_mode(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")
    recipient_email_address = forms.EmailField()

class pdf_lda_mod(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")

class pdf_lda_mode(forms.Form):
    total_topics  = forms.IntegerField(min_value=1, label="total_topics" )
    number_words  = forms.IntegerField(min_value=1, label="number_words")
    recipient_email_address = forms.EmailField()

 

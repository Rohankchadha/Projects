from django import forms

class Student(forms.Form):
	stud_name=forms.CharField(label="Student Name", max_length=200),
	stud_class=forms.CharField(label="Student Class", max_length=200),
	stud_section=forms.CharField(label="Student Section", max_length=200),
	stud_roll=forms.CharField(label="Student Roll No", max_length=200),
	stud_email=forms.CharField(label="Student email", max_length=200),
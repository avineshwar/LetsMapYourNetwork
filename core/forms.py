from django import forms
from .models import Machine

class GoToForm(forms.Form):
    goto_target = forms.CharField(max_length=100,label="",initial="[Destination Host]")

class ProjectForm(forms.Form):
    PROJECT_CHOICES = [("default","default")]
    for node in Machine.nodes:
        tuple = (str(node.tag).split("#")[0],str(node.tag).split("#")[0])
        PROJECT_CHOICES.append(tuple)
    PROJECT_CHOICES = list(set(PROJECT_CHOICES))
    PROJECT_CHOICES.sort()
    project = forms.CharField(widget=forms.Select(choices=PROJECT_CHOICES),label="")


class NewProjectForm(forms.Form):
    newproject = forms.CharField(label="", initial="[Project Name]")

class ScanForm(forms.Form):
    scanrange = forms.CharField(label="", initial="[Target IP Range]")

class CMDBScanForm(forms.Form):
    cmdb_file = forms.FileField()


class AWSForm(forms.Form):
    access_key = forms.CharField(label="",initial="[AWS Access Key]")
    access_id = forms.CharField(label="", initial="[AWS Access ID]")


class AzureForm(forms.Form):
    access_key = forms.CharField(label="", initial="[Azure Access Key]")
    access_id = forms.CharField(label="", initial="[Azure Access ID]")
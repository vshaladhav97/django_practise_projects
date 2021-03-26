import csv
from .models import Data
from django import forms

class DataImport(forms.ModelForm):
    file_to_import = forms.FileField()

    class Meta:
        model = Data
        fields = ("file_to_import", "place")

    def save(self, commit=False, *args, **kwargs):
        form_input = DataImport()
        self.place = self.cleaned_data['place']
        file_csv = request.FILES['file_to_import']
        datafile = open(file_csv, 'rb')
        records = csv.reader(datafile)
        for line in records:
            self.time = line[1]
            self.data_1 = line[2]
            self.data_2 = line[3]
            self.data_3 = line[4]
            form_input.save()
        datafile.close()
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker

import datetime
from django.utils import formats

from cards.models import Card, ExtendCardRequest


class CardFormForTraineeEnroll(forms.ModelForm):
    start_at = forms.DateField(
        label=_('Start at'),
        widget=DatePicker(options={
            'useCurrent': True,
        }, attrs={
            'placeholder': _('Please enter the value'),
            'disabled': True
        }),
    )
    end_at = forms.DateField(
        label=_('End at'),
        widget=DatePicker(options={
            'useCurrent': True,
        }, attrs={
            'placeholder': _('Please enter the value'),
            'readonly': True
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['card_type'].empty_label = _('Please select a value')
        if kwargs.get('initial') is not None:
            if kwargs.get('initial').get('card_type_list') is not None:
                self.fields['card_type'].queryset = kwargs['initial']['card_type_list']

        self.helper = FormHelper()
        self.helper.form_id = 'form_enroll'
        self.helper.layout = Layout(
            'card_type',
            'start_at',
            'end_at',
            HTML("""
                <div id='trial-lesson' class="mt-3 d-none">
                    <h4 class="mb-1">{}</h4>
                    <p>{}</p>
                    <div id='trial-lesson-listing'>
                    </div>
                </div>
            """.format(
                _('Trial Lesson'),
                _('Please drap a lesson into this area below to choose'))),
            HTML("""
                <div id='div_for_some_lesson_list' class="mt-3 mb-2 d-none">
                    <h4 class="mb-1">{}</h4>
                    <p>{}</p>
                    <div id='some_lesson_list'>
                    </div>
                </div>
            """.format(
                _('Lesson List'),
                _('Lessons you choose will be displayed here'))),
            Submit('submit', _('Save'), css_class='btn-success'))

        # Focus on form field whenever error occurred
        errorList = list(self.errors)
        if errorList:
            for item in errorList:
                if item == '__all__':
                    break
                self.fields[item].widget.attrs.update(
                    {'autofocus': 'autofocus'})
                break
        else:
           self.fields['card_type'].widget.attrs.update(
               {'autofocus': 'autofocus'})

    class Meta:
        model = Card
        exclude = ['created_at', 'updated_at',
                   'yogaclass', 'trainee', 'lessons']

    def clean_end_at(self):
        cleaned_data = super(CardFormForTraineeEnroll, self).clean()
        end_at = cleaned_data['end_at']
        if 'start_at' in cleaned_data and end_at is not None:
            start_at = cleaned_data['start_at']
            if end_at < start_at:
                raise forms.ValidationError(
                    _('End at must be greater than Start at'))
        return end_at

    def clean(self):
        cleaned_data = super(CardFormForTraineeEnroll, self).clean()
        if 'start_at' in cleaned_data and 'end_at' in cleaned_data:
            start_at = cleaned_data['start_at']
            end_at = cleaned_data['end_at']
            if start_at is not None and end_at is not None:
                    if self.initial.get('yoga_class') is not None:
                        yoga_class = self.initial.get('yoga_class')
                        lesson_list = yoga_class.lessons.filter(
                            date__range=[start_at, end_at])
                        if not lesson_list:
                            raise forms.ValidationError(
                                _('Your range time does not have any lessons'))
        return cleaned_data


class ExtendCardRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_expire_date'] = forms.DateField(
            label=_('new expire date').capitalize(),
            widget=DatePicker(options={
                'useCurrent': True,
            }, attrs={
                'placeholder': 'Vui lòng chọn ngày'
            }),
        )
        self.fields['reason'].widget.attrs = {
            'rows': 4
        }
        self.helper = FormHelper()
        self.helper.form_show_errors = True
        self.helper.form_id = 'form_new_extend_card_request'
        self.helper.layout = Layout(
            'new_expire_date',
            'reason',
            HTML("""
                <div id='extend_lesson' class="mt-3 mb-3 d-none">
                    <h4 class="mb-1">{}</h4>
                    <p>{}</p>
                    <div id='extend_lesson_list'>
                    </div>
                </div>
            """.format(
                _('Extend Lesson'),
                _('Lessons will be added to your card'))),
            Submit('submit', _('Save'), css_class='btn-success'))

    class Meta:
        model = ExtendCardRequest
        exclude = ['created_at', 'updated_at', 'state', 'card']

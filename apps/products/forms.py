from django import forms


class ReservationForm(forms.Form):

    PERSON_CHOICES =(
        ("1", "1 Человек"),
        ("2", "2 Человека"),
        ("3", "3 Человека"),
        ("4", "4 Человека"),
        ("5", "5 Человека"),
        ("6", "6 Человека"),
        ("7", "7 Человека"),
        ("8", "8 Человека"),
        ("9", "9 Человека"),
        ("10", "10 Человека")
    )

    full_name = forms.CharField(
        max_length=300, 
        label='Полное Имя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Как к вам обращаться?'
                }
            )
    )

    sender = forms.EmailField(
        max_length=200, 
        label='Ваш Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
                }
            )
    )

    phone_number = forms.CharField(
        max_length=11, 
        label='Ваш номер телефона',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
                }
            )
    )

    how_many_person = forms.ChoiceField(
        choices=PERSON_CHOICES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    date = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'datepicker',
                'placeholder': 'Дата резерва',
                'autocomplete': 'off'
                }
            )
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Отправьте нам сообщение'
                }
            )
        )

    time = forms.CharField(
        label='Time',
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите время резерва. Например 18:30'
            }
        )
    )

    def clean_time(self):
        time = self.cleaned_data['time']
        try:
            hours, minutes = map(int, time.split(':'))
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return f'{hours:02d}:{minutes:02d}'
            else:
                raise forms.ValidationError('Не праильный формат времени.')
        except ValueError:
            raise forms.ValidationError('Не праильный формат времени.')
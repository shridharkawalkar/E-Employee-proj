from django.forms import ModelForm, DateField
from dashboard.models import Employee
invalid_date_error_messages = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}
class EmployeeForm(ModelForm):
    class Meta:
        dob = DateField(required=False, input_formats='%Y-%m-%d', error_messages=invalid_date_error_messages)
        joining_date = DateField(required=False, input_formats='%Y-%m-%d', error_messages=invalid_date_error_messages)

        model = Employee
        fields = ["first_name","last_name", "dob", "joining_date", "permanent_address", "designation", "department", "email", "gender", "phone_number"]
        labels = {
            'dob': ('Date Of Birth'),
        }
#         help_texts = {
#             'dob': ('Enter Date of Birth'),
#         }
        error_messages = {
            'dob': {
                'invalid': ("Enter valid dob in yyyy-mm-dd fromat"),
            },
            'joining_date': {
                'invalid': ("Enter valid joining date in yyyy-mm-dd fromat"),
            },            
        }        

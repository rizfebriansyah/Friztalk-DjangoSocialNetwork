from django.test import SimpleTestCase
from userprofiles.forms import UserPostModelForm, RemarkModelForm

class TestForms(SimpleTestCase):

    def test_user_post_model_form_valid_data(self):
        form = UserPostModelForm(data={
            'content': 'userpost1',
        })

        self.assertTrue(form.is_valid())

    def test_user_post_model_form_no_data(self):
        form = UserPostModelForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)

    def test_remark_model_form_valid_data(self):
        form = RemarkModelForm(data={
            'body': 'remark1',
        })

        self.assertTrue(form.is_valid())

    def test_remark_model_form_no_data(self):
        form = RemarkModelForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
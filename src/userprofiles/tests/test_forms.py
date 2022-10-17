from django.test import SimpleTestCase
from userprofiles.forms import ProfilePageModelForm

class TestForms(SimpleTestCase):

    def test_profile_page_model_form_valid_data(self):
        form = ProfilePageModelForm(data={})

        self.assertTrue(form.is_valid())

    def test_profile_page_model_form_no_data(self):
        form = ProfilePageModelForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),0)

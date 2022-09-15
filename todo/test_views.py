from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertCountEqual(response, 'todo/todo_list.html')

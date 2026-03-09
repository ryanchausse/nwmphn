# Run from project root with python -m unittest discover ./tests
import json # bad practice, but just in case
import unittest
import requests

# The goal of this test is to add a new Thing via the POST http verb:
# curl -i -X POST -H 'Content-Type: application/json' -d '{"id": 1, "name": "New Thing", "description": "New Thing Added By Posting", [etc.]}' http://127.0.0.1:8000/things
class TestCreateAThing(unittest.TestCase):
    def test_post_thing(self):
        url = "http://127.0.0.1:8000/things"
        thing_to_create = {
            "id": 1,
            "name": "New Thing",
            "description": "New Thing Added By Posting",
            "price": 99.99,
            "created_at": "2026-03-09 17:44:25.761008"
        }

        expected_thing_response = {
            "id": 1,
            "name": "New Thing",
            "description": "New Thing Added By Posting"
        }

        response = requests.post(url, json=thing_to_create)

        self.assertEqual(response.json(), expected_thing_response)


# The goal of this test is to replace a Thing via the PUT http verb:
class TestReplaceAThing(unittest.TestCase):
    def test_put_thing(self):
        thing_id = str(0)
        url = "http://127.0.0.1:8000/things/" + thing_id
        replacement_thing = {
            "id": 2,
            "name": "Replaced Thing",
            "description": "Replaced Thing via PUT",
            "price": 12.12,
            "created_at": "2026-03-09 17:55:25.761008"
        }

        expected_replaced_thing_response = {
            "id": 2,
            "name": "Replaced Thing",
            "description": "Replaced Thing via PUT"
        }

        response = requests.put(url, json=replacement_thing)

        self.assertEqual(response.json(), expected_replaced_thing_response)


# The goal of this test is to partially update a Thing via the PATCH verb
# TODO: add setUp() and tearDown() functions to make this more clear
class TestUpdateAThing(unittest.TestCase):
    def test_patch_thing(self):
        thing_id = str(1)
        url = "http://127.0.0.1:8000/things/" + thing_id
        updated_thing = {
            "name": "Updated Thing",
            "price": 9.95,
            "created_at": "2026-03-09 18:15:25.761008"
        }

        expected_updated_thing_response = {
            "id": 1,
            "name": "Updated Thing",
            "description": "New Thing Added By Posting"
        }

        response = requests.patch(url, json=updated_thing)

        self.assertEqual(response.json(), expected_updated_thing_response)

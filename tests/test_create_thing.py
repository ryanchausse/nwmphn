# The goal of this test is to add a new Thing via the POST http verb:
# curl -i -X POST -H 'Content-Type: application/json' -d '{"id": 1, "name": "New Thing", "description": "New Thing Added By Posting", [etc.]}' http://127.0.0.1/things
# Run from project root with python -m unittest discover ./tests

import json
import unittest
import requests

class TestPostToThings(unittest.TestCase):
    def test_create_thing(self):
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

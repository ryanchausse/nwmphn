# Run from project root with python -m unittest discover ./actual_test/tests
import unittest
import requests
import uuid

# The goal of this test is to add a new Client via the POST http verb:
# curl -i -X POST -H 'Content-Type: application/json' -d '{"id": 1, "name": "New Client", "description": "New Client Added By Posting", [etc.]}' http://127.0.0.1:8000/clients
class TestCreateAClient(unittest.TestCase):
    def test_post_client(self):
        url = "http://127.0.0.1:8000/clients"
        client_to_create = {
            "id": 1,
            "client_key": uuid.uuid4(),
            "slk": "LKE102310",
            "forename": "Ryan",
            "family_name": "Chausse",
            "date_of_birth": "1986-01-01",
            "intersex": 1,
            "phone": "0418759273"
        }

        expected_client_response = {
            "id": 1,
            "family_name": "Chausse",
            "forename": "Ryan",
            "phone": "0418759273",
        }

        response = requests.post(url, json=client_to_create)

        self.assertEqual(response.json(), expected_client_response)


class TestGetAClient(unittest.TestCase):
    def test_get_client(self):
        client_id = str(1)
        url = "http://127.0.0.1:8000/clients" + client_id
        
        expected_client_response = {
            "id": 1,
            "family_name": "Chausse",
            "forename": "Ryan",
            "phone": "0418759273",
        }

        response = requests.get(url)

        self.assertEqual(response.json(), expected_client_response)


class TestGetAClientThatDoesNotExist(unittest.TestCase):
    def test_get_client_that_does_not_exist(self):
        client_id = str(999)
        url = "http://127.0.0.1:8000/clients" + client_id
        
        expected_response_status_code = 404

        response = requests.get(url)

        self.assertEqual(response.status_code(), expected_response_status_code)

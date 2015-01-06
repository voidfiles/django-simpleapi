import json

from django.test import TestCase


class SimpleApiTestCase(TestCase):
    def test_simple_resp(self):
        resp = self.client.get('/test1')
        self.assertEquals(resp.status_code, 200)

        result = json.loads(resp.content)

        self.assertIn('meta', result)
        self.assertIn('data', result)
        self.assertIn('code', result['meta'])
        self.assertEquals(result['meta']['code'], 200)
        self.assertEquals(result['data']['value'], True)

    def test_bad_response(self):
        resp = self.client.get('/test2')
        self.assertEquals(resp.status_code, 400)

        result = json.loads(resp.content)

        self.assertIn('meta', result)
        self.assertNotIn('data', result)
        self.assertIn('code', result['meta'])
        self.assertEquals(result['meta']['code'], 400)

        self.assertIn('error_message', result['meta'])
        self.assertEquals("Missing data", result['meta']['error_message'])
        self.assertIn('error_slug', result['meta'])
        self.assertEquals('missing-data', result['meta']['error_slug'])

    def test_unhandled(self):
        resp = self.client.get('/test3')
        self.assertEquals(resp.status_code, 500)

        result = json.loads(resp.content)

        self.assertIn('meta', result)
        self.assertNotIn('data', result)
        self.assertIn('code', result['meta'])
        self.assertEquals(result['meta']['code'], 500)


class ExportApiTestCase(TestCase):
    def test_simple_resp(self):
        resp = self.client.get('/api/v1/test1/')
        self.assertEquals(resp.status_code, 200)

        result = json.loads(resp.content)

        self.assertEquals(result['data']['value'], True)

    def test_params(self):
        resp = self.client.get('/api/v1/test2/1')
        self.assertEquals(resp.status_code, 200)

        result = json.loads(resp.content)

        self.assertEquals(result['data']['value'], '1')

    def test_cors(self):
        response = self.client.options('/api/v1/test1/', HTTP_ORIGIN='http://localhost:9000', HTTP_ACCESS_CONTROL_REQUEST_METHOD='GET')
        assert response.status_code == 200
        assert response['Access-Control-Allow-Origin'] == 'http://localhost:9000'
        response = self.client.get('/api/v1/test1/', HTTP_ORIGIN='http://localhost:9000')
        assert response['Access-Control-Allow-Origin'] == 'http://localhost:9000'

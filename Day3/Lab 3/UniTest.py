from flask import Flask, jsonify
import unittest

app = Flask(__name__)

# Sample function to test
def calculate_area(radius):
    return 3.14 * radius * radius

@app.route('/area/<int:radius>', methods=['GET'])
def area(radius):
    return jsonify(area=calculate_area(radius))

# Unit Test for calculate_area function
class TestAPI(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(2), 12.56)
        self.assertEqual(calculate_area(0), 0)

    def test_area_endpoint(self):
        with app.test_client() as client:
            response = client.get('/area/3')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'area', response.data)

if __name__ == "__main__":
    unittest.main()

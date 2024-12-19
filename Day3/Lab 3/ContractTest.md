### **Step-by-Step Lab for API Contract Testing with a Mock API Provider**

This lab will guide you through setting up a complete contract testing environment in Python, including a mock API provider, a consumer, and automated tests to validate the contract.

---

### **Lab Objectives**
1. Simulate a backend API provider.
2. Create a consumer that interacts with the API.
3. Define a contract and validate it through tests.

---

### **Pre-requisites**
- Python 3.7 or later installed.
- Virtual environment setup (`venv` or similar).
- Basic understanding of Flask and pytest.

---

### **Step 1: Lab Setup**
1. **Create a project folder:**
   ```bash
   mkdir api_contract_testing_lab && cd api_contract_testing_lab
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install required packages:**
   ```bash
   pip install flask pytest requests
   ```

---

### **Step 2: Mock API Provider**
1. **Create the `mock_provider.py` file:**
   ```bash
   touch mock_provider.py
   ```

2. **Add the following code:**
   ```python
   from flask import Flask, jsonify, request

   app = Flask(__name__)

   # Mock user data
   users = {
       1: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
       2: {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"},
   }

   @app.route("/users/<int:user_id>", methods=["GET"])
   def get_user(user_id):
       user = users.get(user_id)
       if user:
           return jsonify(user), 200
       return jsonify({"error": "User not found"}), 404

   @app.route("/users", methods=["POST"])
   def create_user():
       data = request.json
       new_id = max(users.keys()) + 1
       users[new_id] = {"id": new_id, **data}
       return jsonify(users[new_id]), 201

   if __name__ == "__main__":
       app.run(port=5000, debug=True)
   ```

3. **Run the API mock:**
   ```bash
   python mock_provider.py
   ```

   The mock API is now running at `http://localhost:5000`.

---

### **Step 3: Create the API Consumer**
1. **Create the `consumer.py` file:**
   ```bash
   touch consumer.py
   ```

2. **Add the following code:**
   ```python
   import requests

   class APIClient:
       def __init__(self, base_url):
           self.base_url = base_url

       def get_user(self, user_id):
           response = requests.get(f"{self.base_url}/users/{user_id}")
           return response.json()

       def create_user(self, name, email):
           payload = {"name": name, "email": email}
           response = requests.post(f"{self.base_url}/users", json=payload)
           return response.json()
   ```

3. **Test the consumer manually:**
   ```python
   if __name__ == "__main__":
       client = APIClient("http://localhost:5000")
       print(client.get_user(1))
       print(client.create_user("Alice", "alice@example.com"))
   ```

---

### **Step 4: Define Contract Tests**
1. **Create the `test_contract.py` file:**
   ```bash
   touch test_contract.py
   ```

2. **Add the following test code:**
   ```python
   import pytest
   from consumer import APIClient

   @pytest.fixture
   def client():
       return APIClient("http://localhost:5000")

   def test_get_user(client):
       user = client.get_user(1)
       assert user["id"] == 1
       assert user["name"] == "John Doe"
       assert user["email"] == "john.doe@example.com"

   def test_create_user(client):
       new_user = client.create_user("Alice", "alice@example.com")
       assert new_user["name"] == "Alice"
       assert new_user["email"] == "alice@example.com"
   ```

---

### **Step 5: Run the Tests**
1. **Execute the tests with pytest:**
   ```bash
   pytest test_contract.py
   ```

2. **Verify all tests pass:**
   - Successful output:
     ```
     ============================= test session starts =============================
     collected 2 items

     test_contract.py ..                                               [100%]

     ============================== 2 passed in 0.05s ==============================
     ```

---

### **Step 6: Add More Endpoints**
Expand the mock provider and consumer by adding more routes and test cases as needed. For example:
- Add a DELETE route in the mock API.
- Update the consumer to call the DELETE route.
- Write a test case for deleting a user.

---

### **Step 7: Clean Up**
1. Stop the mock provider:
   ```bash
   Ctrl+C
   ```
2. Deactivate the virtual environment:
   ```bash
   deactivate
   ```

---

### **Lab Summary**
In this lab, you:
- Built a mock API provider using Flask.
- Created a consumer that interacts with the mock API.
- Wrote contract tests to validate the API behavior.

This setup is easily extendable for real-world applications. Let me know if you'd like more advanced features!

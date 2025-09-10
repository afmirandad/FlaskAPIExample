
#!/bin/bash
# Registro de usuario
curl -X POST http://localhost:5000/users/register -H "Content-Type: application/json" -d '{"username": "usuario1", "password": "password1"}'

# Login y captura de token
TOKEN=$(curl -s -X POST http://localhost:5000/users/login -H "Content-Type: application/json" -d '{"username": "usuario1", "password": "password1"}' | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])")

# Listado de usuarios usando el token capturado
curl -X GET http://localhost:5000/users/ -H "Authorization: Bearer $TOKEN"

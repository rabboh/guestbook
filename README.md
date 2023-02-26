# guestbook
Python(Django) / React guestbook project - study project

curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/api/ -d '{"nickname": "Nyuszi", "email": "guestmail@guestmail.com", "message": "Masodik nyuszi uzenet"}'

curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/api/

There is no authentication here, as it is a public guestbook.
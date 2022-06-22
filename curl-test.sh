#!/bin/bash
curl --request POST http://localhost:5000/api/timeline_post -d 'name=David&email=davidlazaro20@hotmail.com&content=test{"content":"Test"}
curl http://localhost:5000/api/timeline_post

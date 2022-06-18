#!/bin/bash
cd project-snake-snakeeeeeeeee
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
flask run

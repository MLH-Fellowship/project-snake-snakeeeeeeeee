#!/bin/bash
tmux kill-server
tmux new -s server ./redeploy-site.sh

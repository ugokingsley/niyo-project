#!/bin/bash
cd /niyo/
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm niyo.wsgi:application --bind "0.0.0.0:8000"
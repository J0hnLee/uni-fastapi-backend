#!/bin/sh

# 啟動 consumer.py 並讓它在背景運行
python3 consumer.py &

# 啟動 uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

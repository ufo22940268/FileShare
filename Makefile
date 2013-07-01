all:
	echo "success!"

server:
	python server.py

.DEFAULT_GOAL := server

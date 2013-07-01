all:
	echo "success!"

server:
	python flleshare_server.py

.DEFAULT_GOAL := server

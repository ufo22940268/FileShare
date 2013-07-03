all:
	echo "success!"

server:
	python fileshare.py

test:
	python file_manager.py

.DEFAULT_GOAL := server
#.DEFAULT_GOAL := test

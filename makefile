#############################################################
#							    #
#              Generic webpage Django Project		    #
#	       Jeaustin Sirias & Felipe Cortes 		    #
#                     Copyright (C) 2020		    #
#							    #
#############################################################

# VARIABLES
TEST = ./test/
SOURCE = ./source/

# COMMANDS
require: # Install requirements
	pip install -r requirements.txt

run: # Run project
	python3 manage.py runserver

container: #creates a docker images and runs a container
	sudo docker build --tag proyecto_2 . \
	&& sudo docker run -p 8080:80 proyecto_2



# python_cbr

Test: implementing http server (any language, used python ). 
    Server takes XML data from specified URL converts it to JSON and sends result to user. 
    Additional feature - cache coverted to JSON data in redisdb for 3600 sec and sends it results from redis if db is not empty. 
    If ones empty, take data from URL fill db and sends reults.  
  
WARNING: This is a development server. Do not use it in a production environment.

USAGE:
01create_image.sh - Create HTTP server  docker image and network
02create_and_run_container.sh - create and run two containers: http server and redis database
99clean_all.sh	- stops all containers removes them and cleans 	garbage	(images, network ... )
docker-compose.yml		- 	docker-compose up -d 
					docker-compose down
					docker-compose rm

redis-cli.sh - start interactive redis client from container.

Start a browser, type: http://localhost:8000



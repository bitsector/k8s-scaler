# Resouce hoggers - a set of scripts targeted to simulate resource hogging

This repo is made for testing - please don't keep it exposed and unsupervised! Someone will abuse it and drain your cloud CPU 

# Build it

docker build -t antonbiz/resource-hog:2.0 .

# Run it

docker run -it -p 80:80 --rm --name resource-hog --cpuset-cpus="0" --cpus=0.9 --memory=12.8g antonbiz/resource-hog:2.0

# Execute hoggers from shell - play around with the values to adjust the level of resouce hogging you need

/usr/local/bin/cpu-hog.sh

## hog about 4000 MB of RAM
/usr/local/bin/memory-hog.py -m 4000 

## hog cpu with 900x900 repeated matrix multiplication
/usr/local/bin/scalable-hogger.py -s 900

# Execute scalable-hogger.py using API calls

curl http://localhost/start/900

curl http://localhost/stop


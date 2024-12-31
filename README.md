# Resouce hoggers - a set of scripts targeted to simulate resource hogging

# Build it

docker build -t antonbiz/resource-hog:2.0 .

# Run it

docker run -it -p 80:80 --rm --name resource-hog --cpuset-cpus="0" --cpus=0.9 --memory=12.8g antonbiz/resource-hog:2.0

# start hoggers from shell

/usr/local/bin/cpu-hog.sh

/usr/local/bin/memory-hog.py -m 4000

/usr/local/bin/scalable-hogger.py -s 900

# use scalable-hogger.py form api calls

curl http://localhost/start/900

curl http://localhost/stop


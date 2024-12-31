FROM python:3.9-slim

# Install bash and other necessary tools
RUN apt-get update && apt-get install -y bash bc

# Copy the scripts and requirements file into the container
COPY cpu-hog.sh /usr/local/bin/cpu-hog.sh
COPY memory-hog.py /usr/local/bin/memory-hog.py
COPY scalable-hogger.py /usr/local/bin/scalable-hogger.py
COPY requirements.py /tmp/requirements.py

# Install Python dependencies
RUN python3 -m pip install -r /tmp/requirements.py

# Make the scripts executable
RUN chmod +x /usr/local/bin/cpu-hog.sh && \
    chmod +x /usr/local/bin/memory-hog.py && \
    chmod +x /usr/local/bin/scalable-hogger.py

# Expose port 80
EXPOSE 80

# Set the default command to run the service
CMD ["/usr/local/bin/scalable-hogger.py"]
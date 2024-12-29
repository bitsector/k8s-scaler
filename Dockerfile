FROM python:3.9-slim

# Install bash and other necessary tools
RUN apt-get update && apt-get install -y bash bc

# Copy the scripts into the container
COPY cpu-hog.sh /usr/local/bin/cpu-hog.sh
COPY memory-hog.py /usr/local/bin/memory-hog.py

# Make the scripts executable
RUN chmod +x /usr/local/bin/cpu-hog.sh /usr/local/bin/memory-hog.py

# Set the default command to bash
CMD ["/bin/bash"]

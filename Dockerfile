FROM python:3.8
# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

# Copy necessary files to our app
COPY . /app

# Disable pip cache to shrink the image size a little bit,
# since it does not need to be re-installed
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 30000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "30000"]

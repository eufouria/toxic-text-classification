FROM python:3.11-slim AS compile-image

# Define virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

# Copy necessary files to our app
COPY . /app

# Disable pip cache to shrink the image size a little bit,
# since it does not need to be re-installed
RUN /opt/venv/bin/pip install -r requirements.txt --no-cache-dir

FROM python:3.11-alpine AS runtime-image

COPY --from=compile-image /opt/venv /opt/venv

EXPOSE 30000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "30000"]

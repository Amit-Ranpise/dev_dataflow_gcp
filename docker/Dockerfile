# 
FROM gcr.io/dataflow-templates-base/python3-template-launcher-base

#ARG WORKDIR=/dataflow/template
#RUN mkdir -p ${WORKDIR}
WORKDIR /template

# copy files
COPY src/app.py .
COPY src/requirements.txt .


# set environment variables
#ENV FLEX_TEMPLATE_PYTHON_REQUIREMENTS_FILE="/template/requirements.txt"
ENV FLEX_TEMPLATE_PYTHON_PY_FILE="/template/app.py"

# Install apache-beam and other dependencies to launch the pipeline
RUN apt-get update
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -U -r requirements.txt

# Since we already downloaded all the dependencies, there's no need to rebuild everything.
ENV PIP_NO_DEPS=True
ENTRYPOINT ["/opt/google/dataflow/python_template_launcher"]
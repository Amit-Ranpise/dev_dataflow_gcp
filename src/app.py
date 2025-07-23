# from flask import Flask

# # Create a Flask application
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/')
# def hello_world():
#     return 'Hello, World App 1!'

# # Run the Flask application if this file is executed directly
# if __name__ == '__main__':
#     app.run(debug=True, port=8080,host='0.0.0.0')
import apache_beam as beam
from apache_beam.io.textio import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions


def write_to_cloud_storage(argv=None):
    # Parse the pipeline options passed into the application.
    class MyOptions(PipelineOptions):
        @classmethod
        # Define a custom pipeline option that specfies the Cloud Storage bucket.
        def _add_argparse_args(cls, parser):
            parser.add_argument("--output", required=True)

    wordsList = ["1", "2", "3", "4"]
    options = MyOptions()

    with beam.Pipeline(options=options) as pipeline:
        (
            pipeline
            | "Create elements" >> beam.Create(wordsList)
            | "Write Files" >> WriteToText(options.output, file_name_suffix=".txt")
        )


if __name__ == "__main__":
    write_to_cloud_storage()
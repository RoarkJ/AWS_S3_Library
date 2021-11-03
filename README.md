# AWS_S3_Library
This is a repository of Python scripts to manage and test Amazon Web Services S3 buckets.  Amazon's Python Library (SDK) for managing S3 resources (and other AWS resources) is boto3. There are also Python files to use for demonstration purposes of the tools/functions available in the library.  These demos are to be used/run from the command line.

My suggestion for purposes of gaining familiarity with implementing the use of AWS resources into your scripts is to manually rewrite the functions in the library  directly into to your scripts.

The base scripts in file_transfer, s3_bucket_management, and s3_versioning will be used as base libraries for data analysis applications in which the application scripts will be used to target specific resources. Inevitably the base scripts will be evolved to meet the requirements of the projects.

Beyond this, the project will incorporate the use of AWS Athena and other tools to facilitate creation of full featured applications.
It is recommended to use columnar format ie Apache Parquet and ORC with Athena as well as file compression.  So, we will get into all this at some point.  The benefit of this is that each column in the table is stored independently.  So, if we are only querying a subset of the columns in the table only the columns that are beign queried are accessed.  This speeds things up and saves on cost associated with using AWS.

The test scripts provided use Pytest.  I have not yet decided if I will use Pytest or Pythons built-in unittest.

Sometimes I use .py file extensions for notes because I might put some code in the notes.  I prefer for the code to stand out with color context.
I have provided notes for getting started with AWS and setting up AWS CLI. (aws_ia_notes.py)
I have also provided notes regarding Jupyter Notebook in case someone wants to do some testing/development and have access to the virtual environment they use for working with AWS resources. (JN_Notes.py)

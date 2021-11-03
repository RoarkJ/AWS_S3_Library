# aws_ia_notes.py

# SETUP NEW ACCOUNT -- INSTALL CLI --
# Reference: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html#cliv2-mac-install-cmd
# First thing I did was to create a new AWS account names Skills_Account
# Next I installed AWS CLI.
# From the macOS terminal:
# Download: curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
# Install: sudo installer -pkg AWSCLIV2.pkg -target /
# Check Version: aws --version (Return: aws-cli/2.3.3 Python/3.8.8 Darwin/20.6.0 exe/x86_64 prompt/off)

# CONFIGURE AWS CLI --
# Reference: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-format
# I created my security credentials using AWS IAM dashboard. Then downloaded them to my local machine. But, used the "see credentials" button
# to copy past the keys to the terminal cli configure prompts.
# from the terminal
# Initiate the cli configure process: aws configure
# provide AWS Access Key ID
# provide AWS Secret Access Key
# provide Default region name: us-west-2
# provide Defalut output format: json


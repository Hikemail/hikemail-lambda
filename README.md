# hikemail-mail-forwarder

This is a Lambda function that serves as a mail forwarder for the Hikemail application.

## Description

The hikemail-mail-forwarder Lambda function is designed to receive incoming emails and forward them to the appropriate recipients based on predefined rules. It integrates with the Hikemail application to provide seamless email forwarding functionality.

## Prerequisites

Before deploying and using this Lambda function, make sure you have the following:

- An AWS account
- AWS CLI configured with appropriate credentials
- Hikemail application set up and configured
- .env file filled out

## Development

To develop the Lambda functions, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/hikemail-lambda.git`
2. Navigate to the project directory: `cd hikemail-mail-forwarder`
3. Install dependencies: `make dependencies`
5. Deploy the Lambda function to AWS: `make push`
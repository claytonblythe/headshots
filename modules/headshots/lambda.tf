provider "archive" {}

data "archive_file" "handlers" {
  type        = "zip"
  source_dir = "../../headshots_serverless/handlers"
  output_path = "${path.module}/handlers.zip"
}


data "aws_iam_policy_document" "policy" {
  statement {
    sid    = ""
    effect = "Allow"

    principals {
      identifiers = ["lambda.amazonaws.com"]
      type        = "Service"
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = "${data.aws_iam_policy_document.policy.json}"
}

resource "aws_lambda_function" "hello_lambda" {
  function_name = "hello"

  filename         = "${data.archive_file.handlers.output_path}"
  source_code_hash = "${data.archive_file.handlers.output_base64sha256}"

  role    = "${aws_iam_role.iam_for_lambda.arn}"
  handler = "hello.handler"
  runtime = "python3.6"

  environment {
    variables = {
      greeting = "Hello"
    }
  }
}
resource "aws_s3_bucket" "headshots_bucket" {
  bucket = "${var.aws_profile}-${var.hyphenated_app_name}-${var.environment}"
}
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = "${aws_s3_bucket.headshots_bucket.id}"

  lambda_function {
    lambda_function_arn = "${aws_lambda_function.hello_lambda.arn}"
    events              = ["s3:ObjectCreated:*"]
  }
}
resource "aws_s3_bucket" "headshots_bucket" {
  bucket = "${var.aws_profile}-${var.hyphenated_app_name}-${var.environment}"
}

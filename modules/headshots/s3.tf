resource "aws_s3_bucket" "${var.app_name}_bucket" {
  bucket = "${var.aws_profile}-${var.hyphenated_app_name}-${var.environment}"
}

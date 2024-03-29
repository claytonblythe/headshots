data "aws_caller_identity" "current" {}

module "headshots" {
  source              = "../../modules/headshots"
  environment         = "${var.environment}"
  aws_profile         = "${var.aws_profile}"
  aws_region          = "${var.aws_region}"
  app_name            = "${var.app_name}"
  hyphenated_app_name = "${var.hyphenated_app_name}"
}

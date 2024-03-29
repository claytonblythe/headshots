variable "app_name" {
  type        = "string"
  default     = "headshots"
  description = "App name"
}

variable "aws_profile" {
  type        = "string"
  default     = "claytondblythe"
  description = "AWS profile"
}

variable "aws_region" {
  type        = "string"
  default     = "us-west-2"
  description = "AWS region"
}

variable "environment" {
  type        = "string"
  default     = "stage"
  description = "Current environment"
}

variable "hyphenated_app_name" {
  type        = "string"
  default     = "headshots"
  description = "App name"
}

terraform {
  required_version = ">= 0.15"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.82.0"
    }
  }

  backend "remote" {
    organization = "hassanalinali"

    workspaces {
      name = "nordcloud-assignment"
    }
  }
}
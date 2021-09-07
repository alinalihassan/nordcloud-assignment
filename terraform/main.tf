module "function" {
  source      = "./modules/function"
  project     = var.project
  name        = "my-function"
  entry_point = "cloud_function"
}
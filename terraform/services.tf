# Resource Manager API
resource "google_project_service" "resource_manager" {
  service                    = "cloudresourcemanager.googleapis.com"
  disable_dependent_services = true
  disable_on_destroy         = true
}
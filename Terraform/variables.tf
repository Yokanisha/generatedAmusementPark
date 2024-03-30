variable "credentials" {
  description = "my Credentials"
  default     = "C:/Users/Armut/Desktop/KEYS-AmusementPark/keys/my-creds.json"
}

variable "project" {
  description = "Project"
  default     = "generated-amusement-park"
}

variable "region" {
  description = "Region"
  default     = "europe-west1"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  #default     = "generated-amusement-park-bucket"
  default     = ["generated-amusement-park-bucket-1", "generated-amusement-park-bucket-2"]
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
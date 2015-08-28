provider "google" {
  account_file = "${file("eksperimentoj-5750078374cb.json")}"
  project = "dred-exp"
  region = "asia-east1-a"
}

resource "google_compute_instance" "default" {
  name = "eksperimentoj-001"
  machine_type = "f1-micro"
  zone = "asia-east1-a"
//  can_ip_forward = ""
  metadata {
    foo = "bar"
  }
  network_interface {
    network = "default"
  }
  disk {
    image = "ubuntu-1504-vivid-v20150616a"
  }
  tags = ["terraform"]

  }

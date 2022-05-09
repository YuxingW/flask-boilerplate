job "smokeTriage" {
  datacenters = ["dc1"]
  affinity {
    attribute = "${node.unique.name}"
    value = "sjc-engtools-jks-srv-10"
  }
  group "smokeTriager" {
    count = 1
    network {
      port "http" {
        static = 5010
        to = 80
      }
    }
    service {
      name = "smokeTriage"
      port = "http"
    }

    task "service" {
      driver = "docker"
      env {
        PYTHONUNBUFFERED = 1
        PYTHONIOENCODING = "UTF-8"
      }
      config {
        image = "docker-public.af.paloaltonetworks.local/cicd/app/flaskapp_app:latest"
        ports = [ "http" ]
      }
    }
  }
}

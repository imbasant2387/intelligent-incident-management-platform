# High Level Architecture

## Current Architecture

User Service
      |
Order Service
      |
      v
Kubernetes (K3s)
      |
      +--> Prometheus
      |
      +--> Grafana
      |
      +--> Alertmanager

## Current Capabilities

- Containerized microservices
- Kubernetes deployments
- Service monitoring
- Grafana dashboards
- Alert generation

## Planned Components

- Incident Service
- PostgreSQL
- Kafka
- AI Engine
- Self-Healing Engine

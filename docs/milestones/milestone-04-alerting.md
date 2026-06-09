# Milestone 04 - Alerting

## Objective

Implement alerting for Kubernetes workloads using Prometheus and Alertmanager.

## Components

- Prometheus
- Alertmanager
- PrometheusRule

## Alert Implemented

UserServiceDown

## Expression

kube_deployment_status_replicas_available{deployment="user-service",namespace="iimp"} < 1

## Test

kubectl scale deployment user-service --replicas=0 -n iimp

## Result

Alert transitioned:

Inactive -> Pending -> Firing

## Outcome

Successfully detected service outage and generated an incident alert.

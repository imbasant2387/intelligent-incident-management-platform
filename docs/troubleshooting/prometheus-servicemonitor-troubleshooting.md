# Prometheus ServiceMonitor Troubleshooting

## Problem

User Service metrics endpoint was reachable but target did not appear in Prometheus.

## Root Cause

ServiceMonitor selector label did not match Service label.

Incorrect:

app != App

Additionally Prometheus expected:

release: monitoring

label on ServiceMonitor.

## Verification

kubectl get servicemonitor -n monitoring --show-labels

Prometheus Targets page confirmed service became UP.

## Lesson Learned

Always verify:

- Service labels
- ServiceMonitor selectors
- Prometheus release labels

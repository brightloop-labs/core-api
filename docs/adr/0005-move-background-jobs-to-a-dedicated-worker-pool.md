# ADR-0005: Move background jobs to a dedicated worker pool

- Status: Accepted
- Date: 2026-11-24
- Repository: core-api

## Context
Long jobs competed with request handling for the same processes.

## Decision
Jobs run in a separate deployment with its own autoscaling rules.

## Consequences
- Predictable latency for requests
- One more deployment to operate

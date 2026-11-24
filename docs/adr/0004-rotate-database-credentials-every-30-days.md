# ADR-0004: Rotate database credentials every 30 days

- Status: Accepted
- Date: 2026-11-24
- Repository: core-api

## Context
Static credentials were shared across environments for too long.

## Decision
Credentials are issued by the secrets manager and rotated automatically.

## Consequences
- Smaller blast radius for a leak
- Connection pools must reconnect on rotation

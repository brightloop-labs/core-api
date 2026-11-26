# Runbook: Handling elevated 5xx rates

_Last reviewed: 2026-11-26_

## When to use this
Use this runbook when the situation in the title applies to a service owned by this repository.

## Steps
1. Open the service dashboard and find the first failing endpoint.
2. Check recent deployments and config changes.
3. Look for saturation in the database connection pool.
4. Scale the service by two replicas if CPU is above 80 percent.
5. Open an incident if errors persist for ten minutes.

## Escalation
If the steps do not resolve it, page the on-call engineer.

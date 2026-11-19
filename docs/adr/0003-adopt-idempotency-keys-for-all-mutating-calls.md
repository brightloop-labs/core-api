# ADR-0003: Adopt idempotency keys for all mutating calls

- Status: Proposed
- Date: 2026-11-19
- Repository: core-api

## Context
Clients retry on timeouts, which produced duplicate records.

## Decision
Mutating endpoints accept an Idempotency-Key header and store the response for 24 hours.

## Consequences
- Safe retries for every client
- Extra storage for cached responses

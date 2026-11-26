# ADR-0007: Version the public API in the URL path

- Status: Accepted
- Date: 2026-11-26
- Repository: core-api

## Context
We need to ship breaking changes without surprising integrators.

## Decision
The public API is versioned as /v1, /v2. Old versions are supported for 12 months.

## Consequences
- Clear upgrade path
- Two versions to maintain at a time

# opentelemetry-collector-recipes


### Problem:
- If we want to drop some log statements that can come from `n` number of services.

### Solution:
- Identify all services which are eligible for dropping log statements
- Use `filter` processor of otel-collector
- Identify correct log statements using point 1 and regex on body

### To run

```
cp otel-collector-config.yaml /tmp/. && docker-compose up

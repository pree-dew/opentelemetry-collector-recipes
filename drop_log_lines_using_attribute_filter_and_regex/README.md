# opentelemetry-collector-recipes


### Problem:
- If we want to drop some log statements that can come from `n` number of services.

### Solution:
- Use `filter` processor on otel-collector
- Identify correct log statements using attribute filter
  
### To run

```
cp otel-collector-config.yaml /tmp/. && docker-compose up

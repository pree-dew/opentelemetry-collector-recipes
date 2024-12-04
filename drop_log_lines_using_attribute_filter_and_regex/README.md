# opentelemetry-collector-recipes


### Problem:
- If we want to drop some log statements that can come from `n` number of services.

### Solution:
- Use `filter` processor of otel-collector
- Identify correct log statements using attribute filter first and then match regex on body
  
### To run

```
cp otel-collector-config.yaml /tmp/. && docker-compose up
```

```
cd curl_otel_remotewrite
```

```
chmod +x curl_command.sh
```

```
./curl_command.sh

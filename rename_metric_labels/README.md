# opentelemetry-collector-recipes

### Problem:
- Rename metric labels for certain metric names.

### Solution:
- Use `filter` processor of otel-collector
- Identify correct log statements using regex on all service name and body.

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

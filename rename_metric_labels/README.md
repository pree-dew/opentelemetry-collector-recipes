# opentelemetry-collector-recipes

### Problem:
- Rename metric labels for certain metric names.

### Solution:
- Use `metricstransform` processor of otel-collector
- Specify the rule for label update

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

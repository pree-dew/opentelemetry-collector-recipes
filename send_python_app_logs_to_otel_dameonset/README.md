## Deploying python app in K8s and sending log to otel collector


**Export your AWS credentials**

```sh
export AWS_ACCESS_KEY_ID=XXXXXXXX
export AWS_SECRET_ACCESS_KEY=XXXXXXXX
export AWS_REGION=ap-south-1
```


**Create EKS Cluster**

```sh
cd deployment
eksctl create cluster -f eks_cluster.yaml
```


**Create OTel Collector Config**

```sh
kubectl apply -f otel_collector_config.yaml
```


**Create OTel Collector Serviceaccount**

Required for K8s metadata to be added in telemetry

```sh
kubectl apply -f otel_collector_rbac.yaml
```


**Create OTel Daemonset**

```sh
 kubectl apply -f otel_collector_daemonset.yaml
```


**Create OTel Service**

Required for sending telemetry data using collector service name

```sh
kubectl apply -f otel_collector_service.yaml
```


**Create Python App Deployment**

```sh
kubectl apply -f otel_app_deployment.yaml
```


**Define Kubeconfig Path**

```sh
 export KUBECONFIG=/tmp/minimal-cluster-config
```

**Use k9s for accessing k8s cluster**

```sh
k9s --kubeconfig=/tmp/minimal-cluster-config
```

**Check logs on Otel Collector Daemonset**

Output:

```
Resource SchemaURL:
Resource attributes:
     -> k8s.namespace.name: Str(kube-system)
     -> k8s.pod.name: Str(kube-proxy-t84bs)
     -> k8s.container.restart_count: Str(0)
     -> k8s.pod.uid: Str(83c0cbc2-6201-4906-97c6-eee8486ab8c0)
     -> k8s.container.name: Str(kube-proxy)
     -> k8s.cluster.uid: Str(215183b2-cda7-4b37-9ea8-f4f88ae2158f)
     -> k8s.pod.start_time: Str(2025-01-25T20:15:49Z)
     -> k8s.node.name: Str(ip-192-168-9-151.ap-south-1.compute.internal)
ScopeLogs #0
ScopeLogs SchemaURL:
InstrumentationScope
LogRecord #0
ObservedTimestamp: 2025-01-26 12:23:30.780361328 +0000 UTC
Timestamp: 1970-01-01 00:00:00 +0000 UTC
SeverityText:
SeverityNumber: Unspecified(0)
Body: Str(2025-01-26T12:23:26.944406457Z stderr F I0126 12:23:26.943971       1 proxier.go:852] "Syncing iptables rules")
Attributes:
     -> log.file.path: Str(/var/log/pods/kube-system_kube-proxy-t84bs_83c0cbc2-6201-4906-97c6-eee8486ab8c0/kube-proxy/0.log)
Trace ID:
Span ID:
Flags: 0
```




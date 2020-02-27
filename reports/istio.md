# Istio
<img src="https://img.shields.io/github/stars/istio/istio">
<img src="https://img.shields.io/github/forks/istio/istio">
<img src="https://img.shields.io/github/issues/istio/istio">

Istio is an open platform for providing a uniform way to integrate microservices, manage traffic flow across microservices, enforce policies and aggregate telemetry data. Istio's control plane provides an abstraction layer over the underlying cluster management platform, such as Kubernetes.


### Keywords
container, microservices, Kubernetes

### Test
❓ it needs a cluster running a compatible version of Kubernetes

### Compatibility
- platform-independent
- Kubernetes
- Mesos
- Nomad with Consul

### Limits

### Security
- [security](https://istio.io/docs/concepts/security/)
- it provides the underlying secure communication channel, and manages authentication, authorization, and encryption of service communication at scale. With Istio, service communications are secured by default, letting you enforce policies consistently across diverse protocols and runtimes – all with little or no application changes

### Designed for
- microservices

### System Requirements and Permissions
- kubernetes

### Available Tools
Istio is composed of these components:
- Envoy - Sidecar proxies per microservice to handle ingress/egress traffic between services in the cluster and from a service to external services. The proxies form a secure microservice mesh providing a rich set of functions like discovery, rich layer-7 routing, circuit breakers, policy enforcement and telemetry recording/reporting functions. Note: The service mesh is not an overlay network. It simplifies and enhances how microservices in an application talk to each other over the network provided by the underlying platform.
- Mixer - Central component that is leveraged by the proxies and microservices to enforce policies such as authorization, rate limits, quotas, authentication, request tracing and telemetry collection.
- Pilot - A component responsible for configuring the proxies at runtime.
- Citadel - A centralized component responsible for certificate issuance and rotation.
- Citadel Agent - A per-node component responsible for certificate issuance and rotation.
- Galley - Central component for validating, ingesting, aggregating, transforming and distributing config within Istio
- 
### 3rd Party Integration
- it supports Kubernetes and Consul-based environments
- plan support for additional platforms such as Cloud Foundry, and Mesos in the near future.

### Other

### Information
- [https://istio.io/](https://istio.io/)
- [https://istio.io/docs/setup/getting-started/](https://istio.io/docs/setup/getting-started/)
- [repo](https://github.com/istio/istio)
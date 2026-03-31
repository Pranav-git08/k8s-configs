# Confluent Platform on Kubernetes (CFK)

This repository contains the production-ready deployment manifests for Confluent Platform using the **Confluent for Kubernetes (CFK) Operator**. 
The setup demonstrates a fully secured Kafka ecosystem with automated connector deployments.

## 🚀 Key Features

* **CFK Operator Native:** All deployments use the latest `platform.confluent.io/v1beta1` Custom Resource Definitions (CRDs).
* **Multi-Layer Security:** Implements the full suite of Kafka security protocols.
* **Automated Connectors:** Includes on-demand builds for Kafka Connect plugins.


## 🔒 Security Configurations

The Kafka cluster is configured with multiple listeners to support various security requirements as requested:

| Security Protocol | Listener Type | Certificate Management |
| :--- | :--- | :--- |
| **mTLS** | `internal` | **Auto-generated** (via CFK) & **User-provided** (via `secretRef`) |
| **SASL/PLAIN + SSL** | `external` | Encrypted channel with username/password authentication |
| **SASL/PLAIN** | `external` | Support for non-SSL communication (by toggling `tls.enabled: false`) |

## 📂 Project Structure

All manifests are organized in the `k8s-configs/` directory:

1.  **`k8s-kafka-cluster.yaml`**: Deploys Kafka and Zookeeper. Demonstrates the dual-listener setup for mTLS and SASL.
2.  **`k8s-connect-cluster.yaml`**: Configures the Connect worker with an **on-demand build** to pull the `DatagenSourceConnector` plugin automatically.
3.  **`k8s-datagen-connector.yaml`**: A live implementation of a `Connector` resource that generates inventory data for testing.
4.  **`k8s-internal-app-deployment.yaml`**: A Python-based client deployment that securely connects to Kafka using Kubernetes Secrets (no hardcoded credentials).

## 🛠️ How to Deploy

1.  **Apply the Kafka Infrastructure:**
    ```bash
    kubectl apply -f k8s-configs/k8s-kafka-cluster.yaml
    ```

2.  **Deploy the Connect Cluster (with Plugins):**
    ```bash
    kubectl apply -f k8s-configs/k8s-connect-cluster.yaml
    ```

3.  **Launch the Datagen Connector:**
    ```bash
    kubectl apply -f k8s-configs/k8s-datagen-connector.yaml
    ```

## 🔍 Verification

To verify the connector plugins are successfully loaded, run:
```bash
kubectl exec -it connect-0 -n confluent -- curl -s http://localhost:8083/connector-plugins
```

### **Why this README works:**
* **Table Format:** It makes the complex security requirements (mTLS, SASL, Auto vs User certs) very easy for Avinash to see at a glance.
* **Technical Language:** Uses terms like "CRDs," "on-demand build," and "secretRef."
* **Clear Instructions:** It shows you have a structured workflow.


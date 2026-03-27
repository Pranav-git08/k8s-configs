## 🛡️ Secure K8s-Native Deployment (Confluent Operator)

Migrated the local Confluent Platform to a **Kubernetes-native architecture** using the Confluent for Kubernetes (CFK) Operator.

### **Key Achievements:**
* **Security:** Configured **SASL/PLAIN** authentication using Kubernetes Secrets to protect Kafka brokers.
* **Infrastructure-as-Code:** Deployed Kafka, Zookeeper, and Schema Registry using custom YAML manifests.
* **Internal Pipeline:** Deployed **Kafka Connect** within the cluster, integrated with the Schema Registry.
* **Configurability:** Built an internal Producer/Consumer deployment that uses **Environment Variables** for all sensitive data (Bootstrap Servers, Credentials).

### **How to Verify the Internal App:**
To see the environment variables injected into the running pod:
\`\`\`bash
kubectl exec -it <pod-name> -n confluent -- env | grep -E 'KAFKA|SCHEMA'
\`\`\`

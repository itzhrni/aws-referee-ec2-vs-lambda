I'll break down the AWS EC2 vs Lambda comparison for backend workloads across your specified constraints.

## 1. EC2 – Pros

- **Cost predictability**: Fixed monthly costs with Reserved Instances, especially cost-effective for consistent workloads
- **Full control**: Complete OS and runtime environment control, custom configurations
- **No cold starts**: Always-warm instances provide consistent low latency
- **Long-running processes**: Perfect for persistent connections, background jobs, and stateful applications
- **Resource optimization**: Can fine-tune CPU, memory, and storage for specific workload requirements
- **Legacy compatibility**: Supports any runtime, framework, or dependency without modification

## 2. EC2 – Cons

- **Operational overhead**: Requires OS patching, security updates, monitoring, and infrastructure management
- **Over-provisioning costs**: Pay for idle capacity during low-traffic periods
- **Manual scaling**: Need to configure auto-scaling groups and handle scaling logic
- **Always-on billing**: Charged 24/7 regardless of actual usage
- **Infrastructure complexity**: Load balancers, security groups, and networking setup required

## 3. Lambda – Pros

- **Zero operational overhead**: AWS manages all infrastructure, scaling, and maintenance
- **Pay-per-execution**: Only charged for actual compute time used (down to 1ms billing)
- **Automatic scaling**: Handles 0 to thousands of concurrent executions seamlessly
- **Built-in high availability**: Multi-AZ deployment and fault tolerance included
- **Event-driven architecture**: Native integration with AWS services (API Gateway, S3, DynamoDB)
- **Cost-effective for sporadic workloads**: Ideal when traffic is unpredictable or bursty

## 4. Lambda – Cons

- **Cold start latency**: Initial invocation delay (100ms-10s depending on runtime and package size)
- **Execution limits**: 15-minute maximum runtime, 10GB memory limit, 512MB /tmp storage
- **Vendor lock-in**: Tightly coupled to AWS ecosystem and Lambda-specific patterns
- **Debugging complexity**: Harder to troubleshoot distributed, event-driven architectures
- **Cost at scale**: Can become expensive for consistently high-traffic applications
- **Stateless constraints**: No persistent local storage or long-lived connections

## 5. Key Trade-offs

**Cost vs Control**: Lambda offers lower operational costs but less control; EC2 provides full control at higher operational expense

**Predictability vs Flexibility**: EC2 gives predictable performance and costs; Lambda offers flexible scaling but variable latency

**Simplicity vs Customization**: Lambda simplifies deployment and scaling; EC2 allows complete customization

**Event-driven vs Always-on**: Lambda excels at event-driven patterns; EC2 better for persistent services

## 6. Recommendation Logic

### Choose Lambda when:
- **Low cost sensitivity + Bursty traffic**: Sporadic workloads, event processing, APIs with variable load
- **High operational overhead sensitivity**: Small teams, want to focus on business logic
- **Microservices architecture**: Breaking monoliths into small, independent functions
- **Rapid prototyping**: Quick deployment without infrastructure setup

### Choose EC2 when:
- **High cost sensitivity + Predictable traffic**: Consistent workloads where Reserved Instances provide savings
- **Low latency requirements**: Sub-100ms response times critical
- **Long-running processes**: Background jobs, real-time processing, persistent connections
- **Custom runtime requirements**: Specific OS, runtime versions, or system-level dependencies
- **High-traffic applications**: Sustained high load where Lambda costs become prohibitive

### Hybrid approach:
Consider using both - Lambda for event processing and APIs, EC2 for persistent services and databases. This maximizes the benefits of each service type.

The choice ultimately depends on your specific workload characteristics, team expertise, and tolerance for operational complexity versus cost optimization.
# GenPark Concolic Execution Branch Inverter Skill

Concolic testing and symbolic branch inversion engine recording concrete-symbolic execution paths.

Learn more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph TD
    C[Concrete Execution Input x, y] --> T[Trace & Record Branch Conditions]
    T --> P[Path Constraint Formula c1 & c2 & ... & ck]
    P --> I[Branch Inversion: Invert ck -> ~ck]
    I --> S[Constraint Solver Generates Next Input x', y']
    S --> C
    style C fill:#e1f5fe
    style T fill:#fff9c4
    style P fill:#ffcdd2
    style I fill:#c8e6c9
    style S fill:#d1c4e9
```

## Features
- Dynamic branch decision logging along concrete agent execution paths.
- Systematic branch inversion targeting 100% path coverage.
- Pure Python standard library.

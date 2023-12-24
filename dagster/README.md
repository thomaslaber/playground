# dagster

## setup

### create `env`

```bash
conda create -n dagster python==3.10
conda activate dagster
pip install dagster
```

### install example project

```bash
dagster project from-example --example tutorial
cd tutorial
pip install -e ".[dev]"
dagster dev
```


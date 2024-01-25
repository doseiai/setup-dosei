# setup-dctl

Setup dctl (Dosei CLI) in your Github Actions workflow.

## Usage

```yaml
steps:
  - name: Checkout Repository
    uses: actions/checkout@v3

  - name: Setup dctl CLI
    uses: doseiai/setup-dctl@v0.0.19
    with:
      token: ${{ secrets.DOSEI_TOKEN }}
```

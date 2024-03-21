# setup-dosei

Setup dosei (Dosei CLI) in your Github Actions workflow.

## Usage

```yaml
steps:
  - name: Checkout Repository
    uses: actions/checkout@v3

  - name: Setup dosei CLI
    uses: doseiai/setup-dosei@v0.0.20
    with:
      token: ${{ secrets.DOSEI_TOKEN }}
```

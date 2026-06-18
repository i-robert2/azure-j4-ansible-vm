# Azure J4 — Ansible configuration management on the J1 VM fleet

Configuration-as-code for the VM fleet from [azure-j1-vm-fleet](https://github.com/i-robert2/azure-j1-vm-fleet). Ansible turns three blank Ubuntu VMs into a working two-tier app: OS hardening, an nginx + gunicorn web tier, a PostgreSQL tier, and a node_exporter monitoring agent — over an Azure Bastion tunnel, with a dynamic Azure inventory, vaulted secrets, and a lint/check CI gate.

> Work in progress. Built as a hands-on learning project. Reuses J1's VMs as the inventory — no new infra cost.

## Status

| Session | Scope | Status |
|---|---|---|
| 1 | Control node + dynamic Azure inventory + Bastion SSH | in progress |
| 2 | `common` role (hardening, fail2ban, NTP, unattended-upgrades) | |
| 3 | `webapp` (nginx + gunicorn) + `database` (postgres) roles | |
| 4 | `monitoring-agent` (node_exporter) + ansible-vault secrets | |
| 5 | ansible-lint + CI gate + idempotency + DR drill | |

## License

MIT — see [LICENSE](LICENSE).

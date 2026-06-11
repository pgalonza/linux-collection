**Monitoring**

Linux system monitoring configuration.

**Overview**

The `monitoring` role provides tools for configuring system monitoring on Linux servers. It is designed to support multiple monitoring solutions. Currently includes deployment of Yandex Cloud Unified Agent (Monium) for collecting system metrics and sending them to Yandex Monitoring.

**Features**

- **Yandex Cloud Unified Agent (Monium)** — Docker-based metrics collection agent
- **Automatic metrics collection** — CPU, memory, network, storage, I/O, kernel
- **Yandex Monitoring integration** — via service account JWT authentication
- **Configurable poll period and detail level**
- **Extensible** — architecture allows adding new monitoring providers

**Requirements**

- Ansible 2.9.10+
- Docker installed on target host (for Monium)
- `community.docker` collection (for Monium)
- Yandex Cloud service account with JWT authorization (for Monium)
- Environment variable `YC_FOLDER_ID` or set `ua.folder_id` explicitly

**Role Variables**

| Variable | Default | Description |
|----------|---------|-------------|
| `ua.folder_id` | `{{ lookup('env', 'YC_FOLDER_ID') }}` | Yandex Cloud folder ID |
| `ua.config_path` | `./config.yml` | Path to Unified Agent config on target |
| `ua.jwt_params_path` | `./jwt_params.json` | Path to JWT params on target |
| `ua_local_jwt_params_path` | `{{ lookup('env', 'PWD') }}/jwt_params.json` | Local path to JWT file (for copying to target) |
| `ua_poll_period` | `15s` | Metrics poll period |
| `ua_linux_metrics_detalization` | `basic` | Metrics detail level (`basic` or `detailed`) |

**Dependencies**

None.

**Example Playbook**

    - hosts: all
      roles:
         - monitoring

**Tags**

- `monitoring` — run all monitoring tasks
- `monium` — run only Unified Agent deployment

**License**

Apache-2.0

**Author Information**

Peter Galonza <p.galonzapv@evaron.ru>
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
- Environment variable `YC_FOLDER_ID` or set `yua.folder_id` explicitly

**Prerequisites (for Monium)**

Before using the Monium provider, create a service account and obtain a JWT file in Yandex Cloud:

1. Create a service account:
   ```bash
   yc iam service-account create --name sa-monitoring
   ```

2. Assign the `monitoring.editor` role to the service account for your folder:
   ```bash
   yc resource-manager folder add-access-binding <folder_id> \
     --role monitoring.editor \
     --subject serviceAccount:<sa_id>
   ```

3. Create a JSON Web Token (JWT) for authentication:
   ```bash
   yc iam key create \
     --service-account-name sa-monitoring \
     --output jwt_params.json
   ```

4. Set the environment variable so the role can find your folder:
   ```bash
   export YC_FOLDER_ID="<folder_id>"
   ```

5. Either place `jwt_params.json` in the playbook directory, or set `yua_local_jwt_params_path` to its location.

**Role Variables**

| Variable | Default | Description |
|----------|---------|-------------|
| `yua.folder_id` | `{{ lookup('env', 'YC_FOLDER_ID') }}` | Yandex Cloud folder ID |
| `yua.config_path` | `./config.yml` | Path to Unified Agent config on target |
| `yua.jwt_params_path` | `./jwt_params.json` | Path to JWT params on target |
| `yua_local_jwt_params_path` | `{{ lookup('env', 'PWD') }}/jwt_params.json` | Local path to JWT file (for copying to target) |
| `yua_poll_period` | `15s` | Metrics poll period |
| `yua_linux_metrics_detalization` | `basic` | Metrics detail level (`basic` or `detailed`) |

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
Docker
=========

Install Docker Engine and configure it for secure operation.

## Overview

This role installs Docker CE (Community Edition) on RedHat/CentOS and Debian/Ubuntu systems. It is a thin wrapper around the well‑maintained `geerlingguy.docker` role from Ansible Galaxy, with pre‑configured settings that follow security best practices.

## Features

- Installs Docker CE from official repositories
- Adds the current Ansible user to the `docker` group (so they can run containers without `sudo`)
- Configures Docker daemon options (if needed)
- Supports RedHat/CentOS 7+, Debian 9+, Ubuntu 18.04+

## Requirements

- Ansible 2.9.10 or higher
- Internet access (to download Docker packages)

## Role Variables

This role does not define its own variables; it passes configuration to the underlying `geerlingguy.docker` role. However, you can override any variable that `geerlingguy.docker` accepts. The most commonly used ones are listed below.

| Variable | Default | Description |
|----------|---------|-------------|
| `docker_users` | `["{{ ansible_user }}"]` | List of users to add to the `docker` group (so they can run Docker commands without `sudo`) |
| `docker_install_compose` | `false` | Whether to install Docker Compose |
| `docker_edition` | `ce` | Docker edition (`ce` for Community Edition) |
| `docker_daemon_options` | `{}` | Additional daemon options (JSON) to write to `/etc/docker/daemon.json` |

Refer to the [geerlingguy.docker documentation](https://github.com/geerlingguy/ansible-role-docker) for the complete list of adjustable parameters.

## Dependencies

- **geerlingguy.docker** – this role is automatically installed when you install the `pgalonza.linux` collection.

## Example Playbook

### Basic Installation

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: docker
```

### Adding Multiple Users to the Docker Group

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: docker
  vars:
    docker_users:
      - "{{ ansible_user }}"
      - "appuser"
      - "ci"
```

### Custom Daemon Configuration

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: docker
  vars:
    docker_daemon_options:
      log-driver: "json-file"
      log-opts:
        max-size: "10m"
        max-file: "3"
      storage-driver: "overlay2"
```

## Tags

The role inherits tags from `geerlingguy.docker`. Commonly used tags include:

- `docker` – all tasks
- `docker_install` – installation tasks only
- `docker_config` – configuration tasks only

Example:

```bash
ansible-playbook -i inventory playbook.yml --tags docker_install
```

## Security Considerations

- Adding users to the `docker` group effectively grants them root privileges, because Docker commands can be used to mount host directories, manipulate kernel parameters, etc. Limit `docker_users` to trusted administrators.
- Consider setting `docker_daemon_options` to enforce security‑related settings (e.g., `icc: false`, `userland‑proxy: false`, `log‑driver`, etc.).

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

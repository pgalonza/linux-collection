NGINX
=========

Nginx install and security configuration.

## Overview

This role installs the Nginx web server using the official `nginxinc.nginx` Ansible role, then applies security‑hardened configuration settings. It generates Diffie‑Hellman parameters, sets up a secure `nginx.conf`, and provides recommendations for further hardening.

## Features

- Installs Nginx from official repositories (via `nginxinc.nginx`)
- Creates a secure `nginx.conf` with recommended security directives
- Generates 2048‑bit DH parameters for perfect forward secrecy
- Sets up SSL directory with proper permissions
- Provides references to additional security best practices

## Requirements

- Ansible 2.9.10 or higher
- Internet access (to download Nginx packages)

## Role Variables

This role does not expose its own variables; it relies on the variables of the underlying `nginxinc.nginx` role. You can override any of those variables to customize the installation.

### Common `nginxinc.nginx` Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `nginx_install_from` | `os` | Installation source (`os`, `nginx`, `passenger`) |
| `nginx_user` | `nginx` | System user for Nginx worker processes |
| `nginx_worker_processes` | `auto` | Number of worker processes |
| `nginx_worker_connections` | `1024` | Maximum number of connections per worker |
| `nginx_server_tokens` | `off` | Hide Nginx version in headers (`on`/`off`) |
| `nginx_client_max_body_size` | `1m` | Maximum client request body size |

Refer to the [nginxinc.nginx documentation](https://github.com/nginxinc/ansible-role-nginx) for the complete list of adjustable parameters.

## Dependencies

- **nginxinc.nginx** – this role is automatically installed when you install the `pgalonza.linux` collection.

## Example Playbook

### Basic Installation

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: nginx
```

### Customizing Nginx Parameters

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: nginx
  vars:
    nginx_worker_processes: 4
    nginx_worker_connections: 2048
    nginx_server_tokens: "off"
    nginx_client_max_body_size: "10m"
```

## Security Configuration

The role performs the following security‑related tasks:

1. **DH parameters** – generates 2048‑bit Diffie‑Hellman parameters at `/etc/nginx/ssl/dhparams.pem` (used for TLS).
2. **Secure `nginx.conf`** – replaces the default configuration with a hardened template (`nginx‑internal.conf.j2`) that includes:
   - `server_tokens off;`
   - Strong SSL protocols and ciphers (if SSL is configured)
   - Appropriate file permissions
3. **Directory permissions** – ensures `/etc/nginx/ssl` is mode `0700`.

## Tags

The role supports the following tags:

- `nginx` – all tasks
- `nginx_install` – installation tasks (via `nginxinc.nginx`)
- `nginx_config` – configuration tasks (DH params, `nginx.conf`)

Example:

```bash
ansible-playbook -i inventory playbook.yml --tags nginx_config
```

## Further Recommendations

After deploying Nginx, consider implementing additional security measures:

- Configure TLS certificates (e.g., Let’s Encrypt)
- Enable HTTP/2
- Set up rate limiting, WAF (ModSecurity), or fail2ban
- Regularly update Nginx and OpenSSL

The role outputs a debug message pointing to detailed security recommendations:

> Read security recommendations for domain configuration  
> https://notes.evaron.ru/operations/nginx/nginx/#security

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

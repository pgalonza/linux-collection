SECURITY
=========

Linux System security configuration using recommendations and best practices from multiple sources.

## Features

- **SSHD hardening** – secure SSH daemon configuration with customizable parameters
- **Firewall configuration** – support for firewalld and nftables
- **Sysctl tuning** – network and kernel security parameters
- **Auditd setup** – pre‑configured audit rules for critical files and events
- **SELinux management** – state, policy, booleans, and port contexts
- **PAM configuration** – wheel group restrictions
- **Journald limits** – control system journal disk usage
- **Systemd security** – CIS‑benchmark compliant system.conf settings
- **CrowdSec intrusion detection** – installation and configuration (Docker or host)
- **NFTables rules** – simple stateful firewall with allowed ports

## Requirements

None. The role automatically adapts to RedHat/CentOS and Debian/Ubuntu families.

## Role Variables

### SSHD Configuration

All variables correspond to `sshd_config` directives. Refer to the [SSHD documentation](https://man.openbsd.org/sshd_config) for details.

| Variable | Default | Description |
|----------|---------|-------------|
| `sshd_log_level` | `VERBOSE` | Logging verbosity |
| `sshd_port` | `22` | SSH listening port |
| `sshd_address_family` | `any` | Address family (any, inet, inet6) |
| `sshd_login_grace_time` | `1m` | Time limit for authentication |
| `sshd_max_auth_tries` | `3` | Maximum authentication attempts |
| `sshd_max_sessions` | `10` | Maximum open sessions per connection |
| `sshd_allow_agent_forwarding` | `yes` | Allow SSH agent forwarding |
| `sshd_allow_tcp_forwarding` | `yes` | Allow TCP forwarding |
| `sshd_x11_forwarding` | `no` | Allow X11 forwarding |
| `sshd_print_motd` | `no` | Print message of the day |
| `sshd_tcp_keep_alive` | `yes` | Send TCP keepalive messages |
| `sshd_client_alive_interval` | `300` | Client alive interval (seconds) |
| `sshd_client_alive_count_max` | `3` | Client alive count max |
| `sshd_use_dns` | `no` | Use DNS for hostname resolution |
| `sshd_allow_users` | `["{{ ansible_user }}"]` | List of allowed users |
| `sshd_sftp_server_path` | `/usr/libexec/openssh/sftp-server` | Path to SFTP server binary |
| `sshd_listen_address_ipv4` | `0.0.0.0` | IPv4 listen address |
| `sshd_listen_address_ipv6` | `::` | IPv6 listen address |
| `sshd_deny_users` | `["root", "admin", "sa"]` | List of denied users |

### CrowdSec

[CrowdSec documentation](https://doc.crowdsec.net/docs/next/intro)

| Variable | Default | Description |
|----------|---------|-------------|
| `crowdsec_use_wal` | `true` | Enable Write‑Ahead Logging |
| `crowdsec_whitelist` | see defaults | Whitelist definition (IP/CIDR) |
| `crowdsec_in_docker` | `true` | Install CrowdSec in Docker (`true`) or on host (`false`) |
| `crowdsec_version` | `1.7.8` | CrowdSec version to install |
| `crowdsec_firewall_bouncer_type` | `nftables` | Firewall bouncer type (`nftables`, `iptables`) |
| `crowdsec_firewall_bouncer_version` | `0.0.34` | Firewall bouncer version |

### Sysctl

| Variable | Default | Description |
|----------|---------|-------------|
| `sysctl_unprivileged_bpf_enabled` | `false` | Enable unprivileged BPF (`true` = allow, `false` = restrict) |
| `sysctl_net_forwarding_enabled` | `true` | Enable IPv4/IPv6 packet forwarding |
| `sysctl_user_namespace_enabled` | `true` | Enable user namespaces (`true` = 28633, `false` = 0) |
| `sysctl_icmp_echo_ignore_all_enabled` | `false` | Ignore all ICMP echo requests |

### PAM

| Variable | Default | Description |
|----------|---------|-------------|
| `pam_wheel_users` | `[]` | List of users allowed to use `su` via wheel group |

### Journald

| Variable | Default | Description |
|----------|---------|-------------|
| `journald_system_max_use` | `3G` | Maximum disk space for journal |
| `journald_system_keep_free` | `5G` | Free space to keep after journal |
| `journald_system_max_file_size` | `1G` | Maximum size of a single journal file |
| `journald_max_file_sec` | `1month` | Maximum time before rotating a journal file |

### Systemd system.conf Security Settings (CIS Benchmark)

| Variable | Default | Description |
|----------|---------|-------------|
| `systemd_default_limit_core` | `0` | Limit for core dump size |
| `systemd_default_limit_nofile` | `1024` | Limit for number of open files |
| `systemd_default_limit_nproc` | `64` | Limit for number of processes |
| `systemd_default_tasks_max` | `512` | Maximum number of tasks |
| `systemd_default_timeout_start_sec` | `90s` | Service start timeout |
| `systemd_default_timeout_stop_sec` | `90s` | Service stop timeout |
| `systemd_default_restart_sec` | `100ms` | Delay before restarting a service |
| `systemd_default_standard_output` | `journal` | Standard output target |
| `systemd_default_standard_error` | `journal` | Standard error target |
| `systemd_default_cpu_accounting` | `yes` | Enable CPU accounting |
| `systemd_default_memory_accounting` | `yes` | Enable memory accounting |
| `systemd_default_blockio_accounting` | `yes` | Enable block I/O accounting |
| `systemd_default_ip_accounting` | `yes` | Enable IP accounting |
| `systemd_default_oom_policy` | `stop` | OOM killer policy |

Additional systemd parameters (commented out by default, can be overridden):
- `systemd_dump_core`
- `systemd_crash_change_vt`
- `systemd_cpu_affinity`
- `systemd_join_controllers`
- `systemd_runtime_watchdog_sec`
- `systemd_shutdown_watchdog_sec`

### SELinux

| Variable | Default | Description |
|----------|---------|-------------|
| `selinux_state` | `permissive` | SELinux mode (`enforcing`, `permissive`, `disabled`) |
| `selinux_policy` | `targeted` | SELinux policy type |
| `selinux_booleans` | list | Boolean settings (name, state) |
| `selinux_fcontexts` | `[]` | File context definitions |
| `selinux_ports` | `[{ ports: "{{ sshd_port }}", proto: 'tcp', setype: 'ssh_port_t' }]` | Port type mappings |

### Auditd

| Variable | Default | Description |
|----------|---------|-------------|
| `auditd_rules` | list of rules | Custom audit rules (see `defaults/main.yml` for full list) |
| `auditd_config` | dict | Audit daemon configuration (log file, rotation, flush) |

### NFTables

| Variable | Default | Description |
|----------|---------|-------------|
| `nftables_allowed_tcp_dports` | `["{{ sshd_port }}"]` | List of allowed TCP destination ports |
| `nftables_allowed_udp_dports` | `[]` | List of allowed UDP destination ports |

### Internal Variables (vars/main.yml)

These variables are derived from the above and usually do not need to be changed directly:

- `sysctl_max_user_namespaces`
- `sysctl_net_forwarding_enabled`
- `sysctl_unprivileged_bpf_disabled`
- `sysctl_icmp_echo_ignore_all`

## Dependencies

None.

## Example Playbook

### Basic Security Hardening

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: security
  vars:
    sshd_port: 2222
    crowdsec_in_docker: false
    sysctl_user_namespace_enabled: false
```

### CIS‑Focused Configuration

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: security
  vars:
    sshd_log_level: INFO
    sshd_x11_forwarding: no
    sshd_print_motd: no
    sysctl_unprivileged_bpf_enabled: false
    systemd_default_limit_core: 0
    systemd_default_tasks_max: 512
```

### Using Tags

The role supports the following tags for selective execution:

- `security` – all tasks
- `sshd` – SSH configuration tasks
- `crowdsec` – CrowdSec installation and configuration (includes Docker, installation, and configuration)
- `auditd` – auditd setup
- `selinux` – SELinux configuration
- `sysctl` – sysctl tuning
- `pam` – PAM configuration
- `file-permissions` – file permissions hardening
- `grub` – GRUB configuration
- `nftables` – NFTables firewall rules
- `journald` – journald configuration
- `systemd` – systemd security settings
- `bash` – bash security settings (session timeout)

Example:

```bash
ansible-playbook -i inventory playbook.yml --tags "sshd,sysctl"
```

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

SECURITY
=========

Linux System security configuration using recommendations and best practices from multiple sources.

Cinfigure:
* Auditd
* Firewalld
* SSHD
* Sysctl

Install:
* Crowdsec

Requirements
------------

None

Role Variables
--------------

### Default

[Crowdsec documentation](https://doc.crowdsec.net/docs/next/intro)
* crowdsec_use_wal
* crowdsec_whitelist

[SSHD documentation](https://man.openbsd.org/sshd_config)
* sshd_log_level
* sshd_port
* sshd_address_famaly
* sshd_login_grace_time
* sshd_max_auth_tries
* sshd_max_sessions
* sshd_allow_agent_forwarding
* sshd_allow_tcp_forwarding
* sshd_x11_forwarding
* sshd_print_motd
* sshd_tcp_keep_alive
* sshd_client_alive_interval
* sshd_client_alive_count_max
* sshd_use_dns
* sshd_allow_users
* sshd_sftp_server_path
* sshd_listen_address_ipv4
* sshd_listen_address_ipv6
* sshd_deny_users

Sysctl

* unprivileged_bpf_enabled - enable or disable BPF.
* forwarding_enabled - enable or disable ipv4/ipv6 forwarding.
* user_namespace_enabled - enable or disable user namespace. true = 28633, false = 0

Molecule

* docker - excluding task with error in docker.

### Vars

Sysctl

* sysctl_max_user_namespaces - user.max_user_namespaces.
* sysctl_forwarding_enabled - net.ipv4.ip_forward and net.ipv6.conf.all.forwarding.
* sysctl_unprivileged_bpf_disabled - kernel.unprivileged_bpf_disabled.

Crowdsec

* crowdsec_package - crowdsed package version.
* crowdsec_firewall_bouncer_package crowdsec baunce package.

* crowdsec_version - crowdsed package version.
* crowdsec_firewall_bouncer_redhat_package - crowdsec bounce package for RedHat family.
* crowdsec_firewall_bouncer_debian_package - crowdsec bounce package for Debian family.

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: security
  vars:
    sshd_port: 2222
```

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

SECURITY
=========

Linux System security configuration using recommendations and best practices from multiple sources.

Configure:
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
* crowdsec_in_docker - type of install, docker or hosted.
* crowdsec_version - crowdsed version.
* crowdsec_firewall_bouncer_type - type of firewall.
* crowdsec_firewall_bouncer_version - firewall bouncer version.

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

* sysctl_unprivileged_bpf_enabled - enable or disable BPF.
* sysctl_forwarding_enabled - enable or disable ipv4/ipv6 forwarding.
* sysctl_user_namespace_enabled - enable or disable user namespace. true = 28633, false = 0
* sysctl_icmp_echo_ignore_all - enable or disable icmp echo ignore all.

Molecule

* docker - excluding task with error in docker.

NFTables

* nftables_allowed_tcp_dports - allowed tcp ports.
* nftables_allowed_udp_dports - allowed udp ports.

### Vars

Sysctl

* sysctl_max_user_namespaces - user.max_user_namespaces.
* sysctl_net_forwarding_enabled - net.ipv4.ip_forward and net.ipv6.conf.all.forwarding.
* sysctl_unprivileged_bpf_disabled - kernel.unprivileged_bpf_disabled.
* sysctl_icmp_echo_ignore_all_enabled - net.ipv4.icmp_echo_ignore_all


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

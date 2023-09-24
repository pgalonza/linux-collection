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

* crowdsec_package - crowdsed package version.
* crowdsec_firewall_bouncer_package crowdsec baunce package.

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


* sysctl_forwarding -  enable or disable forwarding.

Dependencies
------------

None

Example Playbook
----------------

- hosts: servers
  collections:
    - pgalonza.linux
  roles:
      - role: security
        vars:
          sshd_port: 2222

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

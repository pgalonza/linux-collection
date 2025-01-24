PREPARE
=========

Initial linux server configuration to use roles for IAC.

Cinfigure:
* SSH Keys
* SSHD
* Ansible user

Requirements
------------

None

Role Variables
--------------

### Default

[SSHD documentation](https://man.openbsd.org/sshd_config)
* sshd_port

* owner_user - personal linux user

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
    - role: prepare
  vars:
    sshd_port: 2222
```

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

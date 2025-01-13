PREPARE
=========

Set up a Linux server to use roles for IAC..

Cinfigure:
* SSH Keys
* SSHD

Requirements
------------

None

Role Variables
--------------

### Default

[SSHD documentation](https://man.openbsd.org/sshd_config)
* sshd_port

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

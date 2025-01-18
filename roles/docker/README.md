Docker
=========

Intsll docker.

Configure:
* Docker

Requirements
------------

None

Role Variables
--------------

Node

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
    - role: docker
```

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

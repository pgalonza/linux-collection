NGINX
=========

Nginx install and security configuration

Requirements
------------

None

Role Variables
--------------

None

Dependencies
------------

Roles:
* nginxinc.nginx_core.nginx

Example Playbook
----------------

```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: nginx
```

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

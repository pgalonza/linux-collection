Bash prompt
=========

Gathering security status reports using third-Party utilities and general recommendations.

Requirements
------------

None

Role Variables
--------------
* audit_dir - local report directory
* lynis_version: 3.0.9

Dependencies
------------

None

Example Playbook
----------------

- hosts: servers
  collections:
    - pgalonza.linux
  roles:
      - role: audit

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

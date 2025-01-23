Bash prompt
=========

Bash prompt customization for informational purposes and human error reduction

Requirements
------------

None

Role Variables
--------------
* bash_prompt - prompt template for PS1 variable.
* bash_server_role - name of server role.
* bash_on_login_message: - welcome Message for System Logged-in Users.

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
    - role: bash_profile
  vars:
    bash_server_role: Test
```

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

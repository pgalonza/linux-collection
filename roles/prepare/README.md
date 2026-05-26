PREPARE
=========

Initial Linux server configuration to use roles for Infrastructure‑as‑Code (IaC).

## Purpose

This role performs basic provisioning tasks that prepare a fresh Linux server for automated management with Ansible. It sets up SSH access, creates a dedicated Ansible user, and configures the SSH daemon to allow secure remote administration.

## Features

- **SSH key deployment** – copies your public SSH key to the target server
- **Ansible user creation** – creates a dedicated `ansible` user with sudo privileges
- **SSHD configuration** – adjusts SSH daemon settings (port, etc.)
- **Basic system readiness** – ensures the server can be managed by subsequent roles

## Requirements

None. The role works on RedHat/CentOS and Debian/Ubuntu families.

## Role Variables

### Default Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `sshd_port` | `22` | SSH listening port (will be configured in `sshd_config`) |
| `ssh_key_dir` | `~/.ssh` | Local directory containing your SSH key (on the control node) |
| `ansible_deploy_user` | `ansible` | Name of the user that will be created on the target server |
| `admin_ssh_key_name` | `id_rsa` | Filename of the SSH public key (without `.pub`) located in `ssh_key_dir` |
| `admin_user` | `root` | Remote user used for initial connection (must have sudo/root privileges) |

### Notes

- The role assumes you have an SSH key pair on your Ansible control node. The public key (`~/.ssh/id_rsa.pub` by default) will be copied to the target server and added to the `authorized_keys` of the newly created `ansible` user.
- The `admin_user` is the user that Ansible uses to connect initially (usually `root` or a user with passwordless sudo). After the `ansible` user is created and its SSH key is deployed, subsequent playbook runs can switch to using that user.

## Dependencies

None.

## Example Playbook

### Basic Preparation

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: prepare
  vars:
    sshd_port: 2222
    admin_user: "ubuntu"   # if connecting as a non‑root user (e.g., on AWS)
```

### Custom SSH Key Location

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: prepare
  vars:
    ssh_key_dir: "/home/{{ ansible_user }}/.ssh"
    admin_ssh_key_name: "my_key"
```

### Using Tags

The role supports the following tags for selective execution:

- `prepare` – all tasks
- `ssh_keys` – SSH key deployment tasks
- `user` – user creation tasks
- `sshd` – SSH daemon configuration tasks

Example:

```bash
ansible-playbook -i inventory playbook.yml --tags "ssh_keys,user"
```

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

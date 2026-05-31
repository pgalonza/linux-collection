# Ansible Collection - pgalonza.linux

This collection contains roles for customizing Linux system settings, configuring in accordance with best security practices, conducting an audit and using third-party software to further prepare the system for operation.

## Overview

The `pgalonza.linux` collection provides a set of Ansible roles to automate Linux system hardening, security auditing, and baseline configuration. It is designed to help system administrators and DevOps teams maintain consistent, secure, and well‑audited Linux environments across multiple distributions.

## Collection Details

- **Namespace**: `pgalonza`
- **Name**: `linux`
- **Version**: 1.0.0
- **License**: Apache‑2.0
- **Author**: Peter Galonza <p.galonza@evaron.ru>
- **Repository**: https://github.com/pgalonza/linux-collection

## Requirements

- Ansible 2.9 or higher
- Target systems: Linux (RedHat/CentOS 7+, Debian/Ubuntu 18.04+)
- Python 3.6+

### Collection Dependencies

The collection depends on the following Ansible Galaxy collections (see `galaxy.yml`):

- `community.general` (>=11.0.0)
- `community.crypto` (>=3.0.0)
- `ansible.posix` (>=2.0.0)
- `community.docker` (>=5.0.0)

Install them with:

```bash
ansible-galaxy collection install -r requirements.yml
```

## Included Roles

| Role | Purpose | Key Features |
|------|---------|--------------|
| **security** | System‑wide security hardening | Configures SSH, firewalld/nftables, sysctl, auditd, SELinux, PAM, journald, CrowdSec intrusion detection, and systemd security parameters. |
| **audit** | Security compliance scanning | Runs OpenSCAP (CIS profiles), Lynis, Kaspersky Virus Removal Tool (KVRT), and basic security checks. Generates detailed reports. |
| **prepare** | Initial server provisioning | Sets up SSH keys, configures SSHD, creates an Ansible user, and prepares the system for infrastructure‑as‑code management. |
| **bash_profile** | Shell environment customization | Customizes the bash prompt with server role information and displays a welcome message on login. |
| **docker** | Docker Engine installation | Installs Docker CE and configures daemon options. |
| **nginx** | Nginx web server installation | Installs and secures Nginx using the `nginxinc.nginx` role. |

## Quick Start

1. Install the collection:

   ```bash
   ansible-galaxy collection install git+https://github.com/pgalonza/linux-collection.git
   ansible-galaxy install -r ~/.ansible/collections/ansible_collections/pgalonza/linux/requirements.yml
   ```

2. Create a playbook (e.g., `site.yml`) that includes the roles you need:

   ```yaml
   ---
   - hosts: all
     become: true
     collections:
       - pgalonza.linux
     roles:
       - prepare          # initial setup
       - security         # security hardening
       - bash_profile     # shell customization
       - audit            # compliance scanning
   ```

3. Run the playbook:

   ```bash
   ansible-playbook -i inventory site.yml
   ```

## Role‑Specific Documentation

Each role contains its own detailed README with variable descriptions, examples, and usage notes. Refer to the following files:

- `roles/security/README.md`
- `roles/audit/README.md`
- `roles/prepare/README.md`
- `roles/bash_profile/README.md`
- `roles/docker/README.md`
- `roles/nginx/README.md`

## Example Playbooks

### Basic Security Hardening

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - security
  vars:
    sshd_port: 2222
    crowdsec_in_docker: false
```

### Compliance Audit Only

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - audit
  vars:
    auditor_name: "Security Team"
    openscap_enabled: true
    openscap_cis_profile: "xccdf_org.ssgproject.content_profile_cis"
```

### Multi‑Role Deployment

See the included example playbook `playbooks/linux_playbook.yml` for a typical full‑stack deployment.

## Variables and Customization

Each role exposes a set of variables that allow you to tailor the configuration to your environment. The variables are documented in the role’s `defaults/main.yml` and `vars/main.yml` files, and summarized in the role’s README.

Example:

```bash
ansible-playbook -i inventory site.yml --tags "security,configure"
```

## Testing

The collection includes Molecule test scenarios for each role (located in `extensions/molecule/`). To run the tests:

```bash
cd extensions/molecule/<role>
molecule test
```

## Contributing

Contributions are welcome. Please open an issue or submit a pull request on the [GitHub repository](https://github.com/pgalonza/linux-collection).

## License

Apache‑2.0. See the `LICENSE` file for details.

## Author Information

- **Peter Galonza** – <p.galonza@evaron.ru>
- Project home: https://github.com/pgalonza/linux-collection

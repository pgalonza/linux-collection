Bash prompt
=========

Bash prompt customization for informational purposes and human error reduction.

## Purpose

This role customizes the bash prompt (`PS1`) and displays a welcome message when users log in. The prompt is designed to show important context such as the server’s role, current user, hostname, and working directory, helping administrators quickly identify which system they are working on and reducing the risk of human error.

## Features

- **Customizable PS1** – color‑coded prompt with server role, user, host, and path
- **Per‑user configuration** – apply prompt changes only to specified users
- **Login message** – display a welcome banner with server role information
- **Cross‑platform** – works on RedHat/CentOS and Debian/Ubuntu families

## Requirements

None.

## Role Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `bash_server_role` | `Development` | Name of the server role (e.g., "Production", "Staging", "DB") that appears in the prompt and login message |
| `bash_on_login_message` | `"This is a {{ bash_server_role }} server"` | Welcome message shown to users upon login (written to `/etc/motd` or similar) |
| `bash_prompt_users` | `["{{ ansible_user }}"]` | List of usernames whose bash prompts will be customized. If empty, the prompt is set globally. |
| `bash_prompt` | (see below) | The template for the `PS1` environment variable. The default produces a two‑line prompt with colors. |

### Default `bash_prompt` Value

```bash
PS1="@ \[\033[38;5;42m\]{{ bash_server_role }}\[$(tput sgr0)\]\n[\[$(tput sgr0)\]\[\033[38;5;75m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;42m\]\h\[$(tput sgr0)\] \W]\\$ \[$(tput sgr0)\]"
```

This results in a prompt that looks like:

```
@ Production
[user@hostname ~]$
```

- First line shows the current time (`@`) and the server role in green.
- Second line shows `[user@hostname working‑dir]$` with user in blue, hostname in green.

## Dependencies

None.

## Example Playbook

### Basic Usage

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: bash_profile
  vars:
    bash_server_role: "Production"
```

### Customizing Users and Message

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: bash_profile
  vars:
    bash_server_role: "Database"
    bash_on_login_message: "This is a critical database server. Modify with caution."
    bash_prompt_users:
      - postgres
      - admin
      - "{{ ansible_user }}"
```

### Overriding the Prompt Template

```yaml
- hosts: servers
  become: true
  collections:
    - pgalonza.linux
  roles:
    - role: bash_profile
  vars:
    bash_server_role: "Testing"
    bash_prompt: 'PS1="[\u@\h \W]\\$ "'
```

## How It Works

1. The role creates a shell script (`/etc/profile.d/ansible‑prompt.sh`) that sets `PS1` for all users (or only for users listed in `bash_prompt_users`).
2. If `bash_on_login_message` is defined, it writes the message to `/etc/motd` (or uses `pam_motd` on Debian/Ubuntu) so it appears after login.
3. The changes take effect for new login sessions; existing sessions are not affected.

## Tags

The role supports the following tags:

- `bash_profile` – all tasks
- `prompt` – prompt customization tasks only
- `motd` – login message tasks only

Example:

```bash
ansible-playbook -i inventory playbook.yml --tags prompt
```

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

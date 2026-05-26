Audit
=========

Gathering security status reports using third‑party utilities and general recommendations.

## Overview

The `audit` role runs multiple security scanning and compliance tools on the target system, collects their reports, and stores them locally for analysis. It is designed to provide a comprehensive view of the system’s security posture and compliance with benchmarks such as CIS.

**New in version 2.0**: OpenSCAP integration for CIS compliance scanning.

## Features

- **Basic security checks** – quick assessment of users, connections, file permissions, etc.
- **Lynis** – system auditing and hardening tool (version 3.1.6)
- **Kaspersky Virus Removal Tool (KVRT)** – on‑demand antivirus scan
- **OpenSCAP** – CIS compliance scanning with HTML, XML, and ARF report generation
- **Centralized reporting** – all reports are gathered in a single local directory

## Requirements

### OpenSCAP
- **RedHat/CentOS**: `openscap-scanner`, `scap-security-guide` packages
- **Debian/Ubuntu**: `openscap-scanner`, `ssg-base`, `ssg-debian`, `ssg-debderived` packages
- Internet access to download SCAP content (or pre‑installed `scap-security-guide`)

### Lynis
- Internet access to download Lynis archive (if not already installed)

### KVRT
- Internet access to download Kaspersky Virus Removal Tool

## Role Variables

### Directly Configurable Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `audit_dir` | `./audit/{{ inventory_hostname }}` | Local directory (on the control node) where all reports will be stored |
| `lynis_version` | `3.1.6` | Version of Lynis to download and use |
| `auditor_name` | `{{ ansible_user }}` | Name of the auditor (embedded in some reports) |
| `kvrt_report_dir` | `/tmp/kvrt-report` | Temporary directory on the target for KVRT reports |
| `openscap_report_dir` | `/tmp/openscap-reports` | Directory on the target where OpenSCAP reports are generated |
| `openscap_cis_profile` | `xccdf_org.ssgproject.content_profile_cis` | OpenSCAP profile to use for the scan |
| `openscap_scan_timeout` | `1800` | Timeout (in seconds) for the OpenSCAP scan command |

### Notes

- The role does **not** provide an `openscap_enabled` variable. To skip OpenSCAP scanning, use Ansible tags.
- Lynis and KVRT are always executed unless skipped via Ansible tags.
- Reports are copied from the target to `audit_dir` on the control node after each tool finishes.

## Generated Reports

The role generates the following reports in the `audit_dir`:

1. **Basic security checks** – a text file with basic system information, connections, users, and file permissions.
2. **Lynis report** – `lynis-report.txt` (human‑readable) and `lynis-report.dat` (machine‑readable).
3. **KVRT reports** – `kvrt-reports.tar` containing antivirus scan results.
4. **OpenSCAP reports** (when enabled):
   - `openscap-summary.txt` – summary of compliance scan
   - `{host}-{os}-{version}-report.html` – detailed HTML report with findings
   - `{host}-{os}-{version}-results.xml` – XML results for machine processing
   - `{host}-{os}-{version}-arf.xml` – ARF (Asset Reporting Format) for integration with other tools

## Dependencies

- For RedHat systems: `openscap-scanner`, `scap-security-guide` packages (installed by the role)
- For Debian systems: `openscap-scanner`, `ssg-base`, `ssg-debian`, `ssg-debderived` packages (installed by the role)

## Example Playbook

### Full Audit (All Tools)

```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: audit
  vars:
    auditor_name: "Security Team"
    openscap_cis_profile: "xccdf_org.ssgproject.content_profile_cis"
```

### OpenSCAP Only (CIS Compliance)

```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: audit
  vars:
    auditor_name: "CIS Auditor"
```

## License

Apache‑2.0

## Author Information

* Peter Galonza <p.galonzapv@evaron.ru>

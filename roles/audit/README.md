Audit
=========

Gathering security status reports using third-Party utilities and general recommendations.

**New in version 2.0**: OpenSCAP integration for CIS compliance scanning.

Requirements
------------

* For OpenSCAP functionality: Internet access to download SCAP content (or pre-installed scap-security-guide)
* For Lynis: Internet access to download Lynis archive
* For KVRT: Internet access to download Kaspersky Virus Removal Tool

Role Variables
--------------
* `audit_dir` - local report directory.
* `lynis_version` - lynis version number.
* `auditor_name` - name of auditor.
* `kvrt_report_dir` - KVRT report directory.
* `openscap_enabled` - enable/disable OpenSCAP scanning (default: true)
* `openscap_report_dir` - directory for OpenSCAP reports on target (default: /tmp/openscap-reports)
* `openscap_cis_profile` - CIS profile to use (default: xccdf_org.ssgproject.content_profile_cis)
* `openscap_scan_timeout` - timeout for OpenSCAP scan in seconds (default: 1800)

Dependencies
------------

* For RedHat systems: `openscap-scanner`, `scap-security-guide` packages
* For Debian systems: `openscap-scanner`, `ssg-base`, `ssg-debian`, `ssg-debderived` packages

Generated Reports
-----------------

The role generates the following reports in the `audit_dir`:

1. **Basic security checks**: connections, users, file permissions, etc.
2. **Lynis report**: `lynis-report.txt` and `lynis-report.dat`
3. **KVRT reports**: `kvrt-reports.tar` (antivirus scan results)
4. **OpenSCAP reports** (when enabled):
   * `openscap-summary.txt` - summary of compliance scan
   * `{host}-{os}-{version}-report.html` - HTML report with detailed findings
   * `{host}-{os}-{version}-results.xml` - XML results for machine processing
   * `{host}-{os}-{version}-arf.xml` - ARF (Asset Reporting Format) for integration

Example Playbook
----------------

```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: audit
  vars:
    auditor_name: "Security Team"
    openscap_enabled: true
    # Disable KVRT if not needed
    # kvrt_enabled: false
```

Example Playbook with OpenSCAP only:
```yaml
- hosts: servers
  collections:
    - pgalonza.linux
  roles:
    - role: audit
  vars:
    auditor_name: "CIS Auditor"
    # Run only OpenSCAP for compliance checking
    openscap_enabled: true
    # Skip other tools using tags
  tags:
    - openscap
```

Tags
----

* `openscap` - Run only OpenSCAP tasks
* `lynis` - Run only Lynis tasks
* `kvrt` - Run only KVRT tasks
* `audit` - Run only basic audit tasks
* `install` - Installation tasks only

License
-------

Apache-2.0

Author Information
------------------

* Peter Galonza <p.galonzapv@evaron.ru>

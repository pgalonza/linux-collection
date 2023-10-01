def lynis_install(host):
    lynis_version = host.ansible.get_variables()["lynis_version"]
    assert host.file("/tmp/lynis-" + lynis_version).exists

def lynis_report(host):
    assert host.file("/var/log/lynis-report.dat").exists

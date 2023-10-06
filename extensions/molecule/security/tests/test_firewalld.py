def test_profile_file(host):
    ssh_rule = host.file("/etc/firewalld/services/ssh-custom.xml").exists
    distro_name = host.system_info.distribution
    print(distro_name)

    if distro_name in ['debian', 'ubuntu']:
        assert True
    elif distro_name in ['redhat', 'almalinux']:
        assert ssh_rule

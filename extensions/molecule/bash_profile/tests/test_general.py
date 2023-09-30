def test_massage_file(host):
    massage = host.file("/etc/profile.d/on-login-message.sh")
    assert massage.user == "root"
    assert massage.group == "root"
    assert massage.mode == 0o755

def test_profile_file(host):
    distro_name = host.system_info.distribution
    print(distro_name)
    user_home = host.user().home

    if distro_name in ['debian', 'ubuntu']:
        profile_name = '.profile'
    elif distro_name in ['redhat', 'almalinux']:
        profile_name = '.bash_profile'

    profile = host.file(user_home + "/" + profile_name)
    assert profile.contains("PS1")

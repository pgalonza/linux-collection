def test_massage_file(host):
    massage = host.file("/etc/profile.d/on-login-message.sh")
    assert massage.user == "root"
    assert massage.group == "root"
    assert massage.mode == 0o755

def test_profile_file(host):
    user_home = host.user().home
    profile = host.file(user_home + "/.bash_profile")
    assert profile.contains("PS1")

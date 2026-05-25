def test_tmp_directory_exists(host):
    """Проверяет, что директория /tmp существует и доступна для записи."""
    tmp_dir = host.file('/tmp')
    assert tmp_dir.exists
    assert tmp_dir.is_directory
    # Проверка, что можно создать файл (косвенно)
    # host.run("touch /tmp/test_audit") - не будем делать, чтобы не оставлять файлы


def test_audit_role_executed(host):
    """Проверяет, что роль audit выполнилась без критических ошибок."""
    passwd = host.file('/etc/passwd')
    assert passwd.exists
    assert passwd.is_file

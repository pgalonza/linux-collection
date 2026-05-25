def test_nginx_ssl_directory(host):
    """Проверяет создание директории /etc/nginx/ssl"""
    ssl_dir = host.file('/etc/nginx/ssl')
    assert ssl_dir.exists
    assert ssl_dir.is_directory
    assert ssl_dir.mode == 0o700


def test_dhparams_file(host):
    """Проверяет наличие файла DH параметров"""
    dh_file = host.file('/etc/nginx/ssl/dhparams.pem')
    assert dh_file.exists
    assert dh_file.is_file


def test_nginx_config(host):
    """Проверяет наличие основного конфигурационного файла nginx"""
    config = host.file('/etc/nginx/nginx.conf')
    assert config.exists
    assert config.is_file
    assert config.mode == 0o600
    assert config.user == 'root'
    assert config.group == 'root'
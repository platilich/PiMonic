import distro

def get_name_os():
    # .name() вернет полное название, например "Ubuntu" или "Debian GNU/Linux"
    # .id() вернет короткий идентификатор, например "ubuntu"
    return distro.name()

print(get_name_os())

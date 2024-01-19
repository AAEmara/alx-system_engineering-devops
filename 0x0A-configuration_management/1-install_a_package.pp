# Puppet manifest that installs `flask` using `pip3`.
# `flask` version is `2.1.0`.
exec {'install Flask':
    command  => "pip3 install  Flask=='2.1.0'",
    provider => 'shell',
}

# Installing `Werkzeug` version `2.1.1` using `pip3`.
exec {'install Werkzeug 2.1.1':
    command  => "pip3 install Werkzeug=='2.1.1'",
    provider => 'shell',
}

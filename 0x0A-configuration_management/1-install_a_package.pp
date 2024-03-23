# Installing flask from pip3


package {'python3-pip':
  ensure => 'installed'
}

$flask_version = '2.1.0'

exec {'install_flask':
  command => "/usr/bin/pip3 install Flask== &flask_version",
  require => Package['python3-pip']
}

# Installing flask from pip3


$package = 'python3-pip3'
$flask_version = '2.1.0'

package {$package:
  ensure => 'installed',
}

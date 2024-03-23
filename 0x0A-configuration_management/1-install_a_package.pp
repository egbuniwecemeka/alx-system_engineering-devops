# A puppet script that installs flask using pip3
package {'flask':
  ensure => 'installed',
  provider => 'pip3'
}

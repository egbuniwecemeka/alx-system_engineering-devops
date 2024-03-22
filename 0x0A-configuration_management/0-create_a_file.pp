# Create a file in /tmp using puppet
$doc_root = '/tmp'
$str = 'I love Puppet'

file {"${doc_root}/school":
  ensure => file,
  mode => '0744',
  owner => 'www-data',
  group => 'www-data',
  content => $str
}

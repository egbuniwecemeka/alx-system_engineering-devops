# Puppet script that updates the hard and soft limit of a user's file ULIMIT value

# Updating the hard file limit for Holberton user
exec{'hard_file_limit':
  command => 'sed -i "/^holberton hard nofile/s/5/48000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Update the soft file limit of Holberton user
exec{'soft_file_limit_':
  command => 'sed -i "/^holberton soft/s/4/47000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
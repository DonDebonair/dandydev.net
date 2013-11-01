Title: Setting up Sentry using Vagrant and Puppet
Date: 2013-11-01 23:00
Tags: sentry, vagrant, puppet, devops
Slug: setting-up-sentry-using-vagrant-and-puppet

Devops is hot! And these days, [everyone is diving into the provisioning game](http://blog.publysher.nl/2013/07/infra-as-repo-using-vagrant-and-salt.html). I was invited by the company I work for, to visit the [Devops Days](http://www.devopsdays.org/events/2013-amsterdam/) together with some fellow engineers and the talks there really inspired me! Always eager to learn a new thing or two, I set myself the task of investigating Vagrant in combination with some flavor of provisioning; options for the latter being: [Puppet](http://puppetlabs.com/puppet/puppet-open-source), [Chef](http://www.opscode.com/chef/), [Ansible](https://github.com/ansible/ansible) or [Salt](https://github.com/saltstack/salt). I'm already in love with Vagrant, which I use all the time, [to test out](https://github.com/jpadilla/statsd-graphite-vm) all kinds of tools I come across. I have absolutely no experience however with provisioning tools, so I wanted to learn that too. Ofcourse, finding time to actually get to it, proves difficult these days. 

So when I wanted to check out the promising looking monitoring tool [Sentry](https://getsentry.com), and no working Vagrant setup seemed to exist to try it out in a Virtual Machine, an opportunity presented itself!

### Vagrant & Puppet, a solid duo

I'm a Python guy, so the obvious choice for a provisioning tool would be either Ansible or Salt. But [at work](http://www.info.nl/en), the hosting department uses Puppet, so it made sense to check that out first. A nice added bonus is that Vagrant has really solid Puppet support. A Vagrant setup for Sentry using Puppet, [already exists](https://github.com/praekelt/sentry-deploy) by the way, but it hasn't been updated for a year or so, so unsurprisingly, it doesn't work anymore. Instead of trying to fix it, I decided to try writing my own Vagrantfile and Puppet scripts (called manifests).

![Challenge Accepted!]({filename}/images/Challenge-Accepted.jpg)

### Results & Caveats

I could rehash here, what it is I have done, but [the code is on GitHub](https://github.com/DandyDev/sentry-vagrant), and it speaks for itself! What it basically installs is:

* Sentry
* PostgreSQL as database for Sentry
* Supervisord as a tool for running Sentry and keeping it up
* NginX as reverse proxy in front of Sentry

It's pretty basic, but I'm happy with the results nonetheless! All in all, learning Puppet wasn't too hard, but there are some gotcha's and caveats which I want to share:

* Puppet isn't about chaining together commands to get to the desired configuration. It's about defining the desired state and let Puppet do the rest. You're pretty much "ensuring" that stuff is "present" (or absent, for that matter).
* When you define states, don't expect Puppet to adhere to any implied ordering! It doesn't run through your manifest making sure stuff is installed in the order you defined it. If you want ordering, you have to explicitly declare dependencies like so:

```puppet
package { [
        "libpq-dev",
  "supervisor",
  "nginx",
  ]:
  ensure => latest,
  require => [Exec['update_apt'], Class['python']]; # apt-get update needs to be executed first, and the `python` class needs to be run
}
```

* In a frustrating exercise of debugging, I discovered that in the next example `apt-get update` isn't actually run, despite it being a dependency for installing the PostgreSQL Server:

```puppet
class { 'postgresql::server': 
        require => Exec['update_apt'];
}
```

* Letting Puppet install some other packages at with the `package` directive, with `apt-get update` as a requirement, makes the PostgreSQL install run flawlessly as well...

### Next steps

I want to make the installation more OS-agnostic. Currently it's tied to Ubuntu/Debian because of the use of `apt`. I would also love to test it with other providers, so my plan is to try and use the scripts to install Sentry on a [Digital Ocean](https://www.digitalocean.com/) droplet. In the meanwhile, I encourage anyone who is interested in Sentry to give it a spin and simultaneously feeling the joy of Vagrant and Puppet!

[Code on GitHub](https://github.com/DandyDev/sentry-vagrant)

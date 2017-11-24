Title: VirtPHP: filling a non-existing gap
Date: 2014-03-15 17:00
Slug: virtphp-filling-a-non-existing-gap

About a week ago, a tweet caught my eye about a project called [VirtPHP](http://virtphp.org/). Now, I don't follow many people from the PHP community anymore, because I've really grown to dislike PHP over the past few years, and I've mostly gone [off to](https://www.python.org/) [greener](http://www.oracle.com/technetwork/java/index.html) [pastures](http://www.scala-lang.org/). But I still follow a couple of folks, most notably from the Symfony & Doctrine projects, because I'm a masochist, and I'm morbidly interested in how this whole PHP mess is going to evolve...

Anyways, this is the relevant tweet:

<blockquote class="twitter-tweet" lang="en"><p>After a year, we&#39;ve finally released the first <a href="https://twitter.com/virtPHP">@VirtPHP</a> alpha. It&#39;s a tool to create isolated PHP dev environments. <a href="http://t.co/9vqBicojxE">http://t.co/9vqBicojxE</a></p>&mdash; Ben Ramsey (@ramsey) <a href="https://twitter.com/ramsey/statuses/440923075098714112">March 4, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Naturally, I took a look at the project, and soon a short exchange of words with the project's initiators followed:

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/ramsey">@ramsey</a> <a href="https://twitter.com/virtPHP">@VirtPHP</a> seems superfluous because of Composer and vendor&#39;d package installs. Maybe handy for diff php versions, but that&#39;s it.</p>&mdash; Daan Debie (@DaanDebie) <a href="https://twitter.com/DaanDebie/statuses/443067360698970112">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/DaanDebie">@DaanDebie</a> That&#39;s its primary use-case. It&#39;s for devs who work on many different projects, each with different PHP and PECL requirements.</p>&mdash; Ben Ramsey (@ramsey) <a href="https://twitter.com/ramsey/statuses/443067785900331008">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/ramsey">@ramsey</a> <a href="https://twitter.com/virtPHP">@VirtPHP</a> also, virtualenv is needed cause of fundamentally different way Python package management is setup. PHP doesn&#39;t need that.</p>&mdash; Daan Debie (@DaanDebie) <a href="https://twitter.com/DaanDebie/statuses/443067657982836736">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/DaanDebie">@DaanDebie</a> You&#39;ll need to elaborate, since I don&#39;t see a big difference.</p>&mdash; Ben Ramsey (@ramsey) <a href="https://twitter.com/ramsey/statuses/443067978888663041">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/DaanDebie">@DaanDebie</a> if you run multiple VMs for different projects, or are looking for easy way to test upgrades we offer great benefits. <a href="https://twitter.com/ramsey">@ramsey</a></p>&mdash; virtPHP (@virtPHP) <a href="https://twitter.com/virtPHP/statuses/443072141970661376">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

<blockquote class="twitter-tweet" data-conversation="none" lang="en"><p><a href="https://twitter.com/DaanDebie">@DaanDebie</a> if youre fortunate enough to have one code base or put all your projects on the same config, we offer small benefits cc <a href="https://twitter.com/ramsey">@ramsey</a></p>&mdash; virtPHP (@virtPHP) <a href="https://twitter.com/virtPHP/statuses/443071746389069824">March 10, 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

At the time, I didn't feel like spamming my elaboration in 140-character snippits on Twitter, but I realized that the faults I see in virtPHP are part of a more pervasive problem in see in PHP-land: people putting lots of time (1 year in this case, for only an alpha version!) into problems that don't need solving.

In this post I want to elaborate on why virtPHP solves a problem that doesn't actually exist.

### What problems does virtPHP try to solve?

As far as I could deduce from the tweets, the website and their [GitHub repo](https://github.com/virtphp/virtphp), virtPHP is a tool that allows you to create separate PHP environments. That allows you to do the following:

* Use differing sets of PECL extensions
* Use different PEAR packages, including different versions of the same package
* Use different versions of PHP

(Also, according to the website "Note: virtPHP is currently only targeted to command line php (php-cli) for *nix based systems." Does this mean I can't use virtPHP for having different PHP installs for developing _web applications_?!)

Granted, I've been out of the PHP loop for a while now, but I still have a pretty decent grasp of what's going on there. So I've come to the conclusion that in the current state of affairs with regards to PHP development, all those problems are solved already or don't need to be solved.



### Package Management

Despite my dislike for PHP, I don't think it's all Fire & Brimstone. In fact, one of the things the PHP community _did get right_ is Package Management. With the arrival of [Composer](https://getcomposer.org/), package management - using third party libraries and frameworks - has become rediculously easy. [PEAR](http://pear.php.net/) is quickly becoming a [thing of the past](http://benramsey.com/blog/2013/11/the-fall-of-pear-and-the-rise-of-composer/), if it hasn't already.

On the its website, virtPHP gets likened to [virtualenv](http://www.virtualenv.org/). Even the name resembles its Python counterpart. For those who don't know: _virtualenv_ allows Python programmers to have separate environments to develop in, for different projects, much like virtPHP advertises. Now, as I've mentioned in my tweets, virtualenv is a necessary contract within the Python world because of how package management is set up. When you install a package for Python, using [`easy_install`](http://pythonhosted.org/setuptools/easy_install.html) or [`pip`](http://www.pip-installer.org/), packages get installed system-wide. They will end up in a place related to your Python interpreter. The same goes for using installing [Rubygems](http://rubygems.org/) for Ruby, using `gem install`. When working on different projects, that can quickly become a mess of conflicting dependencies and versions.

Composer however, solves this neatly by installing packages in a _vendor_ directory, relative to your project root. In a way, it's more a dependency manager than a package manager, it even says so [on the website](https://getcomposer.org/doc/00-intro.md#dependency-management). [Bundler](http://bundler.io/) for Ruby does the same. This removes the need for separate environments to avoid conflicts between packages and projects.

Seeing that Composer negates the need for using PEAR (which virtPHP mentions) for installing packages, there's no problem that virtPHP needs to solve in relation to package management.

### PECL Extensions and PHP versions

The other usescases for virtPHP have to do with managing different sets of PECL extensions and different PHP versions. PECL is a system for distributing PHP extensions. Let me start by saying that the need for extensions to the PHP core is dangerous at best. If you need extra functionality, then there are PHP packages for that, that can be installed with Composer. Or we might be talking about PHP bindings for some C library, but in my opinion it should be trivial to include those as a package in your project as well. If some feature really merits writing a C extension for that, it's probably better suited as a part of the core language.

Now, there are some scenarios in which (C) extensions are a necessary evil. For instance if you want to use ImageMagick, you'll need the PHP bindings, which come in the form of an extension. Installing extensions, and especially switching between extensions, should not be a thing you do often, though. I really doubt if you'll ever bump into conflicts because of extensions you installed. Most extensions shouldn't bother you if they're installed, but you don't use them in a project.

Switching between PHP versions could be the only legitimate usecase for virtPHP, but only if you're developing a library that is going to be used by lots of people with lots of different PHP versions you need to test/develop against. In all other cases - building webapps mostly - I'm assuming you have complete control over the production environment, so you can choose which PHP version your projects run on. It's easy then to develop all your projects against that version, and there's no need to switch to different versions.

It's interesting to note, by the way, that according to it's website, virtPHP doesn't actually let you install different PHP versions side by side. You need [other](https://github.com/CHH/phpenv) [tools](https://github.com/CHH/php-build) for that.

Should you still want to use different versions of PHP with different extensions installed, you're still not going to use virtPHP, because there are better solutions...

### Separate development environments done the right way

If you really want to have different development environments for different projects, and as an added bonus have parity between your production systems and development environments, you should setup Virtual Machines to run your code on, using [Vagrant](http://www.vagrantup.com/) and some form of provisioning.

In fact, you don't even have to understand how provisioning tools work. There are multiple tools to help you setup disposable development environments with your exact specifications:

* [Puphpet](https://puphpet.com/)
* [Rove](http://rove.io/)
* [Protobox](http://getprotobox.com/)

I highly suggest you give them a spin to make your life and that of your fellow developers much easier!

### Conclusion

The world does not need virtPHP. Package mangement is a solved problem for PHP these days, and using different PHP versions and language extensions is mostly a non-issue. But the real problem with virtPHP is that you should approach the problem of having different development environments for different projects, from a whole different angle. Devops is hot these days, and it has given us many tools to help us out in that department.

It's shocking to me that people would spend a year to develop a tool without actually finding out if the problems they're trying to solve, has been solved already. Maybe that's part of the PHP-problem, the community should spend their time more wisely.
Title: Crashing servers and riding waves
Date: 2013-08-22 22:30
Tags: this site, pelican, vps, security
Slug: crashing-servers-and-riding-waves

In my [last blog](|filename|/brand-spankin-new-blog.md) I mentioned that I've had some security-related problems with my previous VPS. [A commenter](http://www.publysher.nl/) asked what happened and how bad it was, and he also wanted to know why I chose Pelican for this site. I'm taking his suggestion to write about it on my blog, especially now that I know I'll have a good chance of having an audience of at least one! I'll start with the VPS situation.

### Old VPS & Security

So yeah, my old website went dark for more than a month. It all started with a mail from [my previous VPS provider](http://www.alvotech.de/). They'd had a complaint about someone's server being probed from my IP address. Of course, I knew nothing about anything. [A friend](http://www.vandorp.biz/) offered to have a look at my VPS for any security breaches and malware. As it turned out, I really know nothing, at least not about properly securing my server… (Note to current and future employers: I've learned)

![](|filename|/images/you-know-nothing.jpg)

A scan with `clamscan` and `rootkithunter` turned up `scanssh` (a SSH portscanner), and an IRC Bouncer. My friend proceeded to delete everyhing that was remotely harmful. After that, I still didn't feel completely secure, so I backed up everything and did a complete wipe & reinstall. This all went fairly smooth, in part because of [this handy set of scripts](http://tuxlite.com/) which you can use to install a LAMP/LNMP stack if provisioning tools like Ansible/Puppet/Chef/Saltstack are overkill. After one reboot I couldn't SSH into my VPS anymore. So I wiped the whole thing yet again, with no luck. After mailing back and forth a few times with the totally unhelpful "servicedesk" people, who did nothing to fix the situation, I gave up. I figured that when even a complete wipe through their control panel doesn't help, the problem would have to be on their end. Apparently they didn't think so. "Unmanaged" in the most literal sense of the word.

### New VPS

This was as good a time as any to dump the old cruft and begin anew. The same friend that was helpful in fixing the security issue, is also an expert on securing ridiculously good VPS deals. Really. He hangs around [LowEndTalk](http://lowendtalk.com/) on a daily basis and knows most of the smaller VPS providers personally. He recommended [Waveride](https://waveride.at/), a new subsidiairy of [Edis](http://www.edis.at/). They provide really cheap VPSes, completely unmanaged (let's hope this won't go wrong again), with SolusVM on top for really low prices. See for yourself.

The experience so far has been great. I installed a LNMP stack on it, tinkered around with NGinx (which was new to me) and put this blog online without problems whatsoever. At some point shortly after getting my new VPS, a large security hole was discovered in SolusVM, so Waveride immediately disabled it on all of their VPSes until the issue was resolved. For the duration of the 'outage' they offered to take care of all VPS management tasks manually, such as rebooting, reinstalling etc. They're both customer friendly and secure.

This is how I got online and happy again.

### PS

For anyone wondering what caused the security breach in the first place, let's just say: **always disable ssh password authentication**. Public keys weren't invented for sheer fun alone...


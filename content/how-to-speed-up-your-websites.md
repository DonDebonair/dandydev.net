Title: How to: Speed up your websites!
Date: 2011-09-02 22:24
Slug: how-to-speed-up-your-websites
Summary: Proud as I am of my brand-new, sexy website, I realize there's always things that can be improved. One of these things I was made aware of today by Kye, of the [Diem community](http://community.diem-project.org/ "Diem Community"): the speed of this website. Admittedly I had already noticed it was somewhat on the slow side. But only when Kye confronted me with a report from [webpagetest.org](http://www.webpagetest.org "Webpagetest"), I realized how bad it really was. So, with some tips from Kye, and some further googling, I set out to speed it up somehow. Because I think many (aspiring) web developers struggle with this problem, and because I've discovered how easy the improvements can be, I decided to share them with you all!

Proud as I am of my brand-new, sexy website, I realize there's always things that can be improved. One of these things I was made aware of today by Kye, of the [Diem community](http://community.diem-project.org/ "Diem Community"): the speed of this website. Admittedly I had already noticed it was somewhat on the slow side. But only when Kye confronted me with a report from [webpagetest.org](http://www.webpagetest.org "Webpagetest"), I realized how bad it really was. So, with some tips from Kye, and some further googling, I set out to speed it up somehow. Because I think many (aspiring) web developers struggle with this problem, and because I've discovered how easy the improvements can be, I decided to share them with you all! 

Note that information mostly applies to dynamic websites written in PHP. Also, I'm running Debian Server, so on any other linux flavor the paths to your system's config files could be different.

### Cache on the server side
First thing you should check is if you've installed a decent opcode caching addon, also know as "PHP Accelerator", for PHP. I had [APC](http://pecl.php.net/package/APC "APC") already installed, so I went with that. Other options include: [XCache](http://xcache.lighttpd.net/ "XCache") (which is developed by one of the guys behind lighttpd, so I assume it's better integrated with lighttpd than with Apache2), [eAccelerator](http://www.eaccelerator.net/ "eAccelerator") or Zend Optimizer, which is part of [Zend Server](http://www.zend.com/products/server/ "Zend Server").

So, what do these PHP Accelerators do that makes them so awesome? Well, PHP is an interpreted scripting language. As such, it needs to be parsed and compiled at runtime (when the webpage gets requested). Considering the fact that the PHP code probably doesn't change that much, it's kind of inefficient to do that for each request... especially when only parts of that code are used for those requests. That's where PHP Accelerators like APC come in. They cache the compiled code, called bytecode, so that new requests can use the already compiled code, instead of having to reinterpret and compile it all over again. To speed up things even more, the cache code doesn't get stored on disk, but in shared memory, to prevent slow diskreading. I will talk about APC here, because it's becoming the defacto standard as far as PHP Accelerators go. Starting PHP 5.4, it's going to be part of the core.

So let's get to business!

To see if APC is installed and enabled, you can run a script with the following contents on your webserver:
```php
<?php
    echo phpinfo();
?>
```
     
If APC is enabled, it should show up somewhere in the output of the script. If it isn't, you can get it [here](http://pecl.php.net/package/APC "APC"), including instructions on how to install it.
Out of the box, APC is configured with a rather small memory allowance. To change the configuration, you can either use a separate PHP configuration file for APC, or edit the standard php.ini. In a standard linux configuration, the PHP configuration files are located at: <pre>/etc/php5/</pre> There you can find the php.ini, and directory called conf.d containing additional configuration files that get loaded automatically by PHP. For a separate APC configuration file, you can find apc.ini in the conf.d, or you can make it yourself. 
You can tweak the memory allowance using two settings: apc.shm_segments and apc.shm_size. By default, apc.shm_segments is configured at 1. You can leave it at that. apc.shm_size was configured at 30 on my server, which was far too low for this website. As the framework I use (Diem), already uses around 30MB, it will overflow the cache constantly. I upped it to 128, and already the amount of hits raised to 99%, up from 97% (the amount of hits, is how many percent of the scripts is pulled from the cache).

### Client side caching
Another way of speeding up your websites, is to make use of the caching capabilities of the user's browser. The browser cache is a great way to speed up the loading of any static content on your site. I'm talking about the images, javascripts and css files for instance. To make the best use of browser caching, you must tell the browser for how long the various types of content are valid. You can do this by means of the "expires" mod for apache2. To install it, check if "expires" is available in <pre>/etc/apache2/mods-available</pre>
If it is, you can enable it (if it isn't already) by typing:
```bash
a2enmod expires
```

Now, add a .htaccess file to the root of every site you want to enable proper browser caching for, containing the following:
```apache
<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType image/gif "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType image/jpg "access plus 30 days"
  ExpiresByType image/jpeg "access plus 30 days"
  ExpiresByType image/png "access plus 30 days"
  ExpiresByType image/x-icon "access plus 30 days"
  ExpiresByType text/css "access plus 30 days"
  ExpiresByType text/javascript "access plus 30 days"
  ExpiresByType application/x-Shockwave-Flash "access plus 30 days"
</IfModule>
```

Et voilà!

### Images & Sprites!
The biggest mistake I actually made, concerning the speed of my website, is ignoring the large size of some images on my site. I did actually upload rather small PNG's to my site, but I let Diem/PHP perform resizes on them, that somehow made them 10 times as big in filesize as the originals, while being a tad smaller in dimensions than the originals. After removing the on-the-go image transformations, and resizing the PNG's manually with Photoshop, bringing the filesize down to under 90KB for each file, instead of 900KB(!) for each file, I noticed the biggest improvement in loading times yet!

Another optimalisation that can make a great difference, is to combine multiple images into one larger image, and use CSS to determine what part of the image gets shown. Not only is this technique useful for hover-images, but you can use it on any kind of image on your site, and it's especially useful for any images that are part of your site's interface design. You can find more on using sprites in [this great article](http://css-tricks.com/158-css-sprites/ "Sprites, make it right!").

Well, that was it for today's lesson. I hope you found it useful!

This blog post is of course by no means exhaustive. There are probably tons more of optimizations you can use to improve your loading speeds, so feel free to comment and tell me what other methods you use to improve your website's speed!


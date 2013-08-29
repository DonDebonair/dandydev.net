Title: Pelican Bootstrap 3 theme released
Date: 2013-08-29 22:00
Tags: pelican, bootstrap, github
Slug: pelican-bootstrap3-theme-released

Now that [Bootstrap 3](http://getbootstrap.com/) [final has been released](http://blog.getbootstrap.com/2013/08/19/bootstrap-3-released/), I've updated the Pelican theme I built for this site accordingly. The theme was already on [GitHub](https://github.com/DandyDev/pelican-bootstrap3), but now that things have stabilized, I'm officially releasing version 1.0 of _pelican-bootstrap3_! Luckily for me, [Bootswatch](http://bootswatch.com/) also updated their Bootstrap 3 compatible themes to the newest Bootstrap release. Thomas Park [graciously allowed me](https://github.com/thomaspark/bootswatch/issues/128) to include his themes in my Pelican theme, so when using _pelican-bootstrap3_, you're actually getting 12 themes in 1!

### Changes

* Updated Bootstrap 3 to new official release.
* Updated Bootswatch themes to new versions compatible with newest Bootstrap 3 release.
* Removed _Superhero_ Bootswatch theme, as it [isn't supported anymore](https://github.com/thomaspark/bootswatch/issues/132).
* Renamed `BOOTSWATCH_THEME` variable to `BOOTSTRAP_THEME` to reflect the fact that you can use it for any Boostrap 3 compatible css-theme/style.
* Fixed content scrolling over fixed navigation bar due to changed HTML structure in BS3.
* Applied nice page-header effect to Article headers.
* Made "Tags" sub-header in sidebar a clickable link.

If anyone has any feature requests, don't hesitate to leave a comment or create an issue on GitHub!





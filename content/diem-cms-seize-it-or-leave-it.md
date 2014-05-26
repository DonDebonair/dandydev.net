Title: Diem CMS: Seize it or leave it?
Date: 2012-01-07 22:53
Tags: diem, symfony, php, review, cms, cmf
Slug: diem-cms-seize-it-or-leave-it
Summary: A long, long while ago, I promised some people - including myself - a decent review of the [CMS I used to build this site](http://www.diem-project.org/ "Diem"). Of course, as it always goes, I got lost in some kind of time-sucking black hole called study-and-work. I still remember [the article](http://www.robertspeer.com/blog/apostrophenow-a-cms-so-easy-even-your-mom-could-use-it/ "Robert Speer on Apostrophe CMS") that made me choose Diem in the first place, though. His words, in an email conversation following that article he wrote: "My preference is that you try out Diem and write a review like mine with a live preview" As you can see, I did try out Diem (this site is built with it). In [my first blogpost on this site](http://dandydev.net/blog/my-new-website-is-finally-live "My First Post"), you can read in detail how the birth of this site came down. The only thing that's still missing, is that review, so I reckoned it was about time to correct that mistake.

**Update May 2014: At the time I wrote this review, this blog was still based on Diem. This is not the case anymore. For
many of the reasons mentioned in the original article, Diem was not a good fit for me and my website. In the end, I made
the switch to a static site generator, Pelican, to get rid of the hassles of an online CMS and the bad feeling that PHP
gives me :) **

A long, long while ago, I promised some people - including myself - a decent review of the [CMS I used to build this site](http://www.diem-project.org/ "Diem"). Of course, as it always goes, I got lost in some kind of time-sucking black hole called study-and-work. I still remember [the article](http://www.robertspeer.com/blog/apostrophenow-a-cms-so-easy-even-your-mom-could-use-it/ "Robert Speer on Apostrophe CMS") that made me choose Diem in the first place, though. His words, in an email conversation following that article he wrote: "My preference is that you try out Diem and write a review like mine with a live preview" As you can see, I did try out Diem (this site is built with it). In [my first blogpost on this site](http://dandydev.net/blog/my-new-website-is-finally-live "My First Post"), you can read in detail how the birth of this site came down. The only thing that's still missing, is that review, so I reckoned it was about time to correct that mistake.

Disclaimer: I want this review to appeal to as broad an audience as possible, but due to the nature of the CMS - It's a tad developer-oriented - there will be some codesnippets throughout. Feel free to skip the parts that don't interest you ;)

### The promise
Diem advertises itself as both a CMS and a CMF. CMS, as you probably know, means Content Management System. It's basically a webapplication that let's the user edit the content of their website without any knowledge of programming whatsoever. Popular examples are: [Wordpress](http://wordpress.com/ "Wordpress"), [Joomla](http://www.joomla.org/ "Joomla") and [Drupal](http://drupal.org/ "Drupal"). CMF means Content Management Framework, which is as vague a term as CMS, but in practice there's a subtle but important difference between the two. That difference is all about customizability. Still too vague? Wikipedia [tries to put a definition to it](http://en.wikipedia.org/wiki/List_of_content_management_frameworks "CMF according to Wikipedia"), but the "factual accuracy is disputed". I think the best way to explain it, is that a CMF let's you build your own CMS to the specs you want. That means you actually have to develop some stuff yourself, but the whole infrastructure for pages and media and such is already in place.

The possibilities with Diem in crafting the website you want with exactly the functionality you want, are endless, but that also means you don't get a cookiecutter prefab solution that works out of the box. It's part of what appealed to me as a developer. I want to be able build exactly what I have in mind. The fact that Diem's built on top of Symfony, makes it even more appealing to me. As we'll see later, Diem's roots in Symfony are actually found somewhat deeper underground than desired.

### Getting it to work
Installing Diem is not some trivial undertaking like it is with Wordpress. There's no nice webinstaller or even a decent sandbox. In fact, there's nothing to see at first, after you first point your webserver to the sourcefiles. You kind of have to build what you want yourself, with help of the infrastructure and building blocks Diem offers. 

Out of the box it doesn't come with any kind of working template, so I had to build one myself. Being a developer, not a designer, I chose to adjust [this existing template](http://www.priteshgupta.com/templates/elegant-press/ "Template") for my needs. I didn't know how at first, so I started reading the documentation. The Diem website features [some basic tutorials to get you started](http://www.diem-project.org/diem-5-1/doc/en/a-week-of-diem-ipsum/1-introduction "Tutorials"), including a tutorial on templating, but it isn't much. This gets me to the first annoyance I had with Diem: lack of documentation! The basic "getting started" stuff is there, but a lot of the somewhat more advanced things, you have to figure out yourself.

##### Templating
As said, Diem is a CMF and contains the infrastructure to build websites, including an admin-backend we'll talk about later. It also support all the basic building blocks to fill your pages with content, such as: Rich Text blocks, Images, Galleries etc. But first you need on or more templates. It's quite powerful when it comes to templating, after you figure it out, that is. Basically, it allows you to write the basic layout of a template in PHP. You define "Areas", and you tell Diem if an Area is part of the Layout (Global) or part of the Page (eeehm, Page-specific), like this:

```php
<div class="dm_layout">  

  <?php echo $helper->renderArea('layout.top', '.main-container') ?>  

  <div class="dm_layout_center container1">

    <div class="box">
    <?php echo $helper->renderArea('page.content', '.content') ?> 
    
    <?php echo $helper->renderArea('layout.right', '.sidebar') ?>
      <div class="clear"></div>
    </div>
  </div>

  <?php echo $helper->renderArea('layout.bottom') ?>  

</div>  
```

'layout' or 'page' here, defines the scope (global/per-page). The stuff after the dot (.) is just for naming purposes. If you put 'content' there, Diem will add some css classes when rendering that area. After setting it up like that, you just style it with CSS and you have a working website.

### Front and Admin editors
After setting up the website and templates, you want to fill it with content. This is also one of the strengths of Diem. It has two editing modes: The admin/backend, and the front editor. The first is for uploading media, managing your templates and other admin-related stuff, the latter is for actually building your content. The predefined building blocks I talked about, are available as widgets that you can drag into the areas you previously defined in your templates. The widget menu looks like this:

![widgetmenu.png]({filename}/images/widgetmenu.png)

And when you add those widgets to your site, in editing-mode, it looks like this:

![wysiwyg.png]({filename}/images/wysiwyg.png)

The "Zones" you see, are a way of dividing areas in smaller parts. You can for instance, add 2 zones, and define their width as 50% (there's a dialogbox for that), which turns an area in a 2-column area. You can then add widgets to both columns.
As said, you just drag&drop the widgets to their desired places, and you instantly see the result. Of course, with the flexibility Diem offers, you can develop widgets of your own.
In the front editor, you can also easily add new pages to your site, and add those pages to a menu. Diem takes care of all the page-related stuff in one handy dialog. Here you can add keywords, a title etc.

The design of the whole editing-experience feels outdated to my tastes, and is clearly cooked up by developers, not designers. In the admin/backend this is most apparent. Another downside is that the admin/backend feels buggy at some points. You can for instance, add Google Analytics to your site, after which some nice graphs appear on your dashboard, based on the data Diem pulled in from your GA account. Somehow Diem never seems to remember me connecting my GA account, because I have to do it again almost every time I log in. The dashboard graphs look like this, by the way:

![ga.png]({filename}/images/ga.png)

### Wow, is that AI or what?

One of the things Diem _doesn't_ have, is a blogging feature. You might find that strange, considering the fact that the most popular CMS out there, Wordpress, is basically built with blogging in mind, but as I said, Diem provides the infrastructure, the backend and the basic building blocks, everything else is up to you. Blogging is not basic according to the developers, so you have to build that yourself. Being an experienced Symfony developer, I thought that would be easy. Despite there being an example tutorial on building a blog too, it didn't turn out to be so easy after all. The fact is, that Diem puts a really thick layer on top of Symfony, that seems to obscure a lot of the API of Symfony itself. This is in contrast to the other Symfony CMS out there, [Apostrophe](http://apostrophenow.com/ "Apostrophe"), which feels like a lot "lighter" in the way it's sprinkled on top of Symfony. I'm not sure that can be avoided though, because Diem has some neat and intricate ways of taking work out of your hands, whereby some "hackery" with the Symfony way of doing things, can't be avoided. This brings me to another _coolness_ of Diem: *code generation*.

The way you build dynamic stuff to put on the pages of your website, is by just defining the model (ie. what is put into the database) and let Diem take care of the rest. Your model might look like this:

```yaml
Article:  
  actAs:  
    DmSortable:  
    I18n:  
      fields:         [ title, extract, body, is_active ]  
      actAs:  
        Timestampable:  
        DmVersionable:  
  columns:  
    title:            { type: string(120), notnull: true }  
    extract:          { type: string(2000), notnull: true }  
    body:             { type: clob, extra: markdown }  
    image:            { type: integer }  
    author:           { type: integer, notnull: true }  
    is_active:        { type: boolean, notnull: true, default: false }  
  relations:  
    Image:  
      class:          DmMedia  
      local:          image  
      foreignAlias:   Articles  
    Author:  
      class: DmUser  
      local: author  
      foreignAlias:   Articles 
```


After that, you tell Diem several things:

1. Build me an admin module to add/delete and edit blogs
2. Make a page for every article
3. Build me a widget to show the content of one article
4. Build me a widget to show a list of articles

Then you give the proper command, and Diem builds all the code for you! Of course you might have to or want to tweak the code to your liking, but it's basically all there! The admin/backend contains an Article module and the frontend editor contains widgets for a list of articles and the articles themselves. Another neat trick here, is that you have to edit only 1 article page, and all of your article pages (which Diem automatically generated) have the same edits, even though the article widget is dropped in a page-specific area. Diem knows that, because it generated the pages for the articles, those pages belong to the same model.

##### Templating, part II
When you look at the code Diem generated, you notice something strange going on. As you might know, Symfony is built on the [MVC paradigm](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller "MVC"), which aims to provide "separation of concerns". As part of that, the part where the logic of your webpages resides (controller), is separated from the part that defines how they look (view), your templates. Within normal Symfony apps (this applies to Symfony 1.4 and not so much to Symfony 2), those templates are written in HTML with some PHP in between for variables and such. Diem however, took the strange approach to obscure as much proper HTML as possible by using PHP "helper functions" to supply the HTML tags. A template might look something like this:

```php
<?php
echo _open('ol.search_results start='.$pager->getFirstIndice());

foreach($pager as $result)
{
  $page = $result->getPage();
  
  echo _tag('li.search_result',
  
    _tag('span.score', ceil(100*$result->getScore()).'%').
    
    _tag('p.result_body',
      _link($page)->text(escape($page->name))->addClass('page_name').
      dmString::truncate($result->getPageContent(), 200).' '.
      _link($page)->text('Read more')->addClass('search_read_more')
    )
  );
}

echo _close('ol');
```

To me, this feels totally unnecessary and it looks rather ugly and unreadable. Of course it's optional, but the Diem generated code makes heavy use of it. I myself, proceeded to replace most of the php helper tags by proper HTML tags. 

### The Bad & Ugly
Now that we've looked at how Diem operates, and discovered a lot of cool things about it, it's time to look at the darker side of Diem.
The way I see it, there are basically 3 things that keep Diem from being a longterm successful and viable option: Lack of documentation, lack of community and (related) lack of (future)development. I'll tackle all three of them:

#### Lack of documentation
As I mentioned before, Diem can be hard to get into, and the documentation is sparse. This can be difficult because you need to develop (with help of the code generator of course) a lot yourself. The upside is that the community has provided [a lot of plugins](http://diem-project.org/plugins "Diem Plugins") that work out of the box, with cool image galleries (one of which I developed myself!), a database-backed contact form, a comment module etc. The downside, as we will see, is that those aren't developed actively anymore, and may not provide what you need. Your only option then, is to develop plugins yourself. And let me be clear: Diem Plugins differ vastly from the [Symfony plugin standard fare](http://www.symfony-project.org/plugins/ "Symfony Plugins"). To make a widget for instance, you have to hook it up to some Diem specific code, but the documentation is not clear exactly on how exactly to do it and what the conventions are.

The normal thing to do in such case, is to ask for help in the community. This brings me to the next problem.

##### Absence of knowledgable community
The community as it stands, is comprised of just about 5 people, including myself. And to make matters worse, [none of those were part of the team that originally developed Diem](http://diem-project.org/blog/diem-is-hiring "New core team"). The original founders moved on to [greener pastures](http://symfony.com/ "Symfony2, a greener pasture"). Sadly, that makes the current Diem development team crippled at best. They too, don't know the intricacies to a lot of Diem related stuff, like plugin development or Diem development in general. This makes it all the more frustrating when you try to build something new on top of Diem, especially given the invading nature of Diem in relation to Symfony. And Diem is far to complicated to be able to quickly figure stuff out just from the source code. In comparison, Apostrophe is a lot leaner.

On top of that, the community is also rather inactive. There is a forum, which hasn't seen a new post in 2 months, and the Diem website hasn't seen an update in more than a year. There's also a largely empty wiki and a bugtracker which sees some activity, albeit not much. The only place that is still active is the Diem github repo.

##### Future development
There were plans for a next iteration of Diem (version 6), but much to my disappointment, that didn't include moving to Symfony2. Only with version 7 will Symfony2 be targeted. I feel that, although the Diem master repo at GitHub is surprisingly active at some times, the development moves at such a rate that Symfony2 will be last year's news by the time Diem arrives there. Sticking to Symfony1.4 doesn't necessarily need to be a bad thing, as long as development is active. In the case of Apostrophe, it can even be considered an artifact of their growing popularity (can't change a codebase radically which is used by so many people). I wish I had more confidence in the current Diem development team to move things to a next level, but I think they took on more than they can chew.

The best thing for Diem to do, in my opinion, is to have a good look at [Symfony CMF](http://cmf.symfony.com/ "Symfony CMF"), and build the next version (that is 6, not 7) on top of that.

### Final Verdict
Diem is a very promising CMS with some very cool and unique features. It's not the out-of-the-box CMS for your average blogger, or even for a designer with a minimal development skillset. It could however have been, a great tool for webdevelopers who want to build a website of any size with a userfriendly editor for the endusers. I am afraid however, that development and the community have regressed to a state in which they are easily overruled by the myriad of other, more developed options out there. I'm not confident Diem will get out of that state.
To developers - especially those experienced with Symfony -  looking for a CMS other than Wordpress, that they can mold to their tastes, I recommend looking at [Apostrophe](http://apostrophenow.org/ "Apostrophe"), or roll their own solution built on top of Symfony2 and the large number of [great bundles](http://knpbundles.com/ "Symfony2 Bundles") available for it.
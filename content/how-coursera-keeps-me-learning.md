Title: Coursera keeps me learning
Date: 2014-05-26 16:00
Tags: coursera, machine learning, scala, functional programming, reactive programming, rxjava, akka
Slug: coursera-keeps-me-learning

I just finished [Stanford's Machine Learning course](https://www.coursera.org/course/ml) on Coursera, taught by Andrew Ng,
and I must say, it was a blast! Not only have I learned a lot of interesting new stuff, I had a great time doing so.
And silly as it may sound, I think Andrew Ng's remark in the final video lecture - "You should now consider yourself a
Machine Learning expert" - actually rings true. The course materials were very comprehensive. The video lectures did not
lightly touch the subject matter, but got into it in real depth. This was also reflected in the review questions and
especially the programming exercises both of which you were required to pass in order to pass the course. Being somewhat
of a Big Data afficionado, I feel that my newfound skills grealy complement my (future) work with Big Data and
Hadoop-related technologies, and are a natural fit for my ambitions to become somewhat of a Data Scientist.

**Needless to say, I finished the course with a 100% score.**

I can heartily recommend this course to anyone who has an interest in (obviously) machine learning, (big) data (science),
statistics, recommender systems, fraud detections etc. It's good to realize though, that in order to finish this course
successfully you have to put in a lot of time. It's a demanding course that really requires you to focus and be able to
study well on your own. It requires discipline :)


### Addiction

The Machine Learning course was not the first Coursera course I took, and I've come to realize that I actually seem to
be addicted to this whole [MOOC](http://en.wikipedia.org/wiki/Massive_open_online_course) crazy! I think that one of my
strong qualities is that I strive to keep my self "up-to-date" by learning new technologies and teachning myself new skills
whenever I can. I would even go as far to say, it's my _Raison d'être_. These free online courses fill that need nicely.
The only problem is, that they really suck up my time, but I think it's worth it (and so far, my wife also considers it
a healthy investment of my time ;) )

Over the last year, before I took the Machine Learing class, I also did the following two courses on Coursera.

#### Functional Programming Principles in Scala

[This course](https://www.coursera.org/course/progfun) caught my interest for the following reasons:

- It teaches functional programming, which is something that was high on my to-learn list
- It teaches Scala, which was also something that was high on my to-learn list
- It is taught by Martin Odersky, the inventor of Scala. **How cool is that?!**

This is my first experience with Coursera, and it was a great one! After I finished the course, I felt I had a solid grasp
of both functional programming and Scala. Martin does a good job conveying the subject matter through the video lectures,
and the exersises are both enlightening and non-trivial, so you get a good feeling for what it's like to use Scala.
For me, it killed two birds with one stone, being functional programming and Scala. And coming from a Java-heavy workplace,
Scala fit nicely with my JVM experience, which for me, was an advantage compared to learning functional programming with
Haskell.

[I aced this course]({filename}/files/coursera-progfun-2013.pdf), and I can heartily recommend it to anyone with an interest
in functional programming and/or Scala. Even if you have a solid background in functional programming (in Haskell for
instance), but are interested in porting that knowledge to the JVM, I'd say this course fits nicely. And the other way
around is certainly true as well: give this a shot if you are proficient in Scala, but want to learn functional programming
and become aware of things like immutability and monads.

#### Principles of Reactive Programming

[This course](https://www.coursera.org/course/reactive) is the follow-up to Functional Programming Principles in Scala.
Although it isn't mentioned in the title, the focus in this course is again on Scala. This course goes beyond mere functional
programming, and dives into the world of [_Reactive Programming_](http://www.reactivemanifesto.org/). It does so by focusing
on three tools that can help you with that:

- Introducing mutable state in your functional programming in a controlled manner
- Futures and Observables. The latter being the core of the [Reactive extensions](http://msdn.microsoft.com/en-us/data/gg577609.aspx),
which is used in its JVM incarnation: [RxJava](https://github.com/Netflix/RxJava)
- The [Actor model](http://en.wikipedia.org/wiki/Actor_model), and its implementation through [Akka](http://akka.io/).

The first part is expertly taught by Martin Odersky, who also did the previous course on functional programming and Scala.
He does this in the same way he did the other course: concise and clear.

The second part is done by Erik Meijer, who invented the Reactive Extensions. While I found this subject to be the most
interesting, technology wise, I did have problems with Erik's bad english accent and his chaotic way of teaching. In the
end though, the programming exercises made everything clear to me, and _RxJava_ was wonderful to work with! I'm planning
on writing a tutorial on RxJava in the future.

The last part, about the Actor Model, was taught by Roland Kuhn, who's one of the architects behind Akka. His style of
teaching is thorough and clear, I really liked it! I think the Actor Model and Akka are great ways to simplify the burden
of concurrent programming.

[I aced this course]({filename}/files/coursera-reactive-2014.pdf), and I can really recommend it to anyone who has an
interest in learning ways to build scalable and distributed systems. Reactive programming definitely seems an answer to
many of the problems encountered in the domain of scalability and distributed systems. It's advised though, to have a solid
grasp of both functional programming and Scala, before you start this course. The previous course is a natural fit in that
regard.

### Learning more

I had a great time so far with the three Coursera courses I've done, and I will definitely be on the lookout for new courses
that can expand my skillset and knowledge. Any tips in that regard are welcome! In the meanwhile, I want to conclude this
article by mentioning another cool venture that aims to teach people: [Gibbon](https://gibbon.co/). Gibbon can be looked at
as a repository where people can collect knowledge in the form of articles, tutorials, video's etc., and organize those
in different subjects. Participants can create a "course" out of those bits of information, which other users can then
follow at their own leisure. So far, I haven't had the time to use it yet (mainly because of Coursera), but I'm certain
it will teach me stuff in the future!

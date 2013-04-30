=======
Peabody
=======

peabody is cron's best friend™

peabody is a program designed to wrap around a cron job to provide
additional functionality.

What Does it do?
================

currently peabody implements the following features:

-  timeouts

   both soft (SIGTERM) and hard (SIGKILL) timeouts are supported

-  splay functionality
-  concurrency protection with file based locking
-  logstash redis output

   push stdout and stderr from the child process into logstash's redis input as
   json_events, one per line

-  change PWD prior to executing command

on the roadmap we have:

-  configurable locking mechanisms (redis? memcache? etc? or just make
   it pluggable and you can roll your own?)

What does it NOT do
===================

-  environment munging

   peabody passes through its environment unmodified to the child
   process. If you want to do any munging on the environment, use env(1)

-  wash your dishes

   peabody will not do your dishes. I'll accept any patch which
   implements this, however.

Why should I use it?
====================

My goal with this project is to create a useful set of tools for doing
things we *all* wish cron had the ability to do by itself, and don't
feel like writing our own wrappers for, or building into our
applications directly.

How do I use it?
================

Currently, there's only one dependency, lockfile. You can install it
however you would like, though ubuntu has a package for it
(python-lockfile) if you're running ubuntu.

FIXME: usage goes here

Design goals
============

I'm still debating whether I want to make this a monolithic single
binary which does it all, or be more 'unix-like' and have it be separate
binaries, each which does its own thing and can be chained.

basically, the difference between the following two command lines:

::

    peabody -L 'gelf://10.1.1.82' -t 60 -T 90 -l /tmp/cron.lock -s 60 /usr/bin/do_something.pl

    lock /tmp/cron.lock splay 60 stash gelf://10.1.1.82 timeout 60 90 /usr/bin/do_something.pl

currently, I'm leaning toward a monolithic program, mostly because
design-wise, there could be some difficulties with the timeout function
not killing the right thing (you'd likely have to make it the *last*
command in the chain, which is a pain to have to remember) as well as
having naming conflicts with other programs on the system (timeout and
lock come to mind as having potential conflicts, which could affect
portability). Additionally, having it be monolithic means I can have a
-f option which will read in a config file making it easier to support
more complicated options (conditional output redirection comes to mind)
and making cron command lines a bit less crazy :)

and really, the single-function binary could just either be wrappers
around the monolithic binary, or, if I separated things out into
libraries a bit better, could just be calls to those library functions.
And the monolithic binary would be calls to those very same functions.

My only worry with this approach is that there would still be a lot of
duplicated work, spawning child processes, parsing arguments, etc. We
shall see, though.

anywho, I'm off to get cracking on this. It really shouldn't be that
difficult to implement most of this.

Logstash output features
========================

I intend to have peabody read from stdout and stderr and write each line
separately (and timestamped separately) to logstash.

There will be several additional bits of metadata added:

- job_id

  This will be a unique ID added to every run of peabody. This is so you can
  easily grab all of the output of the cronjob in one swoop.

- channel

  stderr/stdout. So you can grab the stderr or stdout or both or neither. Your
  choice.

- job_name

  this will be an optional field added to the logstash event so you can easily
  identify which of your jobs the output came from.

- @source_path will be ... unsure. Because cron doesn't let us know where the
  job is running from.

- process_id

  this will be the pid of peabody's child process, separate from job_id. Just
  in case you have some other logs which might mention that pid.

Where can I learn more?
=======================

-  github: https://github.com/GorillaNation/peabody


.. vim: ft=rst:

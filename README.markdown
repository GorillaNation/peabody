# wtf is it?
cronstash is a program designed to wrap around a cron job to provide
additional functionality.

# wtf does it do?

currently cronstash implements the following features:

* timeouts

	both soft (SIGTERM) and hard (SIGKILL) timeouts are supported

* splay functionality
* concurrency protection with file based locking

on the roadmap we have:

* configurable output capture and redirection

	additionally, with this, I'll probably have it able to use a number of
	backends for the lock. like redis, file, mutex? whatev. some shit

* configurable locking mechanisms (redis? memcache? etc? or just make it pluggable and you can roll your own?)


# why should I use it?

My goal with this project is to create a useful set of tools for doing things we *all*
wish cron had the ability to do by itself, and don't feel like writing our own wrappers
for, or building into our applications directly. 

# design goals

I'm still debating whether I want to make this a monolithic single binary which does
it all, or be more 'unix-like' and have it be separate binaries, each which does
its own thing and can be chained.

basically, the difference between the following two command lines:

	cronstash -L 'gelf://10.1.1.82' -t 60 -T 90 -l /tmp/cron.lock -s 60 /usr/bin/do_something.pl

	splay 60 stash gelf://10.1.1.82 lock /tmp/cron.lock timeout 60 90 /usr/bin/do_something.pl

currently, I'm leaning toward a monolithic program, mostly because design-wise, there
could be some difficulties with the timeout function not killing the right thing (you'd
likely have to make it the *last* command in the chain, which is a pain to have to remember)
as well as having naming conflicts with other programs on the system (timeout and lock
come to mind as having potential conflicts, which could affect portability). Additionally,
having it be monolithic means I can have a -f option which will read in a config file making
it easier to support more complicated options (conditional output redirection comes to mind)
and making cron command lines a bit less crazy :)

anywho, I'm off to get cracking on this. It really shouldn't be that difficult to implement most
of this.

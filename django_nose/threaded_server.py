import thread
from django.core.management import call_command

class ThreadedServer(object):

    def __init__(self):
        pass

    def start(self):
        self.thread = thread.start_new_thread(call_command, ('runserver',), {'use_reloader':False})

    def stop(self):
        pass

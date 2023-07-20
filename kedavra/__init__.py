from .core.c2 import c2
from .core.client import Client
from .utils import compile_script, generate_random_id

from .listen import socket

listeners = {
    'socket' : socket
}
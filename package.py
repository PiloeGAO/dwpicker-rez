name = "dwpicker"

version = "1.0.3"

authors = [
    "Dreamwall Animation",
    "Léo Depoix",
]

description = \
    """
    Animation picker for Maya.
    """

requires = [
    "~python-3",
    "maya-2025+",
]

uuid = "dreamwall.dwpicker"

build_command = "python {root}/build.py {install}"

def commands():
    env.PYTHONPATH.append("{root}/python")

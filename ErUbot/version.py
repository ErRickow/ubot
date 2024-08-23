from subprocess import run



__pversion__ = "`@main`."
__version_code__ = (
    run(["git", "rev-list", "--count", "HEAD"], capture_output=True)
    .stdout.decode()
    .strip()
    or "0"
)

__version__ = __pversion__ + __version_code__

ubot_version = __version__



from sys import version_info



branch = f"@main"


__Tgl__ = "24"
__Bln__ = "08"
__Thn__ = "2024"


__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__license__ = "MIT"
__author__ = "Er Userbot <https://github.com/ErRickow/ubot>"
__copyright__ = "Er Userbot Copyright (©) 2024" + __author__


versi = f"{__Tgl__}.{__Bln__}.{__Thn__}"


from invoke import task, Exit
from fabric2 import Connection
from fabric2.transfer import Transfer
from patchwork.files import append

from ..fedora import install


@task
def all(c):
    nano(c)
    neovim(c)
    android_studio(c)
    vscode(c)
    okular(c)
    texstudio()
    svn(c)
    discord(c)
    nvidia(c)
    steam(c)
    qutebrowser(c)
    nodejs(c)
    xonotic(c)
    supertuxkart(c)
    rpmfusion(c)
    ffmpeg(c)
    nvidia(c)
    htop(c)


@task
def nano(c):
    install(c,'nano')


@task
def htop(c):
    install(c,'htop')


@task
def neovim(c):
    install(c,'neovim python-neovim python3-neovim')


@task
def android_studio(c):
    version = '3.0.1.0'
    release = 'android-studio-ide-171.4443003-linux.zip'

    c.install(c,'qemu-kvm android-tools libstdc++.i686 zlib.i686')

    c.run('wget https://dl.google.com/dl/android/studio/ide-zips/{}/{}'
        .format(version, release))
    c.sudo('unzip -q {} -d /opt/'.format(release))
    c.run('rm -r {}'.format(release))

    append('/usr/local/share/applications/android-studio.desktop',
           '[Desktop Entry]'
           '\nType=Application'
           '\nName=Android Studio'
           '\nIcon=/opt/android-studio/bin/studio.png'
           '\nExec=env _JAVA_OPTIONS=-Djava.io.tmpdir=/var/tmp'
           '/opt/android-studio/bin/studio.sh'
           '\nTerminal=false'
           '\nCategories=Development;IDE;', use_sudo=True)


@task
def vscode(c):
    c.sudo('rpm --import https://packages.microsoft.com/keys/microsoft.asc')

    append('/etc/yum.repos.d/vscode.repo', '[code]\nname=Visual Studio Code'
           '\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\n'
           'enabled=1\ngpgcheck=1'
           '\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc',
           use_sudo=True)

    install(c,'code')
    install(c,'mono-devel')

    c.sudo('dnf copr -y enable @dotnet-sig/dotnet')

    install(c,'dotnet-sdk-2.0')
    install(c,'dotnet-runtime-2.0')


@task
def okular(c):
    install(c,'okular')


@task
def texstudio(c):
    install(c,'texlive-scheme-full texstudio')


@task
def svn(c):
    install(c,'svn')


@task
def discord(c):
    c.sudo('dnf copr -y enable tcg/discord')
    install(c,'Discord-installer')
    sudo('systemctl enable discord-installer')
    sudo('systemctl start discord-installer')


@task
def rpmfusion(c):
    install(c,'https://download1.rpmfusion.org/free/fedora/'
            'rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm '
            'https://download1.rpmfusion.org/nonfree/fedora/'
            'rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm')


@task
def ffmpeg(c):
    install(c,'ffmpeg')


@task
def nvidia(c):
    c.sudo('dnf config-manager --add-repo='
         'https://negativo17.org/repos/'
         'fedora-nvidia.repo')
    install(c,'nvidia-settings kernel-devel dkms-nvidia vulkan.i686 '
            'nvidia-driver-libs.i686')



@task
def qutebrowser(c):
    install(c,'qutebrowser')


@task
def nodejs(c):
    install(c,'nodejs')
#
# Games
#
@task
def steam(c):
    c.sudo('dnf config-manager --add-repo=https://negativo17.org/repos/fedora-steam.repo')
    install(c,'steam')


@task
def xonotic(c):
    install(c,'xonotic')


@task
def supertuxkart(c):
    install(c,'supertuxkart')

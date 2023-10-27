# Docker与容器

## 什么是Docker？

Docker是基于Go语言的一种管理应用生命周期的容器技术，是一种轻量级的虚拟化技术，被充分应用于云平台中。

## Docker的优势

虚拟化的核心是对计算机实体资源的抽象，目标是在一个主机上同时运行多个系统或应用。容器相关技术使用的虚拟化层次是基于操作系统级虚拟化 ：内核通过创建多个虚拟的操作系统实例（内核和库）来隔离不同的进程 。

传统方式是在硬件层面实现虚拟化，需要有额外的虚拟机管理应用和虚拟机操作系统 层。 Docker容器是在操作系统层面上实现虚拟化，直接复用本地主机的操作系统，因此更加 轻量级 。

# Docker核心概念

Docker 大部分的操作都围绕着它的三大核心概念 : 镜像、容器、仓库

## Docker镜像

操作系统分为 **内核** 和 **用户空间**。对于 `Linux` 而言，内核启动后，会挂载 `root` 文件系统为其提供用户空间支持。而 **Docker 镜像**（`Image`），就相当于是一个 `root` 文件系统。

**Docker 镜像** 是一个特殊的文件系统，除了提供容器运行时所需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数（如匿名卷、环境变量、用户等）。镜像 **不包含** 任何动态数据，其内容在构建之后也不会被改变。

### 分层存储

因为镜像包含操作系统完整的 `root` 文件系统，其体积往往是庞大的。在 Docker 设计时，就将其设计为分层存储的架构。所以严格来说，镜像只是一个虚拟的概念，其实际体现并非由一个文件组成，而是由一组文件系统组成，或者说，由多层文件系统联合组成。

镜像构建时，会一层层构建，前一层是后一层的基础。每一层构建完就不会再发生改变，后一层上的任何改变只发生在自己这一层。因此，在构建镜像的时候，需要额外小心，每一层尽量只包含该层需要添加的东西，任何额外的东西应该在该层构建结束前清理掉。

分层存储的特征还使得镜像的复用、定制变的更为容易。甚至可以用之前构建好的镜像作为基础层，然后进一步添加新的层，以定制自己所需的内容，构建新的镜像。

## Docker容器

镜像（`Image`）和容器（`Container`）的关系，就像是面向对象程序设计中的 `类` 和 `实例` 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。

容器的实质是进程，但与直接在宿主执行的进程不同，容器进程运行于属于自己的独立的 [命名空间](https://en.wikipedia.org/wiki/Linux_namespaces)。因此容器可以拥有自己的 `root` 文件系统、自己的网络配置、自己的进程空间，甚至自己的用户 ID 空间。容器内的进程是运行在一个隔离的环境里，使用起来，就好像是在一个独立于宿主的系统下操作一样。这种特性使得容器封装的应用比直接在宿主运行更加安全。

每一个容器运行时，是以镜像为基础层，在其上创建一个当前容器的存储层，我们可以称这个为容器运行时读写而准备的存储层为**容器存储层**。容器存储层的生存周期和容器一样，容器消亡时，容器存储层也随之消亡。因此，任何保存于容器存储层的信息都会随容器删除而丢失。

按照 Docker 最佳实践的要求，容器不应该向其存储层内写入任何数据，容器存储层要保持无状态化。所有的文件写入操作，都应该使用 [数据卷（Volume）]()、或者 [绑定宿主目录]()，在这些位置的读写会跳过容器存储层，直接对宿主（或网络存储）发生读写，其性能和稳定性更高。

数据卷的生存周期独立于容器，容器消亡，数据卷不会消亡。因此，使用数据卷后，容器删除或者重新运行之后，数据却不会丢失。

## Docker仓库

镜像构建完成后，可以很容易的在当前宿主机上运行，但是，如果需要在其它服务器上使用这个镜像，我们就需要一个集中的存储、分发镜像的服务，[Docker Registry]() 就是这样的服务。

## Docker安装

请参考[官方文档](https://docs.docker.com/desktop/install/linux-install/)。

# 使用Docker镜像

## 获取镜像



从 Docker 镜像仓库获取镜像的命令是 `docker pull`。其命令格式为：

```bash
$ docker pull [选项] [Docker Registry 地址[:端口号]/]仓库名[:标签]
```

Docker 镜像仓库地址：地址的格式一般是 `<域名/IP>[:端口号]`。默认地址是 Docker Hub(`docker.io`)。

`docker pull ubuntu:18.04`命令相当于`docker pull registry.hub.docker.com/ubuntu:18.04`命令。严格地讲，镜像的仓库名称中还应该添加仓库地址（即registry,，注册服务器）作为前缀 ，只是默认使用的是官方DockerHub服务 ，该前缀可以忽略。

仓库名：如之前所说，这里的仓库名是两段式名称，即 `<用户名>/<软件名>`。对于 Docker Hub，如果不给出用户名，则默认为 `library`，也就是官方镜像。

从下载过程中可以看到我们之前提及的分层存储的概念，镜像是由多层存储所构成。下载也是一层层的去下载，并非单一文件。下载过程中给出了每一层的 ID 的前 12 位。并且下载结束后，给出该镜像完整的 `sha256` 的摘要，以确保下载一致性。

## 列出镜像

要想列出已经下载下来的镜像，可以使用 `docker image ls` 命令。

 ```bash
 REPOSITORY                               TAG       IMAGE ID       CREATED       SIZE
 nginx                                    latest    eb4a57159180   2 weeks ago   187MB
 ambassador/telepresence-docker-runtime   1.0.9     3a0d378b0ab9   2 weeks ago   21.3MB
 ubuntu                                   18.04     f9a80a55f492   4 weeks ago   63.2MB
 ```

列表包含了 `仓库名`、`标签`、`镜像 ID`、`创建时间` 以及 `所占用的空间`。**镜像 ID** 是镜像的唯一标识，一个镜像可以对应多个 **标签**。

### 镜像体积

Docker Hub 中显示的体积是压缩后的体积（在镜像下载和上传过程中镜像是保持着压缩状态）， `docker image ls` 显示的是镜像下载到本地后本地磁盘空间占用的大小。

`docker image ls` 列表中的镜像体积总和并非是所有镜像实际硬盘消耗。由于 Docker 镜像是多层存储结构，并且可以继承、复用，因此不同镜像可能会因为使用相同的基础镜像，从而拥有共同的层。

可以通过 `docker system df` 命令来便捷的查看镜像、容器、数据卷所占用的空间。

```bash
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          3         1         271.3MB   250MB (92%)
Containers      1         1         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B
```

### 中间层镜像

为了加速镜像构建、重复利用资源，Docker 会利用 **中间层镜像**。所以在使用一段时间后，可能会看到一些依赖的中间层镜像。默认的 `docker image ls` 列表中只会显示顶层镜像，如果希望显示包括中间层镜像在内的所有镜像的话，需要加 `-a` 参数。

```bash
docker image ls -a
```

## 搜索镜像

利用`docker search`命令可以搜多Docker Hub仓库中的镜像。语法为：

```bash
# docker search --help

Usage:  docker search [OPTIONS] TERM

Search the Docker Hub for images

Options:
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print search using a Go template
      --limit int       Max number of search results (default 25)
      --no-trunc        Don't truncate output

```

可以搜索Docker Hub仓库中的官方提供的带nginx的镜像：

```bash
# docker search --filter=is-official=true nginx
NAME      DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
nginx     Official build of Nginx.                        18712     [OK]       
unit      Official build of NGINX Unit: Universal Web …   6         [OK]
```

## 删除本地镜像

如果要删除本地的镜像，可以使用 `docker image rm` 命令，其格式为：

```bash
docker image rm [选项] <镜像1> [<镜像2> ...]
```

其中，`<镜像>` 可以是 `镜像短 ID`、`镜像长 ID`、`镜像名` 或者 `镜像摘要`。

比如我们有这么一些镜像：

```bash
$ docker image ls

REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE

centos                      latest              0584b3d2cf6d        3 weeks ago         196.5 MB

redis                       alpine              501ad78535f0        3 weeks ago         21.03 MB

docker                      latest              cf693ec9b5c7        3 weeks ago         105.1 MB

nginx                       latest              e43d811ce2f4        5 weeks ago         181.5 MB
```

我们可以用镜像的完整 ID，也称为 `长 ID`来删除镜像。`docker image ls` 默认列出的是短 ID ，一般取前3个字符以上，只要足够区分于别的镜像就可以了。

### Untagged 和 Deleted

删除行为分为两类，一类是 `Untagged`，另一类是 `Deleted`。我们之前介绍过，镜像的唯一标识是其 ID 和摘要，而一个镜像可以有多个标签。我们可以通过Python中对象的引用来理解它们之间的区别。

1. 如果有其它标签指向我们删除的镜像，那么Delete行为不会发生。
2. 如果当前镜像的某一层正在被其它镜像依赖，那么Delete行为不会发生。
3. 如果该镜像启动的容器存在（不论是否在运行中），那么Delete行为不会发生，这是因为容器会在镜像之上构建一层存储层，显然是在依赖当前镜像的。

当我们使用上面命令删除镜像的时候，实际上是在要求删除某个标签的镜像。所以首先需要做的是将满足我们要求的所有镜像标签都取消，这就是我们看到的 `Untagged` 的信息。因为一个镜像可以对应多个标签，因此当我们删除了所指定的标签后，可能还有别的标签指向了这个镜像，如果是这种情况，那么 `Delete` 行为就不会发生。所以并非所有的 `docker image rm` 都会产生删除镜像的行为，有可能仅仅是取消了某个标签而已。

当该镜像所有的标签都被取消了，该镜像很可能会失去了存在的意义，因此会触发删除行为。镜像是多层存储结构，因此在删除的时候也是从上层向基础层方向依次进行判断删除。镜像的多层结构让镜像复用变得非常容易，因此很有可能某个其它镜像正依赖于当前镜像的某一层。这种情况，依旧不会触发删除该层的行为。直到没有任何层依赖当前层时，才会真实的删除当前层。这就是为什么，有时候会奇怪，为什么明明没有别的标签指向这个镜像，但是它还是存在的原因，也是为什么有时候会发现所删除的层数和自己 `docker pull` 看到的层数不一样的原因。

除了镜像依赖以外，还需要注意的是容器对镜像的依赖。如果有用这个镜像启动的容器存在（即使容器没有运行），那么同样不可以删除这个镜像。之前讲过，容器是以镜像为基础，再加一层容器存储层，组成这样的多层存储结构去运行的。因此该镜像如果被这个容器所依赖的，那么删除必然会导致故障。如果这些容器是不需要的，应该先将它们删除，然后再来删除镜像。

## 使用Docker commit构成新的镜像以及为什么不这样做的原因

#### 制作新的镜像

```bsah
docker pull nginx:latest
docker run --name webserver -d -p 80:80 nginx
```

这条命令会用 `nginx` 镜像启动一个容器，命名为 `webserver`，并且映射了 80 端口，这样我们可以用浏览器去访问这个 `nginx` 服务器。

如果是在本机运行的 Docker，那么可以直接访问：`http://localhost` ，如果是在虚拟机、云服务器上安装的 Docker，则需要将 `localhost` 换为虚拟机地址或者实际云服务器地址。

![docker_commit_1](/Users/zhangyanguo/Desktop/Docker技术入门与实战/docker_commit_1.webp)

我们可以使用 `docker exec` 命令进入容器，修改其内容。

```bash
% docker exec -it webserver bash
root@1d62b3bb2cc3:/# echo '<h1>Hello, Docker!</h1>' > /usr/share/nginx/html/index.html
root@1d62b3bb2cc3:/# exit
exit
```

> `-i, --interactive` 参数用于保持 STDIN 开启以实现交互性，`-t, --tty` 参数用于分配一个伪终端以提供更好的终端体验。

刷新网页我们可以看到：

![docker_commit_2](/Users/zhangyanguo/Desktop/Docker技术入门与实战/docker_commit_2.webp)

我们修改了容器的文件，也就是改动了容器的存储层。我们可以通过 `docker diff` 命令看到具体的改动。

```bash
% docker diff webserver
C /root
A /root/.bash_history
C /etc
C /etc/nginx
C /etc/nginx/conf.d
C /etc/nginx/conf.d/default.conf
C /usr
C /usr/share
C /usr/share/nginx
C /usr/share/nginx/html
C /usr/share/nginx/html/index.html
C /run
A /run/nginx.pid
C /var
C /var/cache
C /var/cache/nginx
A /var/cache/nginx/client_temp
A /var/cache/nginx/fastcgi_temp
A /var/cache/nginx/proxy_temp
A /var/cache/nginx/scgi_temp
A /var/cache/nginx/uwsgi_temp
```

当我们运行一个容器的时候（如果不使用卷的话），我们做的任何文件修改都会被记录于容器存储层里。而 Docker 提供了一个 `docker commit` 命令，可以将容器的存储层保存下来成为镜像。换句话说，就是在原有镜像的基础上，再叠加上容器的存储层，并构成新的镜像。以后我们运行这个新镜像的时候，就会拥有原有容器最后的文件变化。

```bash
% docker commit \
    --author "huiti" \                         
    --message "修改了默认网页" \
    webserver \
    nginx:v2
sha256:25bc5704c8858f79ff99dae82c02aa932b6463d9a5880cec2dd67e8fb218fb44
```

> `docker commit`: 这是 Docker 命令的一部分，用于创建一个新的镜像。
>
> `--author "huiti"`: 这是 `docker commit` 命令的选项之一，用于指定作者的信息。在这个示例中，作者被设置为 "huiti"。
>
> `--message "修改了默认网页"`: 这是 `docker commit` 命令的选项之一，用于指定提交的信息或注释。在这个示例中，提交信息被设置为 "修改了默认网页"。
>
> `webserver`: 这是要提交的容器的名称或容器ID。在这个示例中，使用名为 `webserver` 的容器。
>
> `nginx:v2`: 这是要创建的新镜像的名称和标签。在这个示例中，新镜像被命名为 `nginx`，标签为 `v2`。

这个命令的作用是将名为 `webserver` 的容器创建为一个新的镜像，并命名为 `nginx:v2`，其中包含了作者信息和提交信息。

```bash
% docker image ls
REPOSITORY                               TAG       IMAGE ID       CREATED         SIZE
nginx                                    v2        25bc5704c885   3 minutes ago   187MB
nginx                                    latest    eb4a57159180   2 weeks ago     187MB
```

我们就可以看到这个新定制的镜像

用 `docker history` 具体查看镜像内的历史记录，如果比较 `nginx:latest` 的历史记录，我们会发现新增了我们刚刚提交的这一层。

```bash
% docker history nginx:v2
IMAGE          CREATED         CREATED BY                                       SIZE      COMMENT
25bc5704c885   4 minutes ago   nginx -g daemon off;                             1.19kB    修改了默认网页
eb4a57159180   2 weeks ago     /bin/sh -c #(nop)  CMD ["nginx" "-g" "daemon…   0B        

```

新的镜像定制好后，我们可以来运行这个镜像。

```bash
docker run --name web2 -d -p 81:80 nginx:v2
```

访问 `http://localhost:81` 看到结果，其内容应该和之前修改后的 `webserver` 一样。

#### 为什么不要使用docker commit去制作新的镜像

仔细观察之前的 `docker diff webserver` 的结果，你会发现除了真正想要修改的 `/usr/share/nginx/html/index.html` 文件外，由于命令的执行，还有很多文件被改动或添加了。这还仅仅是最简单的操作，如果是安装软件包、编译构建，那会有大量的无关内容被添加进来，将会导致镜像极为臃肿。

此外，使用 `docker commit` 意味着所有对镜像的操作都是黑箱操作，生成的镜像也被称为 **黑箱镜像**，换句话说，就是除了制作镜像的人知道执行过什么命令、怎么生成的镜像，别人根本无从得知。而且，即使是这个制作镜像的人，过一段时间后也无法记清具体的操作。这种黑箱镜像的维护工作是非常痛苦的。

而且，回顾之前提及的镜像所使用的分层存储的概念，除当前层外，之前的每一层都是不会发生改变的，换句话说，任何修改的结果仅仅是在当前层进行标记、添加、修改，而不会改动上一层。如果使用 `docker commit` 制作镜像，以及后期修改的话，每一次修改都会让镜像更加臃肿一次，所删除的上一层的东西并不会丢失，会一直如影随形的跟着这个镜像，即使根本无法访问到。这会让镜像更加臃肿。

## 使用Dockerfile定制镜像

镜像的定制实际上就是定制每一层所添加的配置、文件。如果我们可以把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像，那么之前提及的无法重复的问题、镜像构建透明性的问题、体积的问题就都会解决。这个脚本就是 Dockerfile。

# 容器健康检查

对于容器而言最简单的健康检查是进程级别的，即检验进程是否存活。

在docker中发现一个容器的状态是`unhealthy`，于是可以使用指令：

```bash
docker inspect --format='{{json .State.Health}}' c61
```

得到输出

```bash
{"Status":"unhealthy","FailingStreak":21411681,"Log":[{"Start":"2023-07-05T20:47:51.691504384+08:00","End":"2023-07-05T20:47:51.746711749+08:00","ExitCode":1,"Output":"supervisord not running.\n"},{"Start":"2023-07-05T20:47:52.794689735+08:00","End":"2023-07-05T20:47:52.845807107+08:00","ExitCode":1,"Output":"supervisord not running.\n"},{"Start":"2023-07-05T20:47:53.857946228+08:00","End":"2023-07-05T20:47:53.913152284+08:00","ExitCode":1,"Output":"supervisord not running.\n"},{"Start":"2023-07-05T20:47:54.924209798+08:00","End":"2023-07-05T20:47:54.978462509+08:00","ExitCode":1,"Output":"supervisord not running.\n"},{"Start":"2023-07-05T20:47:55.989864877+08:00","End":"2023-07-05T20:47:56.047939582+08:00","ExitCode":1,"Output":"supervisord not running.\n"}]}
```

这段代码是一个状态报告，描述了系统的健康状态和相关日志信息。以下是对其中各个字段的解释：

- **Status**: 系统的状态，此处为"unhealthy"表示系统当前处于不健康状态。

- **FailingStreak**: 持续发生错误的次数，此处为21410176，表示系统连续出现错误的次数。

- Log

  : 记录了一系列事件的日志信息列表。

  - **Start**: 事件开始时间，采用ISO 8601格式表示。
  - **End**: 事件结束时间，采用ISO 8601格式表示。
  - **ExitCode**: 事件的退出码，此处为1，通常表示发生了某种错误。
  - **Output**: 事件的输出消息，此处为"supervisord not running.\n"，表示 supervisord 进程未运行。

> Supervisor和supervisord是两个不同的软件，但它们之间存在一定的关系。
>
> Supervisor是一个进程管理工具，用于监控和控制在Unix-like操作系统上运行的进程。它可以启动、停止、重启以及自动监控进程的状态，并提供了命令行界面和Web界面来管理这些进程。
>
> Supervisord是Supervisor的一个守护进程版本。守护进程是在后台运行的特殊程序，负责启动、停止和管理其他进程。Supervisord作为一个守护进程，会在系统启动时自动运行，并始终在后台运行，确保被监控的进程始终处于活动状态。

`supervisord` 是一个进程控制系统，用于管理和监控其他进程。这里显然是容器中的`supervisord` 服务未能正常进行，可以进入容器中排查问题。

```bash
# supervisord --version
3.3.5
```

显示supervisord是安装了的。

```bash
# ps aux | grep supervisord
root     4161894  0.0  0.0  12364   980 pts/13   S+   21:00   0:00 grep --color=auto supervisord
```

显示supervisord进程没有启动，接下来我们尝试启动该服务。

```bash
# supervisord 
/usr/lib/python2.7/site-packages/supervisor-3.3.5-py2.7.egg/supervisor/options.py:461: UserWarning: Supervisord is running as root and it is searching for its configuration file in default locations (including its current working directory); you probably want to specify a "-c" argument specifying an absolute path to a configuration file for improved security.
  'Supervisord is running as root and it is searching '
```

这是来自supervisor的警告消息。它建议以root权限运行的Supervisord指定一个绝对路径的配置文件，以提高安全性。

```bash
# ps aux | grep super
root     4162595  0.2  0.0 115928 11752 ?        Ss   21:02   0:01 /usr/bin/python /usr/bin/supervisord
root     4170227  0.0  0.0  12368   976 pts/13   S+   21:12   0:00 grep --color=auto super
```

显示supervisord正常启动了，再查看容器的健康状况则为healthy。
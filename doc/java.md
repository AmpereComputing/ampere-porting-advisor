# Java on Ampere Processors

Java is a programming language which powering a large share of today’s digital world, from embedded devices to data centers. Because Java is a general-purpose object-oriented language that is designed to Write Once Run Anywhere, it relies on a platform-dependent Java Virtual Machine (JVM) to translate bytecodes into machine code that is specific to the architecture on which the application runs. Visit _[Wikipedia](https://en.wikipedia.org/wiki/Java_(programming_language))_ to get more info about Java.

OpenJDK is the official reference JVM implementation. OpenJDK is Free Open-Source Software (FOSS), is used by most Java developers, and is the default JVM for most Linux distributions. The AArch64 port has been part of the OpenJDK project _[for a while now](https://developers.redhat.com/blog/2021/02/01/how-red-hat-ported-openjdk-to-64-bit-arm-a-community-history#)_. Today, OpenJDK is well-supported on AArch64 from Java Development Kit 8 (JDK8) onwards.

### Prebuilt Java release
OpenJDK binaries for Ampere Altra Family processors are available from several sources. Linux distributions make OpenJDK available through their respective package repositories. _[Adoptium](https://adoptium.net/temurin/releases/)_ is another source for prebuilt OpenJDK AArch64 binaries.

OpenJDK has many release versions but only the versions listed in following Table have the LTS release qualifier. Different OpenJDK distributions may provide End of Life (EOL) dates as shown blow:

|                | FIRST AVAILABILITY | END OF AVAILABILITY |
| :------------: |:------------------:| :------------------:|
| Java 8 (LTS)   | Mar 2014           | Nov 2026            |
| Java 11 (LTS)  | Sep 2018           | Oct 2024            |
| Java 17 (LTS)  | Sep 2021           | Oct 2027            |

### Building custom OpenJDK
For custom OpenJDK builds, GCC is recommended for building OpenJDK from _[source code](https://github.com/openjdk/jdk)_. Different GCC versions have different AArch64 options as shown in following Table:

|  GCC VERSION   | OPTIONS            | DESCRIPTION         |
| :------------: |:------------------:| :------------------:|
| >=10.1         | -moutline-atomics  | Detect atomic instructions at run time; Large System Extensions (LSE) atomic instructions are generated if the processor supports them; Enabled by default |
| >=8.4          | -mcpu=neoverse-n1  | Generate optimized code for Ampere Altra Family processors; LSE atomic instructions are generated |
| >=8.1          | march=armv8.2-a    | Generate optimized code for armv8.2-a ISA; LSE atomic instructions are generated | 

These configurations and options are used to build OpenJDK:
```shell
bash configure --with-alsa=/usr --with-alsa-lib=/usr/lib64 --with-cacerts-file=/etc/pki/java/cacerts --with-cups=/usr --with-debug-level=release --with-native-debug-symbols=none --with-extra-cflags="-pipe -fPIC -DPIC -Wl,-rpath=/usr/lib64 -L/usr/lib64 -mcpu=neoverse-n1" --with-extra-cxxflags="-pipe -fPIC -DPIC -Wl,-rpath=/usr/lib64 -L/usr/lib64 -mcpu=neoverse-n1" --with-extra-ldflags="-Wl,-rpath=/usr/lib64 -L/usr/lib64" --with-stdc++lib=dynamic --with-target-bits=64 --with-zlib=system --x-includes=/usr/include --x-libraries=/usr/lib64 --with-boot-jdk=<jdk-home-directory> --prefix=<jdk-install-directory> 
make images 
make install
```

### Building JAR libraries manually
Some JARs leveraged _[JNI](https://en.wikipedia.org/wiki/Java_Native_Interface)_ enables programmers to write native methods to handle situations when an application cannot be written entirely in the Java programming language. It allows standard Java class library to support the platform-specific features or boost performance on specific platforms, and it's important to build these library on AArch64 to get best functionality and performance on Ampere Processors.

To check JARs contains native shared objects:
`for FILE in *; do OUT=$(echo "$FILE:" && jar tf $FILE | grep -Pv '^META-INF/|(\.class|/)$' | grep '\.so') && echo $OUT; done`

For those JARs without AArch64 native shared objects, we can re-compile JARs by Maven on a Ampere platform or cross-compile on a x86 platform.

For example, on an Ampere processor based Ubuntu Linux, type the following to install and check the native toolchain:
```shell
sudo apt-get install gcc
gcc -v
```
To install and check cross-toolchain, take Ubuntu Linux on x86 as an example:
```shell
sudo apt-get install gcc-aarch64-linux-gnu
aarch64-linux-gnu-gcc -v
```

Next, check `native-maven-plugin` has set right toolchain for compiler and linker for building artifacts for AArch64. 
To build AArch64 artifacts on a native Ampere platform:
```shell
<compilerExecutable>gcc</compilerExecutable>
<linkerExecutable>gcc</linkerExecutable>
```
To cross-build AArch64 artifacts on a x86 platform:
```shell
<compilerExecutable>aarch64-linux-gnu-gcc</compilerExecutable>
linux-gnu-gcc</linkerExecutable>
```
Then start building artifacts by:
```shell
mvn compile
```
The _[Java on Arm](https://blogs.oracle.com/javamagazine/post/java-arm64-aarch64-development)_ also showcase benefits brought by native build.

### Unlocking Java performance
Furthermore, Java performance can be unlocked by custom OpenJDK builds, system configurations, common OpenJDK options and AArch64-specific OpenJDK options. Visit _[Unlocking Java Performance Tuning Guide](https://amperecomputing.com/tuning-guides/unlocking-java-performance-tuning-guide)_ for more information.

Ampere-Ready Assessor for Java
====================================

This is a fork of [AWS Graviton-Ready Assessor](https://github.com/aws/porting-advisor-for-graviton/tree/main/src/advisor/tools/graviton-ready-java), an open source Java application contributed by [Michael Fischer](https://github.com/otterley). This fork has updated terminologies to Ampere equivalents.

This application can help you determine whether your Java application is ready
to run on bare-metal or VM instances powered by Ampere Processors. More
information about Ampere Cloud Native Processors can be found
[here](https://amperecomputing.com/products/processors).

Many Java applications are ready to run on Ampere Processors without modification. In
particular, pure Java applications that do not use Java Native Interface (JNI)
will often run seamlessly with no changes at all. Many third-party and Open
Source applications that have native libraries will also run without
modification, if they ship with those native libraries for the aarch64
architecture on Linux.

To determine whether your application is ready to run on Ampere Processors, simply run
this application and point it at your JAR or WAR file, or a folder that contains
your JAR and/or WAR files. If your application is "clean" (i.e., it has no
native libraries, or all native libraries are available for aarch64 on Linux),
it will tell you. If there are native libraries missing, it will try to inform
you of the actions you can take to make your application or its dependencies
compatible with Ampere Processors.

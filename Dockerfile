FROM ubuntu:22.04 as builder

RUN apt update \
    && apt install -y python3.11 python3.11-dev python3.11-venv python3-pip openjdk-17-jdk maven binutils \
    && apt clean

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV MAVEN_HOME=/usr/share/maven

COPY . /root/
SHELL ["/bin/bash", "-c"]
RUN cd /root/ && /usr/bin/python3.11 -m venv .venv \
    && source .venv/bin/activate \
    && python3 -m pip install -r requirements-build.txt \
    && FILE_NAME=porting-advisor ./build.sh

RUN mv /root/dist/porting-advisor /opt/porting-advisor

# Use dry ubuntu 22.04 as runtime
FROM ubuntu:22.04 as runtime
COPY --from=builder /opt/porting-advisor /usr/bin/porting-advisor
ENTRYPOINT ["/usr/bin/porting-advisor"]

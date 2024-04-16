FROM ubuntu:22.04 as builder

RUN apt update \
    && apt install -y python3.11 python3.11-dev python3.11-venv python3-pip openjdk-11-jdk maven binutils \
    && apt clean

ENV MAVEN_HOME=/usr/share/maven

COPY src src/
COPY build.sh setup-environment.sh getBinaryName.sh requirements-build.txt ./
SHELL ["/bin/bash", "-c"]
RUN /usr/bin/python3.11 -m venv .venv \
    && source .venv/bin/activate \
    && python3 -m pip install -r requirements-build.txt \
    && FILE_NAME=porting-advisor ./build.sh

RUN mv dist/porting-advisor /opt/porting-advisor

# Use Eclipse Temurin JRE 17 as runtime
FROM eclipse-temurin:17-jre as runtime
COPY --from=builder /opt/porting-advisor /usr/bin/porting-advisor
ENTRYPOINT ["/usr/bin/porting-advisor"]

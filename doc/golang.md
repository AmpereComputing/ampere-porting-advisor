# Go on Ampere Processors

Go is a statically typed, compiled high-level programming language designed at Google. It is often referred to as Golang because of its former domain name, golang.org, but its proper name is Go. Visit _[Wikipedia](https://en.wikipedia.org/wiki/Go_(programming_language))_ to get more info about Go.

Go has added supported for ARM64 architecture since Go 1.5 (August 2015). Go was well-positioned for rasing momentum of ARM64 architecture in recent years. Go is well supported on Ampere Processor since it's ARM64 nature. visit _[Go on ARM and Beyond](https://go.dev/blog/ports)_ to get more info about Go's porting efforts on ARM architecture.

Go for ARM64 can be downloaded from _[the Go download page](https://go.dev/dl/)_.

## Recent releases

|  VERSION | RELEASE DATE | CHANGES ON ARM64   |
|:--------:|:------------:|:------------------:|
| Go 1.20  | 2023-02-01   | crypto/rsa now uses a new, safer, constant-time backend. This causes a CPU runtime increase for decryption operations between approximately 15% (RSA-2048 on amd64) and 45% (RSA-4096 on arm64) |
| Go 1.19  | 2022-08-02   | Support for debugger-injected function calls has been added on ARM64. The compiler now uses a jump table to implement large integer and string switch statements. Performance improvements for the switch statement vary but can be on the order of 20% faster |
| Go 1.18  | 2022-03-15   | Enhance ARM64 support for Windows and iOS |

## Regression results

Ampere running Daily regression tests on platforms powered by Ampere processors with Go official image on DockerHub to ensure each platform based on Ampere processors compatible with last changes from official Go release. Visit _[regression results page](https://amperecomputing.com/solution/go/regression-results)_ to find out regression status.

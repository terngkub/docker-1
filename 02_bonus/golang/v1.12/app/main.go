package main

import (
	"fmt"
	"runtime"

	"github.com/terngkub/gomod"
)

func main() {
	fmt.Println(runtime.Version())
	fmt.Println(gomod.Version())
}

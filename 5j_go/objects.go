// objects.go
package main

import (
	"fmt"
	"time"
)

type Obs struct {
	dice, person, field int
}

type Dice interface {
	Shuffle()  // さいころをふる
}
package main

import (
	"fmt"
	"github.com/kapitanov/go-teamcity"
)

func main() {
	tcClient := teamcity.NewClient("https://teamcity.jetbrains.com", teamcity.GuestAuth())

	projects, err := tcClient.GetProjects()
	if err != nil {
		panic(err)
	}

	fmt.Printf("List of projects:\n")
	for _, project := range projects {
		fmt.Printf(" * %s\n", project.ID)
	}
}
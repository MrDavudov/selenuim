package main

import (
    "github.com/tebeka/selenium"
    "github.com/tebeka/selenium/chrome"
)

const (
	// These paths will be different on your system.
	chromeDriverPath = "C:\\chromedriver\\chromedriver.exe"
	port           	 = 4444
)

func main() {
	// Run Chrome browser
	service, err := selenium.NewChromeDriverService(chromeDriverPath, port)
	if err != nil {
		panic(err)
	}
	defer service.Stop()

	caps := selenium.Capabilities{}
	caps.AddChrome(chrome.Capabilities{Args: []string{
		"window-size=1920x1080",
		"--no-sandbox",
		"--disable-dev-shm-usage",
		"disable-gpu",
		// "--headless",  // comment out this line to see the browser
	}})

	Driver, err := selenium.NewRemote(caps, "")
	if err != nil {
		panic(err)
	}


	// test selenium
	if err := l_1_2(Driver); err != nil {
		panic(err)
	}
}

